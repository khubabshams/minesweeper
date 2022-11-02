import random as rnd
import copy
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
from termcolor import colored
from pyfiglet import Figlet
import time

MENU_ACTIONS = {1: "initiate_game", 2: "show_rules", 3: "show_about"}

LEVELS = {1: {'name': 'Easy', 'mines': 3, 'col': 3, 'row': 3},
          2: {'name': 'Medium', 'mines': 6, 'col': 4, 'row': 4},
          3: {'name': 'Hard', 'mines': 16, 'col': 6, 'row': 6}}


class Board:

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

    def print_table(self, table):
        Console().print(table, justify="center")

    def show(self):
        table = self.draw_board()
        self.print_table(table)

    def show_real_board(self):
        self.show_mines()
        table = self.draw_board()
        self.print_table(table)


class User:

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login(self):
        pass

    def signup(self):
        pass


class Game:

    def _get_rules(self):
        return "Choosing a square which doesn't have a mine reveals the number of neighbouring squares containing mines. By a process of deduction, elimination and guesswork, this information can be used to work out where all the mines are."

    def _get_about(self):
        return "Minesweeper:\na Command line version of Minesweeper game developed by Khubab Shams."

    def _get_level_menu(self):
        lev_text = "\n".join([f"## {lev}. {LEVELS[lev]['name']} {LEVELS[lev]['col']}x{LEVELS[lev]['row']} ({LEVELS[lev]['mines']} Mines)"
                              for lev in LEVELS])
        return f"# Levels:\n{lev_text}"

    def _get_position_max_value(self, position_type):
        level_info = LEVELS[self.level]
        return level_info['row'] if position_type == 'row' else level_info['col']

    def formatted_title(self, text):
        fig = Figlet(font='rectangles', justify="center", width=150)
        print(colored(fig.renderText(text), attrs=['bold']))

    def formatted_menu(self, text):
        menu_text = Markdown(text)
        Console().print(menu_text, justify="center")

    def __init__(self):
        pass

    def run(self):
        self.formatted_title("Welcome to Minesweeper!")
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
            print("Invalid input, please enter a number from the displayed choices only.")
        except ValueError as e:
            print("Invalid input, please enter numbers only to select an item.")
        failure_callback_func = getattr(self, callback_func)
        failure_callback_func(arg) if arg else failure_callback_func()

    def get_menu_choice(self, menu_text, possible_values, callback_func):
        self.formatted_menu(menu_text)
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
            f"Enter the number of the {position_type} of the selected cell here:\n")
        max = self._get_position_max_value(position_type)
        return self.validate_number_input(position_input, list(range(max)),
                                          "get_single_position", position_type)

    def get_user_input(self):
        row_position = self.get_single_position('row')
        col_position = self.get_single_position('column')
        return (row_position, col_position)

    def validate_cors(self, cors, board):
        if board.is_already_revealed(cors):
            print("Entered cell position already revealed, please try new ones.")
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
        self.formatted_title(final_message)
        time.sleep(5)
        self.run_replay_menu()

    def run_replay_menu(self):
        replay_menu = "# Play again:\n## 1. Yes\n## 2. No"
        menu_choice = self.get_menu_choice(replay_menu, [1, 2],
                                           "run_replay_menu")
        self.start_game() if menu_choice == 1 else self.run_main_menu

    def initiate_game(self):
        self.level = self.get_game_level()
        self.start_game()

    def start_game(self):
        board = self.initiate_board()
        self.play_round(board)

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


main()
