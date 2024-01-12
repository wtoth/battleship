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
            placement_result = player_board.add_ship([int(row) - 1, int(col) - 1], piece, orientation) 

    player_board.display_board()

    computer_board = board_helpers.computer_board_construction(pieces)
    # computer_board.display_board()
    print("The computer has generated its board \n")

    
    #game loop
    while True:
        # add game logic here
        player_attack = False
        while not player_attack:
            player_attack_row = input("Enter the row you want to attack: ")
            player_attack_col = input("Enter the column you want to attack: ")
            player_attack = computer_board.attack_square(int(player_attack_row) - 1, int(player_attack_col) - 1)
        print("\n")
        if computer_board.hits >= sum(pieces):
            print("You win!!! Congrats")
            break

        computer_attack = False
        print("Computers attack")
        while not computer_attack:
            board_attack_square = board_helpers.computer_attack()
            computer_attack = player_board.attack_square(board_attack_square[0], board_attack_square[1])
        print("\n")
        if player_board.hits >= sum(pieces):
            print("The computer wins :( better luck next time")
            break

if __name__ == "__main__":
    main()