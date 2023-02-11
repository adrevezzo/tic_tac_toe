

def initialize_game():
    print("\nWelcome to Tic Tac Toe")

    cur_game = Board()
    pX = Player("X")
    pO = Player("O")
    active_player = pX

    return cur_game, pX, pO, active_player


def play_again():
    play_again = input("\nPlay Again? (y/n) ").upper()
    
    if play_again in ('Y', 'y', 'yes'):
        return game()

def game():
    cur_game, pX, pO, active_player = initialize_game()
    playing = True
    while playing:
        
        cur_game.show_board()
        cur_game.show_available_moves()
        try:
            move = int(input(f"\nPlayer {active_player.marker} Move (0-9): "))
            if move == 99:
                print("\nThanks for playing!")
                playing = False
            else:
                cur_game.post_move(move, active_player.marker)
                check_result = cur_game.game_check()

                if check_result[1] == "win":
                    print(f"\nPlayer {active_player.marker} Wins!")
                    playing = check_result[0]
                    play_again()

                
                elif check_result[1] == "draw":
                    print("No moves remaining. Draw. Thanks for playing!")
                    playing = check_result[0]
                    play_again()

                if active_player == pX:
                    active_player = pO
                else:
                    active_player = pX

        
        except ValueError as ve:
            os.system('clear')
            print("\n*****Please enter a valid number*****")
        except KeyError as ke:
            print("\n*****Please enter one of the remaining available moves*****")


game()