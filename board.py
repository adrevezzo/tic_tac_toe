import os

class Board:
    def __init__(self) -> None:
        self.board_positions = {
            "top_left": " ",
            "top_mid": " ",
            "top_right": " ",
            "mid_left": " ",
            "mid_mid": " ",
            "mid_right": " ",
            "bot_left": " ",
            "bot_mid": " ",
            "bot_right": " "
        }

        self.move_list = {
            "1. Top Left": "top_left",
            "2. Top Center": "top_mid",
            "3. Top Right": "top_right",
            "4. Middle Left": "mid_left",
            "5. Center": "mid_mid",
            "6. Middle Right": "mid_right",
            "7. Bottom Left": "bot_left",
            "8. Bottom Center": "bot_mid",
            "9. Bottom Right": "bot_right",
        }

        self.move_helper = {
            1:["1. Top Left", "top_left"],
            2:["2. Top Center", "top_mid"],
            3:["3. Top Right", "top_right"],
            4:["4. Middle Left", "mid_left"],
            5:["5. Center", "mid_mid"],
            6:["6. Middle Right", "mid_right"],
            7:["7. Bottom Left", "bot_left"],
            8:["8. Bottom Center", "bot_mid"],
            9:["9. Bottom Right", "bot_right"],
        }


    def show_board(self):
        board = f"""

 {self.board_positions["top_left"]} | {self.board_positions["top_mid"]} | {self.board_positions["top_right"]}
-----------
 {self.board_positions["mid_left"]} | {self.board_positions["mid_mid"]} | {self.board_positions["mid_right"]}
-----------
 {self.board_positions["bot_left"]} | {self.board_positions["bot_mid"]} | {self.board_positions["bot_right"]}

"""
        print(board)
    
    def show_available_moves(self):
        print("Available Moves:")
        for key,value in self.move_helper.items():
            print(value[0])

    def post_move(self, move_number, player):
        os.system('clear')
        move = self.move_helper[move_number]
        self.board_positions[move[1]] = player
        self.move_helper.pop(move_number)
        self.show_board()

    def game_check(self):
        if len(self.move_helper) == 0:
            print("No moves remaining. Draw. Thanks for playing!")
            return False
        return True
