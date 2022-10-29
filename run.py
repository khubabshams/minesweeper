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

    def _set_rules(self):
        return ""

    def _set_about(self):
        return ""

    def __init__(self):
        self.rules = self._set_rules()
        self.about = self._set_about()

    def start(self):
        print("Welcome to Minesweeper!")
        self.show_main_menu()

    def validate_menu_choice(self, menu_choice):
        try:
            menu_choice = int(menu_choice)
            if menu_choice in [1, 2, 3]:
                return menu_choice
            else:
                print("Invalid input, please select a number \
                    from the shown menu only.")
                self.show_main_menu()
        except ValueError as e:
            print("Invalid input, please use numbers only to select a menu \
                item.")

    def get_menu_choice(self):
        menu_choice = input("Enter the number of your choice here:\n")
        return self.validate_menu_choice(menu_choice)

    def show_main_menu(self):
        print("Main Menu\n1. Start Game\n2. Rules\n3. About")

    def show_rules(self):
        pass

    def show_about(self):
        pass

    def get_game_level(self):
        user_level = input("Enter the number of your choice here:\n")

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
