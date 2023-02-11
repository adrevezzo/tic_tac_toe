from board import Board
from players import Player
import os

class GameBrain:
    def __init__(self, active_player="X") -> None:
        self.welcome = "\nWelcome to Tic Tac Toe"
        self.cur_game = Board()
        self.pX = Player("X")
        self.pO = Player("O")
        
        if active_player == "X":
            self.active_player = self.pX
        else:
            self.active_player = self.pO

        self.game_play()
    

    def game_play(self):
        # cur_game, pX, pO, active_player = initialize_game()
        playing = True
        while playing:
        
            self.cur_game.show_board()
            self.cur_game.show_available_moves()
            
            try:
                move = int(input(f"\nPlayer {self.active_player.marker} Move (0-9): "))
                if move == 99:
                    print("\nThanks for playing!")
                    playing = False
                else:
                    self.cur_game.post_move(move, self.active_player.marker)
                    check_result = self.cur_game.game_check()

                    if check_result[1] == "win":
                        print(f"\nPlayer {self.active_player.marker} Wins!")
                        playing = check_result[0]
                        self.play_again()

                    
                    elif check_result[1] == "draw":
                        print("No moves remaining. Draw. Thanks for playing!")
                        playing = check_result[0]
                        self.play_again()

                    if self.active_player == self.pX:
                        self.active_player = self.pO
                    else:
                        self.active_player = self.pX
            
            except ValueError as ve:
                os.system('clear')
                print("\n*****Please enter a valid number*****")
            except KeyError as ke:
                print("\n*****Please enter one of the remaining available moves*****")


    def play_again(self):
        play_again = input("\nPlay Again? (y/n) ").upper()
    
        if play_again in ('Y', 'y', 'yes'):
            first = input(f"\nWho will go first? (X / O) ").upper()
            return GameBrain(first)
        
        print("\Thanks for playing!")