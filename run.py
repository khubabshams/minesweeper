class Cell:

    def __init__(self, col_cor, row_cor):
        self.col_cor = col_cor
        self.row_cor = row_cor
        self.is_mine = False

    def get_neighbour_mines_num(self):
        pass

    def set_neighbour_mines_num(self):
        pass

    def has_mine(self):
        pass


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

    def __init__(self):
        self.rules = self._set_rules()
        self.about = self._set-about()

    def start(self):
        pass

    def show_main_menu(self):
        pass

    def show_rules(self):
        pass

    def show_about(self):
        pass

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
