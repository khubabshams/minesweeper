import random as rnd
import copy


class Board:

    def _initiate_cells(self):
        return [[0] * self.col_size] * self.row_size

    def _get_random_cors(self):
        return (rnd.randrange(self.col_size), rnd.randrange(self.row_size))

    def _set_mines(self):
        while len(self.mines) != self.mines_num:
            rand_cors = self._get_random_cors()
            if self.has_mine(rand_cors):
                continue
            self.mines.append(rand_cors)

    def _build_cells(self):
        self.cells = self._initiate_cells()
        self._set_mines()

    def __init__(self, col_size, row_size, mines_num):
        self.col_size, self.row_size = col_size, row_size
        self.mines_num = mines_num
        self.mines = []
        self.cells = self._build_cells()

    def has_mine(self, cors):
        return cors in self.mines

    def reveal_cell(self):
        pass

    def show(self):
        pass


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

    def _get_levels(self):
        return {1: {'name': 'Easy', 'mines': 3, 'col': 3, 'row': 3},
                2: {'name': 'Medium', 'mines': 6, 'col': 4, 'row': 4},
                3: {'name': 'Hard', 'mines': 16, 'col': 6, 'row': 6}}

    def _get_level_menu(self):
        levels = self._get_levels()
        lev_text = "\n".join([f"{lev}. {levels[lev]['name']} {levels[lev]['col']}x{levels[lev]['row']} ({levels[lev]['mines']} Mines)"
                              for lev in levels])
        return f"Levels:\n{lev_text}"

    def _initiate_boards(self, level):
        level_info = self._get_levels()[level]
        board = Board(level_info['col'], level_info['row'],
                      level_info['mines'])
        user_board = copy.deepcopy(board)
        return board, user_board

    def __init__(self):
        pass

    def start(self):
        print("Welcome to Minesweeper!")
        self.run_main_menu()

    def _validate_int_input(self, input, possible_values):
        int_input = int(input)
        return int_input in possible_values and int_input or False

    def validate_menu_choice(self, menu_choice, possible_values,
                             callback_func):
        try:
            menu_choice = self._validate_int_input(menu_choice,
                                                   possible_values)
            if menu_choice:
                return menu_choice
            print("Invalid input, please enter a number from the shown menu only.")
        except ValueError as e:
            print("Invalid input, please enter numbers only to select a menu item.")
        failure_callback_func = getattr(self, callback_func)
        failure_callback_func()

    def get_menu_choice(self):
        menu_choice = input("Enter the number of your choice here:\n")
        return self.validate_menu_choice(menu_choice, [1, 2, 3],
                                         "run_main_menu")

    def run_game(self):
        level = self.get_game_level()
        board, user_board = self._initiate_boards(level)

    def show_rules(self):
        print(self._get_rules())
        self.run_main_menu()

    def show_about(self):
        print(self._get_about())
        self.run_main_menu()

    def exec_menu_choice(self, menu_choice):
        menu_actions = {1: "run_game", 2: "show_rules", 3: "show_about"}
        function = getattr(self, menu_actions.get(menu_choice))
        function()

    def run_main_menu(self):
        print("Main Menu:\n1. Start Game\n2. Rules\n3. About")
        menu_choice = self.get_menu_choice()
        self.exec_menu_choice(menu_choice)

    def get_game_level(self):
        level_menu_text = self._get_level_menu()
        print(level_menu_text)
        user_level = input(
            "Enter the number of the level you want to play here:\n")
        return self.validate_menu_choice(user_level, [1, 2, 3],
                                         "get_game_level")

    def show_board(self):
        pass

    def get_user_input(self):
        pass

    def show_feedback_message(self):
        pass

    def end_game(self):
        pass


def main():
    game = Game()
    game.start()


main()
