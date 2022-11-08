from board import Board
from user import User
from utility import FeedbackMixin
import time
import re


MENU_ACTIONS = {1: "initiate_game", 2: "show_rules", 3: "show_about"}

LEVELS = {1: {'name': 'Easy', 'mines': 3, 'col': 3, 'row': 3},
          2: {'name': 'Medium', 'mines': 6, 'col': 4, 'row': 4},
          3: {'name': 'Hard', 'mines': 16, 'col': 6, 'row': 6}}


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

    def display_input(self, cors):
        """
        Display the entered coordinations to the user
        """
        print(f"You choosed row: {cors[0]},  column: {cors[1]}")
        time.sleep(1)

    def play_round(self, board):
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
            print(e)
            self.print_failure_message("an Error occurred during the "
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
