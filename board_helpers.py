from board import Board
from random import randrange, randint

def computer_board_construction(pieces):
    board = Board()

    #place pieces loop
    for piece in pieces:
        placement_result = False
        while not placement_result:
            row = randrange(10)
            col = randrange(10)
            orientation = randint(0,1)
            if orientation == 1:
                orientation = "v"
            else:
                orientation = "h"
            placement_result = board.add_ship([row, col], piece, orientation) 
    return board

def computer_attack():
    attack_row = randint(0,9)
    attack_col = randint(0,9)
    return [attack_row, attack_col]

#test_board = computer_board_construction()
#test_board.display_board()