import random as rnd
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
from termcolor import colored
from pyfiglet import Figlet
import time
import re
import bcrypt

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from getpass import getpass

MENU_ACTIONS = {1: "initiate_game", 2: "show_rules", 3: "show_about"}

LEVELS = {1: {'name': 'Easy', 'mines': 3, 'col': 3, 'row': 3},
          2: {'name': 'Medium', 'mines': 6, 'col': 4, 'row': 4},
          3: {'name': 'Hard', 'mines': 16, 'col': 6, 'row': 6}}

EMAIL_REGEX = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
CHAR_START_REGEX = r'^[a-zA-Z]'
NAME_LENGTH = 4
PASSWORD_LENGTH = 8


CRED = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(CRED)
FIREBASE_CLIENT = firestore.client()


class FeedbackMixin:

    def print_colored_message(self, message, color="white", attrs=[]):
        print(colored(message, color=color, attrs=attrs))

    def print_failure_message(self, error_message):
        self.print_colored_message(error_message, 'red')

    def print_success_message(self, success_message):
        self.print_colored_message(success_message, 'green')

    def print_on_console(self, content):
        Console().print(content, justify="center")

    def print_title(self, text):
        fig = Figlet(font='rectangles', justify="center", width=150)
        self.print_colored_message(fig.renderText(text), attrs=['bold'])

    def print_from_markup(self, markup_text):
        self.print_on_console(Markdown(markup_text))


class Board(FeedbackMixin):

    def _initiate_cells(self):
        return [['🔒' for col in range(self.col_size)]
                for row in range(self.row_size)]

    def _get_random_cors(self):
        return (rnd.randrange(self.col_size), rnd.randrange(self.row_size))

    def _initiate_mine(self):
        rand_cors = self._get_random_cors()
        return rand_cors if not self.has_mine(rand_cors)\
            else self._initiate_mine()

    def _set_mines(self):
        while len(self.mines) != self.mines_num:
            mine_cors = self._initiate_mine()
            self.mines.append(mine_cors)

    def _build_cells(self):
        self.cells = self._initiate_cells()
        self._set_mines()

    def __init__(self, col_size, row_size, mines_num):
        self.col_size, self.row_size = col_size, row_size
        self.mines_num = mines_num
        self.revealed_cells, self.mines = [], []
        self._build_cells()

    def has_mine(self, cors):
        return cors in self.mines

    def get_neighbour_cells_cors(self, row, col):
        return [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                (row, col - 1), (row, col + 1),
                (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]

    def calculate_neighbour_mines_num(self, cors):
        return sum([self.has_mine(cell_cors)
                    for cell_cors in
                    self.get_neighbour_cells_cors(cors[0], cors[1])])

    def set_neighbour_mines_num_style(self, neighbour_mines_num):
        color = "[red]" if neighbour_mines_num >= 3 else "[#f45f0e]" \
            if neighbour_mines_num >= 1 else '[green]'
        return f"[bold]{color}{neighbour_mines_num}"

    def set_neighbour_mines_num(self, cors):
        neighbour_mines_num = self.calculate_neighbour_mines_num(cors)
        self.cells[cors[0]][cors[1]] = self.set_neighbour_mines_num_style(
            neighbour_mines_num)

    def is_already_revealed(self, cors):
        return cors in self.revealed_cells

    def is_all_cells_revealed(self):
        return len(self.revealed_cells) + self.mines_num ==\
            self.col_size * self.row_size

    def update_board_data(self, cors):
        self.revealed_cells.append(cors)
        self.set_neighbour_mines_num(cors)

    def reveal_cell(self, cors):
        if self.has_mine(cors):
            return True
        else:
            self.update_board_data(cors)
            return False

    def _create_table(self, style):
        table = Table(title="", min_width=50, show_lines=True)
        table.add_column("#", width=1)
        for indx in range(self.col_size):
            table.add_column(f"{style}{indx}", width=3)
        return table

    def _add_rows(self, table, style):
        row_indx = 0
        for row in self.cells:
            new_row = [f"{style}{row_indx}"] + row
            table.add_row(*new_row)
            row_indx += 1
        return table

    def _add_mine(self, row, col):
        if self.has_mine((row, col)):
            self.cells[row][col] = "💥"

    def show_mines(self):
        [[self._add_mine(row, col) for col in range(self.col_size)]
         for row in range(self.row_size)]

    def draw_board(self):
        style = "[bold][blue]"
        table = self._create_table(style)
        table = self._add_rows(table, style)
        return table

    def show(self):
        table = self.draw_board()
        self.print_on_console(table)

    def show_real_board(self):
        self.show_mines()
        table = self.draw_board()
        self.print_on_console(table)


class User(FeedbackMixin):

    def __init__(self):
        pass

    def get_firestore_collection(self):
        return FIREBASE_CLIENT.collection(u'GameUsers')

    def _set_user_data(self, user_data):
        self.email = user_data.get('email')
        self.password = user_data.get('password')
        self.username = user_data.get('username')

    def _authentication_response(self, user_data):
        self._set_user_data(user_data)
        self.print_success_message(
            f"Hi {user_data.get('username')}, enjoy playing ...\n")
        time.sleep(1)

    def _verify_user_record(self, user_record, password):
        verified_password = user_record and bcrypt.\
            checkpw(password.encode('utf-8'), user_record["key"]) or False
        if not user_record or not verified_password:
            self.print_failure_message(
                "Wrong email or password, please try again")
            self.login()
        return user_record

    def _search_user_record(self, email):
        firestore_collection = self.get_firestore_collection()
        docs = firestore_collection.where(u'email', u'==', email).\
            limit(1).get()
        return docs and docs[0].to_dict() or False

    def authenticate(self, email, password):
        print("Getting things done ...")
        user_record = self._search_user_record(email)
        self._verify_user_record(user_record, password)
        self._authentication_response(user_record)
        return user_record

    def _is_email_registered(self, email):
        user_record = self._search_user_record(email)
        return user_record and True or False

    def _validate_email(self, email):
        if re.search(EMAIL_REGEX, email):
            if not self._is_email_registered(email):
                return True
            self.print_failure_message("Email already exists, "
                                       "please use a different email")
        else:
            self.print_failure_message("Please enter a valid email")
        return False

    def _get_hashed_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'),
                             bcrypt.gensalt(rounds=10))

    def _validate_credential(self, cred, length, cred_name):
        if re.search(CHAR_START_REGEX, cred):
            if len(cred) >= length:
                return True
            self.print_failure_message(
                f"{cred_name} must be a minimum of {length} characters")
        else:
            self.print_failure_message(f"{cred_name} must start with a letter")
        return False

    def _validate_username(self, name):
        return self._validate_credential(name, NAME_LENGTH, 'Name')

    def _validate_password(self, password, confirm=False):
        return self._validate_credential(password, PASSWORD_LENGTH, 'Password')

    def _validate_confirmed_password(self, password, password_confirm):
        if password != password_confirm:
            self.print_failure_message(
                "Confirm password doesn't match entered password")
            return self._get_confirmed_password()
        else:
            return password

    def _get_username(self, validate=True):
        name = input("Enter your name here:\n")
        validate and not self._validate_username(name) and \
            self._get_username(validate)
        return name

    def _get_email(self, validate=True):
        email = input("Enter your email here:\n")
        validate and not self._validate_email(email) and \
            self._get_email(validate)
        return email

    def _get_password(self, confirm=False, validate=True):
        confirmation = confirm and " confirmation" or ""
        password = getpass(prompt=f"Enter your password{confirmation}"
                           " here (hidden characters):")
        validate and not self._validate_password(password, confirm) and \
            self._get_password(confirm, validate)
        return password

    def _get_confirmed_password(self):
        password = self._get_password()
        password_confirm = self._get_password(confirm=True)
        return self._validate_confirmed_password(password, password_confirm)

    def _do_signup(self, username, email, password):
        hashed_password = self._get_hashed_password(password)
        user_data = {
            u'username': username,
            u'email': email,
            u'key': hashed_password
        }
        firestore_collection = self.get_firestore_collection()
        _, doc_ref = firestore_collection.add(user_data)
        return doc_ref

    def login(self):
        email = self._get_email(validate=False)
        password = self._get_password(validate=False)
        self.authenticate(email, password)

    def signup(self):
        username = self._get_username()
        email = self._get_email()
        password = self._get_confirmed_password()
        doc_ref = self._do_signup(username, email, password)
        self.authenticate(email, password)


class Game(FeedbackMixin):

    def _get_rules(self):
        return "Rules:\nChoosing a square which doesn't have a mine reveals"
        "the number of neighbouring squares containing mines. "
        "By a process of deduction, elimination and guesswork, "
        "this information can be used to work out where all the mines are."

    def _get_about(self):
        return "Minesweeper:\na Command line version of Minesweeper game "
        "developed by Khubab Shams."

    def _get_level_menu(self):
        lev_text = "\n".join([f"## {lev}. {LEVELS[lev]['name']} "
                              f"{LEVELS[lev]['col']}x{LEVELS[lev]['row']} "
                              f"({LEVELS[lev]['mines']} Mines)"
                              for lev in LEVELS])
        return f"# Levels:\n{lev_text}"

    def _get_position_max_value(self, position_type):
        level_info = LEVELS[self.level]
        return level_info['row'] if position_type == 'row' \
            else level_info['col']

    def __init__(self):
        self.user = User()

    def run(self):
        self.print_title("Welcome to Minesweeper!")
        time.sleep(1)
        self.process_user_login()
        self.run_main_menu()

    def _validate_int_input(self, input, possible_values):
        int_input = int(input)
        return int_input if int_input in possible_values else None

    def validate_number_input(self, input, possible_values,
                              callback_func, arg=None):
        try:
            int_input = self._validate_int_input(input, possible_values)
            if isinstance(int_input, int):
                return int_input
            self.print_failure_message(
                "Invalid input, please enter a number from the displayed "
                "choices only")
        except ValueError as e:
            self.print_failure_message(
                "Invalid input, please enter numbers only to select an item")
        failure_callback_func = getattr(self, callback_func)
        failure_callback_func(arg) if arg else failure_callback_func()

    def get_menu_choice(self, menu_text, possible_values, callback_func):
        self.print_from_markup(menu_text)
        menu_choice = input("Enter the number of your choice here:\n")
        return self.validate_number_input(menu_choice, possible_values,
                                          callback_func)

    def initiate_board(self):
        level_info = LEVELS[self.level]
        board = Board(level_info['col'], level_info['row'],
                      level_info['mines'])
        return board

    def get_single_position(self, position_type):
        position_input = input(
            f"Enter the number of the {position_type} of the selected cell"
            " here:\n")
        max = self._get_position_max_value(position_type)
        return self.validate_number_input(position_input, list(range(max)),
                                          "get_single_position", position_type)

    def get_user_input(self):
        row_position = self.get_single_position('row')
        col_position = self.get_single_position('column')
        return (row_position, col_position)

    def validate_cors(self, cors, board):
        if board.is_already_revealed(cors):
            self.print_failure_message("Entered cell position "
                                       "already revealed, please try new ones")
            self.play_round(board)

    def play_round(self, board):
        self.show_board(board)
        cors = self.get_user_input()
        self.validate_cors(cors, board)
        has_mine = board.reveal_cell(cors)
        self.finsh_round(has_mine, board)

    def finsh_round(self, has_mine, board):
        if has_mine:
            self.show_board(board, hide_mines=False)
            self.end_game("GAME OVER")
        elif board.is_all_cells_revealed():
            self.end_game("YOU WIN!")
        else:
            self.play_round(board)

    def end_game(self, final_message):
        self.print_title(final_message)
        time.sleep(5)
        self.run_replay_menu()

    def run_replay_menu(self):
        menu_choice = self.get_menu_choice("# Play again?\n## 1. Yes"
                                           "\n## 2. No", [1, 2],
                                           "run_replay_menu")
        self.start_game() if menu_choice == 1 else self.run_main_menu()

    def initiate_game(self):
        self.level = self.get_game_level()
        self.start_game()

    def start_game(self):
        board = self.initiate_board()
        self.play_round(board)

    def process_user_login(self):
        try:
            menu_choice = self.get_menu_choice("# Have account?\n## "
                                               "1. Yes, we will ask you to"
                                               " sign in\n## "
                                               "2. No, you can signup to have"
                                               " one", [1, 2],
                                               "process_user_login")
            self.user.login() if menu_choice == 1 else self.user.signup()
        except Exception as e:
            self.print_failure_message("an Error accured during the "
                                       "authentication process, "
                                       "please try again")
            self.process_user_login()

    def print_game_info(self, info):
        print(info)
        time.sleep(7)
        self.run_main_menu()

    def show_rules(self):
        self.print_game_info(self._get_rules())

    def show_about(self):
        self.print_game_info(self._get_about())

    def show_board(self, board, hide_mines=True):
        if hide_mines:
            board.show()
        else:
            board.show_real_board()

    def exec_menu_choice(self, menu_choice):
        function = getattr(self, MENU_ACTIONS.get(menu_choice))
        function()

    def run_main_menu(self):
        main_menu = "# Main Menu:\n## 1. Start Game\n## 2. Rules\n## 3. About"
        menu_choice = self.get_menu_choice(main_menu, [1, 2, 3],
                                           "run_main_menu")
        self.exec_menu_choice(menu_choice)

    def get_game_level(self):
        level_menu_text = self._get_level_menu()
        return self.get_menu_choice(level_menu_text, [1, 2, 3],
                                    "get_game_level")


def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    main()
