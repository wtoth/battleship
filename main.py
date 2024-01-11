from board import Board
import board_helpers

def main():
    #board construction
    player_board = Board()
    pieces = [5, 4, 3, 3, 2]

    #place pieces loop
    for piece in pieces:
        placement_result = False
        while not placement_result:
            player_board.display_board()
            row = input("Enter the starting row: ")
            col = input("Enter the starting column: ")
            orientation_loop = True
            while orientation_loop:
                orientation = input("Enter the orientation (v - vertical, h - horizontal)): ")
                if (orientation == "h") or (orientation == "v"):
                    orientation_loop = False
            placement_result = player_board.add_ship([int(row), int(col)], piece, orientation) 

    player_board.display_board()

    computer_board = board_helpers.computer_automated_board_construction()
    print("the computer has generated its board")
    
    #game loop
    while True:

        # add game logic here

        if computer_board.hits() >= 17:
            print("You win!!! Congrats")
            break
        if player_board.hits() >= 17:
            print("The computer wins :( better luck next time")
            break

if __name__ == "__main__":
    main()