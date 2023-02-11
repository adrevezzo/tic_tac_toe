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


    def update_combos(self):
        self.left_column = [
            self.board_positions.get("top_left"),
            self.board_positions.get("mid_left"),
            self.board_positions.get("bot_left")
        ]

        self.mid_column = [
            self.board_positions.get("top_mid"),
            self.board_positions.get("mid_mid"),
            self.board_positions.get("bot_mid")
        ]

        self.right_column = [
            self.board_positions.get("top_right"),
            self.board_positions.get("mid_right"),
            self.board_positions.get("bot_right")
        ]

        self.top_row = [
            self.board_positions.get("top_left"),
            self.board_positions.get("top_mid"),
            self.board_positions.get("top_right")
        ]

        self.mid_row = [
            self.board_positions.get("mid_left"),
            self.board_positions.get("mid_mid"),
            self.board_positions.get("mid_right")
        ]

        self.bottom_row = [
            self.board_positions.get("bot_left"),
            self.board_positions.get("bot_mid"),
            self.board_positions.get("bot_right")
        ]

        self.left_diagonal = [
            self.board_positions.get("top_left"),
            self.board_positions.get("mid_mid"),
            self.board_positions.get("bot_right")
        ]

        self.right_diagonal = [
            self.board_positions.get("top_right"),
            self.board_positions.get("mid_mid"),
            self.board_positions.get("bot_left")
        ]

        self.combos = [self.left_column, self.mid_column, self.right_column, self.top_row,
                       self.mid_row, self.bottom_row, self.left_diagonal, self.right_diagonal]
        
        return self.combos


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

        for combo in self.update_combos():
            result = self.check_combo(combo)
            if not result:
                return result
        return True

    def check_combo(self,combo):
        if " " not in combo and len(set(combo)) == 1:
            return False
        return True

