import random as rnd
import emoji
from rich.table import Table
from utility import UtilityMixin


class Board(UtilityMixin):

    def _initiate_cells(self) -> list:
        """
        Preparing values of cells 2-d list
        """
        return [['🔒' for col in range(self.col_size)]
                for row in range(self.row_size)]

    def _get_random_cors(self) -> tuple:
        """
        Getting a tuple of random coordinations (row, col)
        """
        return (rnd.randrange(self.row_size), rnd.randrange(self.col_size))

    def _initiate_mine(self) -> tuple:
        """
        Generate mine random coordination
        """
        rand_cors = self._get_random_cors()
        return rand_cors if not self.has_mine(rand_cors)\
            else self._initiate_mine()

    def _set_mines(self) -> None:
        """
        Setting the mines list by mines_num number of elements
        """
        while len(self.mines) != self.mines_num:
            mine_cors = self._initiate_mine()
            self.mines.append(mine_cors)

    def _build_cells(self) -> None:
        """
        Set cells and mines lists
        """
        self.cells = self._initiate_cells()
        self._set_mines()

    def __init__(self, col_size: int, row_size: int, mines_num: int) -> None:
        """
        Initialize Board object
        """
        self.col_size, self.row_size = col_size, row_size
        self.mines_num = mines_num
        self.revealed_cells, self.mines = [], []
        self._build_cells()

    def has_mine(self, cors) -> bool:
        """
        Check if the given cell exist in the mines list
        """
        return cors in self.mines

    def get_neighbour_cells_cors(self, cors: tuple) -> list:
        """
        Get a list of all direct neighbours coordinates of a cell
        """
        row, col = cors[0], cors[1]
        return [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                (row, col - 1), (row, col + 1),
                (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]

    def calculate_neighbour_mines_num(self, cors: tuple) -> int:
        """
        Calculate the number of the mines in neighbours for a specific cell
        """
        return sum([self.has_mine(cell_cors)
                    for cell_cors in
                    self.get_neighbour_cells_cors(cors)])

    def set_neighbour_mines_num_style(self, neighbour_mines_num: int) -> str:
        """
        Set the neighbour mines num text style based on itself,
        the level of danger: >= 3 Red, >=1 Orange, 0 Green
        and add the bold style
        """
        color = "[red]" if neighbour_mines_num >= 3 else "[#f45f0e]" \
            if neighbour_mines_num >= 1 else '[green]'
        return f"[bold]{color}{neighbour_mines_num}"

    def set_neighbour_mines_num(self, cors: tuple) -> None:
        """
        Set the content of the given cell to be it's neighbour mines number
        """
        neighbour_mines_num = self.calculate_neighbour_mines_num(cors)
        self.cells[cors[0]][cors[1]] = self.set_neighbour_mines_num_style(
            neighbour_mines_num)

    def is_already_revealed(self, cors: tuple) -> bool:
        """
        Check if the cell revealed before already
        """
        return cors in self.revealed_cells

    def is_all_cells_revealed(self) -> bool:
        """
        Check if all non-mines cells has been revealed
        """
        return len(self.revealed_cells) + self.mines_num ==\
            self.col_size * self.row_size

    def update_board_data(self, cors: tuple) -> None:
        """
        Add the cell to the revealed cells list and update it's content
        """
        self.revealed_cells.append(cors)
        self.set_neighbour_mines_num(cors)

    def reveal_cell(self, cors: tuple) -> bool:
        """
        Check cell if it's contains a mine or not, and if not update the board
        """
        if self.has_mine(cors):
            return True
        else:
            self.update_board_data(cors)
            return False

    def _create_table(self, style: str) -> Table:
        """
        Create rich.table with specific style and add all columns
        """
        table = Table(title="", show_lines=True)
        table.add_column("#", width=1)
        for indx in range(self.col_size):
            table.add_column(f"{style}{indx}", width=3)
        return table

    def _add_rows(self, table: Table, style: str) -> Table:
        """
        Add styled rows for a given rich.table
        """
        row_indx = 0
        for row in self.cells:
            new_row = [f"{style}{row_indx}"] + row
            table.add_row(*new_row)
            row_indx += 1
        return table

    def _add_mine(self, row: int, col: int) -> None:
        """
        Replace the content of a cell with mine emoji if it's in the mines list
        """
        if self.has_mine((row, col)):
            self.cells[row][col] = emoji.emojize(':bomb:')

    def show_mines(self) -> None:
        """
        Replace content of all cells which in the mines list
        """
        [[self._add_mine(row, col) for col in range(self.col_size)]
         for row in range(self.row_size)]

    def draw_board(self) -> Table:
        """
        Draw a table of row and column based on the board dimensions
        """
        style = "[bold][blue]"
        table = self._create_table(style)
        table = self._add_rows(table, style)
        return table

    def show(self) -> None:
        """
        Show board on terminal
        """
        table = self.draw_board()
        self.print_on_console(table)

    def show_real_board(self) -> None:
        """
        Show board on terminal with mine shown
        """
        self.show_mines()
        table = self.draw_board()
        self.print_on_console(table)
