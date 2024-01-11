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
            if len(temp_row) > 0:
                display_board.append(temp_row)
        for row in display_board:
            print(*row)

    def add_ship(self, position, length, orientation):
        # make sure on board
        # vertical placement
        if orientation == "v":
            if (position[0] > 10) or (position[0] < 0):
                raise Exception("add_ship not on the board")
            if ((position[0] + length) > 10) or ((position[0] + length) < 0):
                raise Exception("add_ship not on the board")
            if (position[1] > 10) or (position[1] < 0):
                raise Exception("add_ship not on the board")
        # horizontal placement
        elif orientation == "h":
            if (position[0] > 10) or (position[0] < 0):
                raise Exception("add_ship not on the board")
            if ((position[1] + length) > 10) or ((position[1] + length) < 0):
                raise Exception("add_ship not on the board")
            if (position[1] > 10) or (position[1] < 0):
                raise Exception("add_ship not on the board")
        else:
            raise Exception("Orientation is not h or v")
        
        # make sure all squares are clear
        if orientation == "v":
            bottom_square = position[0] + length
            for i in range(position[0], bottom_square):
                if self.board_list[i][position[1]].has_ship():
                    raise Exception(f"ship on {i} {position[1]}")
            # add the ship
            for i in range(position[0], bottom_square):
                self.board_list[i][position[1]].add_ship()
        

        elif orientation == "h":
            right_square = position[1] + length
            for i in range(position[1], right_square):
                if self.board_list[position[0]][i].has_ship():
                    raise Exception(f"ship on {position[0]} {i}")
            # add the ship
            for i in range(position[1], right_square):
                self.board_list[position[0]][i].add_ship()
        return True

    def is_space_occupied(self):
        pass

#board = Board()
#board.display_board()