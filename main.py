print("Welcome to Tic Tac Toe")


move_map = {
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


print(
f"""

 {move_map["top_left"]} | {move_map["top_mid"]} | {move_map["top_right"]}
-----------
 {move_map["mid_left"]} | {move_map["mid_mid"]} | {move_map["mid_right"]}
-----------
 {move_map["bot_left"]} | {move_map["bot_mid"]} | {move_map["bot_right"]}

"""      
)
playing = True

while playing:
    p1 = input("\nPlayer One Move: ")

    if p1.lower() == "x":
        print("Thanks for playing!")
        playing = False
