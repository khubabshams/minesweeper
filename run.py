import random as rnd
import copy


MENU_ACTIONS = {1: "run_game", 2: "show_rules", 3: "show_about"}


class Board:

    def _initiate_cells(self):
        return [[0 for c in range(self.col_size)]
                for r in range(self.row_size)]

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
        print(self.mines)

    def __init__(self, col_size, row_size, mines_num):
        self.col_size, self.row_size = col_size, row_size
        self.mines_num = mines_num
        self.revealed_cells, self.mines = [], []
        self._build_cells()

    def has_mine(self, cors):
        return cors in self.mines

    def get_neighbour_cells_cors(self, cors):
        row, col = cors[0], cors[1]
        return [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                (row, col - 1), (row, col + 1),
                (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]

    def calculate_neighbour_mines_num(self, cors):
        return sum([self.has_mine(cell_cors)
                    for cell_cors in
                    self.get_neighbour_cells_cors(cors)])

    def set_neighbour_mines_num(self, cors):
        neighbour_mines_num = self.calculate_neighbour_mines_num(cors)
        self.cells[cors[0]][cors[1]] = neighbour_mines_num

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

    def _get_position_max_value(self, position_type):
        level_info = self._get_levels()[self.level]
        return level_info['row'] if position_type == 'row' else level_info['col']

    def __init__(self):
        pass

    def start(self):
        print("Welcome to Minesweeper!")
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
        failure_callback_func(arg)

    def get_menu_choice(self):
        menu_choice = input("Enter the number of your choice here:\n")
        return self.validate_number_input(menu_choice, [1, 2, 3],
                                          "run_main_menu")

    def initiate_boards(self):
        level_info = self._get_levels()[self.level]
        board = Board(level_info['col'], level_info['row'],
                      level_info['mines'])
        user_board = copy.deepcopy(board)
        return board, user_board

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

    def validate_cors(self, cors, board, user_board):
        if user_board.is_already_revealed(cors):
            print("Entered cell position already revealed, please try new ones.")
            self.play_round(board, user_board)

    def play_round(self, board, user_board):
        cors = self.get_user_input()
        self.validate_cors(cors, board, user_board)
        has_mine = user_board.reveal_cell(cors)
        self.finsh_round(has_mine, board, user_board)

    def finsh_round(self, has_mine, board, user_board):
        if has_mine:
            print("GAME OVER")
        else:
            if user_board.is_all_cells_revealed():
                print("YOU WIN!")
            else:
                self.play_round(board, user_board)

    def run_game(self):
        self.level = self.get_game_level()
        board, user_board = self.initiate_boards()
        result = self.play_round(board, user_board)

    def show_rules(self):
        print(self._get_rules())
        self.run_main_menu()

    def show_about(self):
        print(self._get_about())
        self.run_main_menu()

    def exec_menu_choice(self, menu_choice):
        function = getattr(self, MENU_ACTIONS.get(menu_choice))
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
        return self.validate_number_input(user_level, [1, 2, 3],
                                          "get_game_level")

    def show_board(self):
        pass

    def show_feedback_message(self):
        pass

    def end_game(self):
        pass


def main():
    game = Game()
    game.start()


main()
