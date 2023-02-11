from board import Board

print("Welcome to Tic Tac Toe")
cur_game = Board()
cur_game.show_board()


playing = True

while playing:
    cur_game.show_available_moves()
    try:
        pX = int(input("\nPlayer X Move (0-9): "))
        if pX == 99:
            print("Thanks for playing!")
            playing = False
        else:
            cur_game.post_move(pX,"x")

    except ValueError as ve:
        print("\nPlease enter a valid number")
    except KeyError as ke:
        print("\nPlease enter one of the remaining available moves")




