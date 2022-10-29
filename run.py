class Board:

    def _set_mines(self):
        pass

    def _build_cells(self):
        pass

    def __init__(self, col_size, row_size, mines_num):
        self.col_size, self.row_size = col_size, row_size
        self.mines_num = mines_num
        self.cells = self._build_cells()

    def show(self):
        pass


class UserBoard(Board):

    def __init__(self, col_size, row_size, mines_num):
        super(Board, self).__init__(col_size, row_size, mines_num)
        self.cells_revealed = 0

    def reveal_cell(self):
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

    def __init__(self):
        pass

    def start(self):
        print("Welcome to Minesweeper!")
        self.run_main_menu()

    def _validate_int_input(self, input, possible_values):
        int_input = int(input)
        return int_input in possible_values and int_input or False

    def validate_menu_choice(self, menu_choice, possible_values, callback):
        try:
            menu_choice = self._validate_int_input(menu_choice,
                                                   possible_values)
            if not menu_choice:
                print("Invalid input, please enter a number from the shown menu only.")
                callback_func = getattr(self, callback)
                callback_func()
            return menu_choice
        except ValueError as e:
            print("Invalid input, please enter numbers only to select a menu item.")

    def get_menu_choice(self):
        menu_choice = input("Enter the number of your choice here:\n")
        return self.validate_menu_choice(menu_choice, [1, 2, 3],
                                         "run_main_menu")

    def run_game(self):
        level = self.get_game_level()

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
        levels = self._get_levels()
        lev_text = [f"{lev}. {levels[lev]['name']} {levels[lev]['col']}x{levels[lev]['row']} ({levels[lev]['mines']} Mines)"
                    for lev in levels].join("\n")
        print(f"Levels:\n{lev_text}")
        # print("Levels: \n1. Easy 3x3 (3 Mines)\n2. Medium 4x4 (6 Mines)\n3. Hard 6x6 (16 Mines)")
        user_level = input(
            "Enter the number of the level you want to play here:\n")
        return self.validate_menu_choice(user_level, [1, 2, 3],
                                         "get_game_level")

    def set_game_level(self, game_level):
        self.level = game_level

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
