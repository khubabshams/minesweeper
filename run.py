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
