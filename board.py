from square import Square

class Board:
    def __init__(self):
        self.board_list = []
        for i in range(10):
            col_list = []
            for j in range(10):
                temp_square = Square()
                col_list.append(temp_square)
            self.board_list.append(col_list)

    def display_board(self):
        display_board = []
        for row in self.board_list:
            temp_row = []
            for col in row:
                if col.attacked == True:
                    temp_row.append("X")
                elif col.ship == True:
                    temp_row.append("O")
                else:
                    temp_row.append("-")
            display_board.append(temp_row)
        for row in display_board:
            print(row)

    def add_ship(self, length, orientation):
        # make sure on board

        # make sure all squares are clear

        # if both true: update desired squares and return True
        pass

    def is_space_occupied(self):
        pass

board = Board()
print(board.display_board())
