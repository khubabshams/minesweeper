from board import Board
from user import User
from utility import UtilityMixin
import time
from typing import Union
import signal
import sys


MENU_ACTIONS = {1: "initiate_game", 2: "show_rules", 3: "show_about"}

LEVELS = {1: {'name': 'Easy', 'mines': 3, 'col': 3, 'row': 3},
          2: {'name': 'Medium', 'mines': 6, 'col': 4, 'row': 4},
          3: {'name': 'Hard', 'mines': 16, 'col': 6, 'row': 6}}
DEFAULT_TITLE_SPACE = "\t\t"


class Game(UtilityMixin):

    def _get_welcome_title(self) -> str:
        """
        Get formatted 'welcome to minesweeper!' message
        """
        return f"""
{DEFAULT_TITLE_SPACE} _ _ _     _                      _
{DEFAULT_TITLE_SPACE}| | | |___| |___ ___ _____ ___   | |_ ___
{DEFAULT_TITLE_SPACE}| | | | -_| |  _| . |     | -_|  |  _| . |
{DEFAULT_TITLE_SPACE}|_____|___|_|___|___|_|_|_|___|  |_| |___|

{DEFAULT_TITLE_SPACE}                                               __
{DEFAULT_TITLE_SPACE} _____ _                                      |  |
{DEFAULT_TITLE_SPACE}|     |_|___ ___ ___ _ _ _ ___ ___ ___ ___ ___|  |
{DEFAULT_TITLE_SPACE}| | | | |   | -_|_ -| | | | -_| -_| . | -_|  _|__|
{DEFAULT_TITLE_SPACE}|_|_|_|_|_|_|___|___|_____|___|___|  _|___|_| |__|
{DEFAULT_TITLE_SPACE}                                  |_|
"""

    def _get_win_title(self) -> str:
        """
        Get formatted 'you win!' message
        """
        return f"""
{DEFAULT_TITLE_SPACE}                                     __
{DEFAULT_TITLE_SPACE} __ __ _____ _____    _ _ _ __ _____|  |
{DEFAULT_TITLE_SPACE}|  |  |     |  |  |  | | | |  |   | |  |
{DEFAULT_TITLE_SPACE}|_   _|  |  |  |  |  | | | |  | | | |__|
{DEFAULT_TITLE_SPACE}  |_| |_____|_____|  |_____|__|_|___|__|
"""

    def _get_game_over_title(self) -> str:
        """
        Get formatted 'game over' message
        """
        return f"""
{DEFAULT_TITLE_SPACE} _____ _____ _____ _____    _____ _____ _____ _____
{DEFAULT_TITLE_SPACE}|   __|  _  |     |   __|  |     |  |  |   __| __  |
{DEFAULT_TITLE_SPACE}|  |  |     | | | |   __|  |  |  |  |  |   __|    -|
{DEFAULT_TITLE_SPACE}|_____|__|__|_|_|_|_____|  |_____|\\___/|_____|__|__|
"""

    def _get_rules(self) -> str:
        """
        Get 'rules' text
        """
        return "Rules:\nChoosing a square which doesn't have a mine reveals"
        "the number of neighbouring squares containing mines. "
        "By a process of deduction, elimination and guesswork, "
        "this information can be used to work out where all the mines are."

    def _get_about(self) -> str:
        """
        Get 'about' text
        """
        return "Minesweeper:\na Command line version of Minesweeper game "
        "developed by Khubab Shams."

    def _get_level_menu(self) -> str:
        """
        Prepare 'level menu' content
        """
        lev_text = "\n".join([f"## {lev}. {LEVELS[lev]['name']} "
                              f"{LEVELS[lev]['col']}x{LEVELS[lev]['row']} "
                              f"({LEVELS[lev]['mines']} Mines)"
                              for lev in LEVELS])
        return f"# Levels:\n{lev_text}\n##"

    def _get_position_max_value(self, position_type: str) -> int:
        """
        Get maximum number of the index based on if it's a row or a column
        """
        level_info = LEVELS[self.level]
        return level_info['row'] if position_type == 'row' \
            else level_info['col']

    def __init__(self) -> None:
        """
        Initialize Game object
        """
        self.user = User()

    def run(self) -> None:
        """
        Welcome user, and process login if successed show main menu
        """
        print(self._get_welcome_title())
        self.sleep(2)
        self.process_user_login()
        self.run_main_menu()

    def _validate_int_input(self, input: str,
                            possible_values: list) -> Union[int, bool]:
        """
        Convert a given input to 'int'
        and check it's availability in a given list
        """
        int_input = int(input)
        return int_input if int_input in possible_values else None

    def validate_number_input(self, input: str, possible_values: list,
                              callback_func: str,
                              arg: str = None) -> Union[int, None]:
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

    def get_menu_choice(self, menu_text: str, possible_values: list,
                        callback_func: str) -> Union[int, None]:
        """
        Show menu text on terminal and get the user choice input
        and validate it
        """
        self.print_from_markup(menu_text)
        menu_choice = input("Enter the number of your choice here:\n")
        return self.validate_number_input(menu_choice, possible_values,
                                          callback_func)

    def initiate_board(self) -> Board:
        """
        Create the game board with dimensions based on the selected level
        """
        level_info = LEVELS[self.level]
        board = Board(level_info['col'], level_info['row'],
                      level_info['mines'])
        return board

    def get_single_position(self, position_type: str) -> Union[int, None]:
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

    def get_user_input(self) -> tuple:
        """
        Get the user input of the row and column of his chosen cell
        """
        row_position = self.get_single_position('row')
        col_position = self.get_single_position('column')
        return (row_position, col_position)

    def validate_cors(self, cors: tuple, board: Board) -> None:
        """
        Check if the cors not revealed before and if it's inform the user
        and recall the play round function
        """
        if board.is_already_revealed(cors):
            self.print_failure_message("Entered cell position "
                                       "already revealed, please try new ones")
            self.play_round(board)

    def display_input(self, cors: tuple) -> None:
        """
        Display the entered coordinations to the user
        """
        print(f"You choosed row: {cors[0]},  column: {cors[1]}")
        self.sleep(1)

    def play_round(self, board: Board) -> None:
        """
        Ask user for his guessed cell position,
        validate position and check mine in it
        """
        self.show_board(board)
        cors = self.get_user_input()
        self.validate_cors(cors, board)
        self.display_input(cors)
        has_mine = board.reveal_cell(cors)
        self.finsh_round(has_mine, board)

    def finsh_round(self, has_mine: bool, board: Board) -> None:
        """
        Check if chosen cell has mine and end game,
        or if it's the final correct guess otherwise start a new round
        """
        if has_mine:
            self.show_board(board, hide_mines=False)
            self.end_game(False)
        elif board.is_all_cells_revealed():
            self.end_game(True)
        else:
            self.play_round(board)

    def show_game_over(self) -> None:
        """
        Show 'game over' message on terminal
        """
        print(self._get_game_over_title())

    def show_win(self) -> None:
        """
        Show 'you win' message on terminal
        """
        print(self._get_win_title())

    def end_game(self, won: bool) -> None:
        """
        Show an end game message (win, lose), and call replay menu
        """
        self.show_win() if won else self.show_game_over()
        self.sleep(5)
        self.run_replay_menu()

    def run_replay_menu(self) -> None:
        """
        Show the user an options to replay game or back to the main menu
        """
        menu_choice = self.get_menu_choice("# Play again?\n## 1. Yes"
                                           "\n## 2. No\n##", [1, 2],
                                           "run_replay_menu")
        self.start_game() if menu_choice == 1 else self.run_main_menu()

    def initiate_game(self) -> None:
        """
        Get the level and start new game
        """
        self.level = self.get_game_level()
        self.start_game()

    def start_game(self) -> None:
        """
        Initialize the game board and start the first round
        """
        board = self.initiate_board()
        self.play_round(board)

    def process_user_login(self) -> None:
        """
        Show login menu and get the user input to call login or signup
        """
        try:
            menu_choice = self.get_menu_choice("# Have account?\n## "
                                               "1. Yes, we will ask you to"
                                               " sign in\n## "
                                               "2. No, you can signup to have"
                                               " one\n##", [1, 2],
                                               "process_user_login")
            self.user.login() if menu_choice == 1 else self.user.signup()
        except Exception as e:
            print(e)
            self.print_failure_message("an Error occurred during the "
                                       "authentication process, "
                                       "please try again")
            self.process_user_login()

    def print_game_info(self, info: str) -> None:
        """
        Print text on the terminal and get back to the main menu
        """
        print(info)
        self.sleep(5)
        self.run_main_menu()

    def show_rules(self) -> None:
        """
        Show 'rules' text
        """
        self.print_game_info(self._get_rules())

    def show_about(self) -> None:
        """
        Get 'about' text
        """
        self.print_game_info(self._get_about())

    def show_board(self, board: Board, hide_mines: bool = True) -> None:
        """
        Show the user board with an option to show mines places
        """
        if hide_mines:
            board.show()
        else:
            board.show_real_board()

    def exec_menu_choice(self, menu_choice: int) -> None:
        """
        Execute a specific function based on menu choice
        """
        function = getattr(self, MENU_ACTIONS.get(menu_choice))
        function()

    def run_main_menu(self) -> None:
        """
        Show the main menu on terminal, get the user input
        and respond accordingly
        """
        main_menu =\
            "# Main Menu:\n## 1. Start Game\n## 2. Rules\n ## 3. About\n##"
        menu_choice = self.get_menu_choice(main_menu, [1, 2, 3],
                                           "run_main_menu")
        self.exec_menu_choice(menu_choice)

    def get_game_level(self) -> int:
        """
        Show the level menu and get the user input
        """
        level_menu_text = self._get_level_menu()
        return self.get_menu_choice(level_menu_text, [1, 2, 3],
                                    "get_game_level")


def signal_handler(signal, frame):
    """
    Handle the default behaviour of Ctrl+C user input
    which cause (KeyboardInterrupt) Error
    Found on 'rtfpessoa' Github repos
    """
    print("\nExitting Minesweeper, click on 'Run Game' to restart again ...")
    sys.exit(0)


if __name__ == '__main__':
    """
    Create game instance and run the game
    """
    signal.signal(signal.SIGINT, signal_handler)
    game = Game()
    game.run()
