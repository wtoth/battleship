from board import Board
import board_helpers

def main():
    #board construction
    player_board = Board()
    pieces = []

    #place pieces loop
    for piece in pieces:
        placement_result = False
        while not placement_result:
            placement_result = player_board.add_ship()

    computer_board = board_helpers.computer_automated_board_construction()
    
    #game loop


    pass


if __name__ == "__main__":
    main()