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
        """
        Print given a text on terminal with specific color and attributes
        """
        print(colored(message, color=color, attrs=attrs))
        time.sleep(2)

    def print_failure_message(self, error_message):
        """
        Print an error message on terminal
        """
        self.print_colored_message(error_message, 'red')

    def print_success_message(self, success_message):
        """
        Print a success message on terminal
        """
        self.print_colored_message(success_message, 'green')

    def print_on_console(self, content):
        """
        Using rich console to print a given content
        """
        Console().print(content, justify="center")

    def print_title(self, text):
        """
        Print text in shape of centered rectangles
        """
        fig = Figlet(font='rectangles', justify="center", width=150)
        self.print_colored_message(fig.renderText(text), attrs=['bold'])

    def print_from_markup(self, markup_text):
        """
        Print a markdown formatted text on console
        """
        self.print_on_console(Markdown(markup_text))


class Board(FeedbackMixin):

    def _initiate_cells(self):
        """
        Preparing values of cells 2-d list
        """
        return [['🔒' for col in range(self.col_size)]
                for row in range(self.row_size)]

    def _get_random_cors(self):
        """
        Getting a tuple of random coordinations (row, col)
        """
        return (rnd.randrange(self.row_size), rnd.randrange(self.col_size))

    def _initiate_mine(self):
        """
        Generate mine random coordination
        """
        rand_cors = self._get_random_cors()
        return rand_cors if not self.has_mine(rand_cors)\
            else self._initiate_mine()

    def _set_mines(self):
        """
        Setting the mines list by mines_num number of elements
        """
        while len(self.mines) != self.mines_num:
            mine_cors = self._initiate_mine()
            self.mines.append(mine_cors)

    def _build_cells(self):
        """
        Set cells and mines lists
        """
        self.cells = self._initiate_cells()
        self._set_mines()

    def __init__(self, col_size, row_size, mines_num):
        """
        Initialize Board object
        """
        self.col_size, self.row_size = col_size, row_size
        self.mines_num = mines_num
        self.revealed_cells, self.mines = [], []
        self._build_cells()

    def has_mine(self, cors):
        """
        Check if the given cell exist in the mines list
        """
        return cors in self.mines

    def get_neighbour_cells_cors(self, cors):
        """
        Get a list of all direct neighbours coordinates of a cell
        """
        row, col = cors[0], cors[1]
        return [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                (row, col - 1), (row, col + 1),
                (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]

    def calculate_neighbour_mines_num(self, cors):
        """
        Calculate the number of the mines in neighbours for a specific cell
        """
        return sum([self.has_mine(cell_cors)
                    for cell_cors in
                    self.get_neighbour_cells_cors(cors)])

    def set_neighbour_mines_num_style(self, neighbour_mines_num):
        """
        Set the neighbour mines num text style based on itself,
        the level of danger: >= 3 Red, >=1 Orange, 0 Green
        and add the bold style
        """
        color = "[red]" if neighbour_mines_num >= 3 else "[#f45f0e]" \
            if neighbour_mines_num >= 1 else '[green]'
        return f"[bold]{color}{neighbour_mines_num}"

    def set_neighbour_mines_num(self, cors):
        """
        Set the content of the given cell to be it's neighbour mines number
        """
        neighbour_mines_num = self.calculate_neighbour_mines_num(cors)
        self.cells[cors[0]][cors[1]] = self.set_neighbour_mines_num_style(
            neighbour_mines_num)

    def is_already_revealed(self, cors):
        """
        Check if the cell revealed before already
        """
        return cors in self.revealed_cells

    def is_all_cells_revealed(self):
        """
        Check if all non-mines cells has been revealed
        """
        return len(self.revealed_cells) + self.mines_num ==\
            self.col_size * self.row_size

    def update_board_data(self, cors):
        """
        Add the cell to the revealed cells list and update it's content
        """
        self.revealed_cells.append(cors)
        self.set_neighbour_mines_num(cors)

    def reveal_cell(self, cors):
        """
        Check cell if it's contains a mine or not, and if not update the board
        """
        if self.has_mine(cors):
            return True
        else:
            self.update_board_data(cors)
            return False

    def _create_table(self, style):
        """
        Create rich.table with specific style and add all columns
        """
        table = Table(title="", min_width=50, show_lines=True)
        table.add_column("#", width=1)
        for indx in range(self.col_size):
            table.add_column(f"{style}{indx}", width=3)
        return table

    def _add_rows(self, table, style):
        """
        Add styled rows for a given rich.table
        """
        row_indx = 0
        for row in self.cells:
            new_row = [f"{style}{row_indx}"] + row
            table.add_row(*new_row)
            row_indx += 1
        return table

    def _add_mine(self, row, col):
        """
        Replace the content of a cell with mine emoji if it's in the mines list
        """
        if self.has_mine((row, col)):
            self.cells[row][col] = "💥"

    def show_mines(self):
        """
        Replace content of all cells which in the mines list
        """
        [[self._add_mine(row, col) for col in range(self.col_size)]
         for row in range(self.row_size)]

    def draw_board(self):
        """
        Draw a table of row and column based on the board dimensions
        """
        style = "[bold][blue]"
        table = self._create_table(style)
        table = self._add_rows(table, style)
        return table

    def show(self):
        """
        Show board on terminal
        """
        table = self.draw_board()
        self.print_on_console(table)

    def show_real_board(self):
        """
        Show board on terminal with mine shown
        """
        self.show_mines()
        table = self.draw_board()
        self.print_on_console(table)


class User(FeedbackMixin):

    def get_firestore_collection(self):
        """
        Get firebase game users collection
        """
        return FIREBASE_CLIENT.collection(u'GameUsers')

    def _set_user_data(self, user_data):
        """
        Set user's object attributes
        """
        self.email = user_data.get('email')
        self.password = user_data.get('password')
        self.username = user_data.get('username')

    def _authentication_response(self, user_data):
        """
        Set user's attributes and print auth success message
        """
        self._set_user_data(user_data)
        self.print_success_message(
            f"Hi {user_data.get('username')}, enjoy playing ...\n")

    def _verify_user_record(self, user_record, password):
        """
        Check the user record and compare the hashed password
        with the one from user record and give feedback accordingly
        """
        verified_password = user_record and bcrypt.\
            checkpw(password.encode('utf-8'), user_record["key"]) or False
        if not user_record or not verified_password:
            self.print_failure_message(
                "Wrong email or password, please try again")
            self.login()
        return user_record

    def _search_user_record(self, email):
        """
        Search the game users table by email for a record of user
        """
        firestore_collection = self.get_firestore_collection()
        docs = firestore_collection.where(u'email', u'==', email).\
            limit(1).get()
        return docs and docs[0].to_dict() or False

    def authenticate(self, email, password):
        """
        Identify if there's a record exist for user
        by searching by the given credentials
        """
        print("Getting things done ...")
        user_record = self._search_user_record(email)
        self._verify_user_record(user_record, password)
        self._authentication_response(user_record)
        return user_record

    def _is_email_registered(self, email):
        """
        Check if the email in use already in game users table
        """
        user_record = self._search_user_record(email)
        return user_record and True or False

    def _validate_email(self, email):
        """
        Check if entered email is valid and provide a feedback
        """
        if re.search(EMAIL_REGEX, email):
            if not self._is_email_registered(email):
                return True
            self.print_failure_message("Email already exists, "
                                       "please use a different email")
        else:
            self.print_failure_message("Please enter a valid email")
        return False

    def _get_hashed_password(self, password):
        """
        Hashing a given password using bcrypt
        """
        return bcrypt.hashpw(password.encode('utf-8'),
                             bcrypt.gensalt(rounds=10))

    def _validate_credential(self, cred, length, cred_name):
        """
        Check if the entered credential meets validity requirements
        (starting by letter, minimum characters size)
        """
        if re.search(CHAR_START_REGEX, cred):
            if len(cred) >= length:
                return True
            self.print_failure_message(
                f"{cred_name} must be a minimum of {length} characters")
        else:
            self.print_failure_message(f"{cred_name} must start with a letter")
        return False

    def _validate_username(self, name):
        """
        Check if entered name is starting with a letter,
        and have amin of NAME_LENGTH
        """
        return self._validate_credential(name, NAME_LENGTH, 'Name')

    def _validate_password(self, password, confirm=False):
        """
        Check if entered password is starting with a letter,
        and have amin of PASSWORD_LENGTH
        """
        return self._validate_credential(password, PASSWORD_LENGTH, 'Password')

    def _validate_confirmed_password(self, password, password_confirm):
        """
        Check [confirmation] password if it's meets the validity requirements
        """
        if password != password_confirm:
            self.print_failure_message(
                "Confirm password doesn't match entered password")
            return self._get_confirmed_password()
        else:
            return password

    def _get_username(self, validate=True):
        """
        Get the user input of his name and validate it
        """
        name = input("Enter your name here:\n")
        validate and not self._validate_username(name) and \
            self._get_username(validate)
        return name

    def _get_email(self, validate=True):
        """
        Get the user input of his email and validate it
        """
        email = input("Enter your email here:\n")
        validate and not self._validate_email(email) and \
            self._get_email(validate)
        return email

    def _get_password(self, confirm=False, validate=True):
        """
        Get the user input of his login [confirmation] password and validate it
        """
        confirmation = confirm and " confirmation" or ""
        password = getpass(prompt=f"Enter your password{confirmation}"
                           " here (hidden characters):")
        validate and not self._validate_password(password, confirm) and \
            self._get_password(confirm, validate)
        return password

    def _get_confirmed_password(self):
        """
        Get the user input of password and a confirmation and validate it
        """
        password = self._get_password()
        password_confirm = self._get_password(confirm=True)
        return self._validate_confirmed_password(password, password_confirm)

    def _do_signup(self, username, email, password):
        """
        Prepare user data and create a database record with it
        """
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
        """
        Ask for email, password. authenticate user credentials
        and show feedback
        """
        email = self._get_email(validate=False)
        password = self._get_password(validate=False)
        self.authenticate(email, password)

    def signup(self):
        """
        Rigister user data for first time in the database and authenticate
        """
        username = self._get_username()
        email = self._get_email()
        password = self._get_confirmed_password()
        doc_ref = self._do_signup(username, email, password)
        self.authenticate(email, password)


class Game(FeedbackMixin):

    def _get_rules(self):
        """
        Get 'rules' text
        """
        return "Rules:\nChoosing a square which doesn't have a mine reveals"
        "the number of neighbouring squares containing mines. "
        "By a process of deduction, elimination and guesswork, "
        "this information can be used to work out where all the mines are."

    def _get_about(self):
        """
        Get 'about' text
        """
        return "Minesweeper:\na Command line version of Minesweeper game "
        "developed by Khubab Shams."

    def _get_level_menu(self):
        """
        Prepare 'level menu' content
        """
        lev_text = "\n".join([f"## {lev}. {LEVELS[lev]['name']} "
                              f"{LEVELS[lev]['col']}x{LEVELS[lev]['row']} "
                              f"({LEVELS[lev]['mines']} Mines)"
                              for lev in LEVELS])
        return f"# Levels:\n{lev_text}"

    def _get_position_max_value(self, position_type):
        """
        Get maximum number of the index based on if it's a row or a column
        """
        level_info = LEVELS[self.level]
        return level_info['row'] if position_type == 'row' \
            else level_info['col']

    def __init__(self):
        """
        Initialize Game object
        """
        self.user = User()

    def run(self):
        """
        Welcome user, and process login if successed show main menu
        """
        self.print_title("Welcome to Minesweeper!")
        self.process_user_login()
        self.run_main_menu()

    def _validate_int_input(self, input, possible_values):
        """
        Convert a given input to 'int'
        and check it's availability in a given list
        """
        int_input = int(input)
        return int_input if int_input in possible_values else None

    def validate_number_input(self, input, possible_values,
                              callback_func, arg=None):
        """
        Validate and return an input if it's a number and available in given
        choices, and callback a function if it's not
        """
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
        """
        Show menu text on terminal and get the user choice input
        and validate it
        """
        self.print_from_markup(menu_text)
        menu_choice = input("Enter the number of your choice here:\n")
        return self.validate_number_input(menu_choice, possible_values,
                                          callback_func)

    def initiate_board(self):
        """
        Create the game board with dimensions based on the selected level
        """
        level_info = LEVELS[self.level]
        board = Board(level_info['col'], level_info['row'],
                      level_info['mines'])
        return board

    def get_single_position(self, position_type):
        """
        Get the position number of the chosen row or column
        and validate the input to ensure it's applicable on board
        """
        position_input = input(
            f"Enter the number of the {position_type} of the selected cell"
            " here:\n")
        max = self._get_position_max_value(position_type)
        return self.validate_number_input(position_input, list(range(max)),
                                          "get_single_position", position_type)

    def get_user_input(self):
        """
        Get the user input of the row and column of his chosen cell
        """
        row_position = self.get_single_position('row')
        col_position = self.get_single_position('column')
        return (row_position, col_position)

    def validate_cors(self, cors, board):
        """
        Check if the cors not revealed before and if it's inform the user
        and recall the play round function
        """
        if board.is_already_revealed(cors):
            self.print_failure_message("Entered cell position "
                                       "already revealed, please try new ones")
            self.play_round(board)

    def play_round(self, board):
        """
        Ask user for his guessed cell position,
        validate position and check mine in it
        """
        self.show_board(board)
        cors = self.get_user_input()
        self.validate_cors(cors, board)
        has_mine = board.reveal_cell(cors)
        self.finsh_round(has_mine, board)

    def finsh_round(self, has_mine, board):
        """
        Check if chosen cell has mine and end game,
        or if it's the final correct guess otherwise start a new round
        """
        if has_mine:
            self.show_board(board, hide_mines=False)
            self.end_game("GAME OVER")
        elif board.is_all_cells_revealed():
            self.end_game("YOU WIN!")
        else:
            self.play_round(board)

    def end_game(self, final_message):
        """
        Show an end game message (win, lose), and call replay menu
        """
        self.print_title(final_message)
        time.sleep(5)
        self.run_replay_menu()

    def run_replay_menu(self):
        """
        Show the user an options to replay game or back to the main menu
        """
        menu_choice = self.get_menu_choice("# Play again?\n## 1. Yes"
                                           "\n## 2. No", [1, 2],
                                           "run_replay_menu")
        self.start_game() if menu_choice == 1 else self.run_main_menu()

    def initiate_game(self):
        """
        Get the level and start new game
        """
        self.level = self.get_game_level()
        self.start_game()

    def start_game(self):
        """
        Initialize the game board and start the first round
        """
        board = self.initiate_board()
        self.play_round(board)

    def process_user_login(self):
        """
        Show login menu and get the user input to call login or signup
        """
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
        """
        Print text on the terminal and get back to the main menu
        """
        print(info)
        time.sleep(5)
        self.run_main_menu()

    def show_rules(self):
        """
        Show 'rules' text
        """
        self.print_game_info(self._get_rules())

    def show_about(self):
        """
        Get 'about' text
        """
        self.print_game_info(self._get_about())

    def show_board(self, board, hide_mines=True):
        """
        Show the user board with an option to show mines places
        """
        if hide_mines:
            board.show()
        else:
            board.show_real_board()

    def exec_menu_choice(self, menu_choice):
        """
        Execute a specific function based on menu choice
        """
        function = getattr(self, MENU_ACTIONS.get(menu_choice))
        function()

    def run_main_menu(self):
        """
        Show the main menu on terminal, get the user input
        and respond accordingly
        """
        main_menu = "# Main Menu:\n## 1. Start Game\n## 2. Rules\n## 3. About"
        menu_choice = self.get_menu_choice(main_menu, [1, 2, 3],
                                           "run_main_menu")
        self.exec_menu_choice(menu_choice)

    def get_game_level(self):
        """
        Show the level menu and get the user input
        """
        level_menu_text = self._get_level_menu()
        return self.get_menu_choice(level_menu_text, [1, 2, 3],
                                    "get_game_level")


if __name__ == '__main__':
    """
    Create game instance and run the game
    """
    game = Game()
    game.run()
