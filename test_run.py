import unittest
from run import User, Board, Game, LEVELS
from unittest.mock import patch


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.col_size, self.row_size, self.mines_num = 12, 14, 8
        self.board = Board(col_size=self.col_size, row_size=self.row_size,
                           mines_num=self.mines_num)
        self.mines, self.cells = self.board.mines, self.board.cells

    def test_cells_length(self):
        cols_list, rows_list = self.cells[0], self.cells
        self.assertTrue(len(cols_list) == self.col_size)
        self.assertTrue(len(rows_list) == self.row_size)

    def test_mines_length(self):
        self.assertTrue(len(self.mines) == self.mines_num)

    def test_cells_lock(self):
        all_cells_locked = all([all([cell == '🔒' for cell in row])
                                for row in self.cells])
        self.assertEqual(all_cells_locked, True, "Some cells left un-locked.")

    def test_has_mine(self):
        all_has_mines = all([self.board.has_mine(cors)
                             for cors in self.mines])
        any_has_mine = any([any([(row, col) not in self.mines
                                 and self.board.has_mine((row, col))
                                 for col in range(self.col_size)])
                            for row in range(self.row_size)])
        self.assertEqual(all_has_mines, True, "Expected mines only in these"
                         " board cells.")
        self.assertEqual(any_has_mine, False, "Expected no one of these cells"
                         " has a mine.")

    def test_reveal_cells(self):
        reveal_all = [[(r, c) not in self.mines and
                       self.board.reveal_cell((r, c))
                       for c in range(self.col_size)]
                      for r in range(self.row_size)]
        self.assertEqual(self.board.is_all_cells_revealed(), True,
                         "Expected all cells to be revealed.")


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User()

    def test_validate_email(self):
        valid_email, invalid_email = "valid@email.com", "invalid@email"
        already_exist_email = "already@exist.com"
        self.assertEqual(self.user._validate_email(valid_email), True,
                         "Expected True as email is valid.")
        self.assertEqual(self.user._validate_email(invalid_email), False,
                         "Expected False as email is invalid.")
        self.assertEqual(self.user._validate_email(already_exist_email), False,
                         "Expected False as email is already registered.")

    def test_validate_credential(self):
        valid_name, invalid_name_numbered = "validname", "1startswithnumber"
        invalid_short_password = "pass"
        self.assertEqual(self.user._validate_username(valid_name), True,
                         "Expected True as name is valid.")
        self.assertEqual(self.user._validate_password(invalid_short_password),
                         False, "Expected False as name less than min length.")
        self.assertEqual(self.user._validate_username(invalid_name_numbered),
                         False, "Expected False as name starting with number.")

    def test_firebase_connection(self):
        retrieve_user_record =\
            self.user._search_user_record("already@exist.com")
        self.assertEqual(isinstance(retrieve_user_record, dict),
                         True, "Expected user data in a dictionary.")

    def test_authenticate(self):
        authenicated_user_record =\
            self.user.authenticate("already@exist.com", "password")
        self.assertEqual(isinstance(authenicated_user_record, dict),
                         True, "Expected user data in a dictionary.")

    def test_do_signup(self):
        email, name, key = "abc@xyz.com", "justname", "password"
        doc_ref = self.user._do_signup(name, email, key)
        self.assertEqual(isinstance(doc_ref.get().to_dict(), dict), True,
                         "Expected document reference object to dict.")
        doc_ref.delete()


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        with patch('builtins.input', side_effect='2'):
            self.game.level = self.game.get_game_level()

    def test_game_board(self):
        board = self.game.initiate_board()
        self.assertEqual(len(board.cells), LEVELS[2]['col'],
                         "Expected different number of columns for level 2.")
        self.assertEqual(len(board.mines), LEVELS[2]['mines'],
                         "Expected different number of mines for level 2.")


if __name__ == '__main__':
    unittest.main()
