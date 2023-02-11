from board import Board
from players import Player


print("Welcome to Tic Tac Toe")
cur_game = Board()
cur_game.show_board()

pX = Player("X")
pO = Player("O")
active_player = pX



playing = True
while playing:
    cur_game.show_available_moves()
    try:
        move = int(input(f"\nPlayer {active_player.marker} Move (0-9): "))
        if move == 99:
            print("Thanks for playing!")
            playing = False
        else:
            cur_game.post_move(move, active_player.marker)
            playing = cur_game.game_check()
            if playing == False:
                print(f"\nPlayer {active_player.marker} Wins!")

            if active_player == pX:
                active_player = pO
            else:
                active_player = pX

    except ValueError as ve:
        print("\nPlease enter a valid number")
    except KeyError as ke:
        print("\nPlease enter one of the remaining available moves")


