from board import Board

print("Welcome to Tic Tac Toe")
cur_game = Board()
cur_game.show_board()


playing = True

while playing:
    cur_game.show_available_moves()
    pX = input("\nPlayer X Move: ")


    if pX.lower() == "x":
        print("Thanks for playing!")
        playing = False
    else:
        cur_game.post_move(pX,"x")

