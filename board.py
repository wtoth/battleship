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
        self.hits = 0

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
        i = 1
        # 3 spaces to indent
        print("   1 2 3 4 5 6 7 8 9 10")
        for row in display_board:
            if i < 10:
                # two spaces after the i to account for 10
                print(f"{i}  ", end="")
            else:
               # one space after the i
               print(f"{i} ", end="") 
            print(*row)
            i += 1
        print("\n")

    def add_ship(self, position, length, orientation):
        # make sure on board
        # vertical placement
        if orientation == "v":
            if (position[0] > 10) or (position[0] < 0):
                return False
                # raise Exception("add_ship not on the board")
            if ((position[0] + length) > 10) or ((position[0] + length) < 0):
                return False
                # raise Exception("add_ship not on the board")
            if (position[1] > 10) or (position[1] < 0):
                return False
                # raise Exception("add_ship not on the board")
        # horizontal placement
        elif orientation == "h":
            if (position[0] > 10) or (position[0] < 0):
                return False
                # raise Exception("add_ship not on the board")
            if ((position[1] + length) > 10) or ((position[1] + length) < 0):
                return False
                # raise Exception("add_ship not on the board")
            if (position[1] > 10) or (position[1] < 0):
                return False
                # raise Exception("add_ship not on the board")
        else:
            return False
            # raise Exception("Orientation is not h or v")
        
        # make sure all squares are clear
        if orientation == "v":
            bottom_square = position[0] + length
            for i in range(position[0], bottom_square):
                if self.board_list[i][position[1]].has_ship():
                    return False
                    # raise Exception(f"ship on {i} {position[1]}")
            # add the ship
            for i in range(position[0], bottom_square):
                self.board_list[i][position[1]].add_ship()

        elif orientation == "h":
            right_square = position[1] + length
            for i in range(position[1], right_square):
                if self.board_list[position[0]][i].has_ship():
                    return False
                    # raise Exception(f"ship on {position[0]} {i}")
            # add the ship
            for i in range(position[1], right_square):
                self.board_list[position[0]][i].add_ship()
        return True

    def attack_square(self, row, col):
        result = self.board_list[row][col].attack()
        if result[0] == False:
            return False
        elif result[1] == 1:
            print("Hit!!!")
            self.hits += 1
        else:
            print("Miss")
        return True

#board = Board()
#board.display_board()