from datetime import date
from time import sleep


# the current date
today = date.today()

# playing board
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


# dislpays the board in the terminal
def show_board():
    print("+---+---+---+")
    print(f"| {board[0][0]} | {board[0][1]} | {board[0][2]} |")
    print("+---+---+---+")
    print(f"| {board[1][0]} | {board[1][1]} | {board[1][2]} |")
    print("+---+---+---+")
    print(f"| {board[2][0]} | {board[2][1]} | {board[2][2]} |")
    print("+---+---+---+")


# animation that plays when you win
def win_animation(winner):
    for i in range(1, 3):
        print("                ___________  ")
        print("               |           | ")
        print(f"       ___     | Hurray {winner.title()}! | ")
        print("      /o o\   <____________|  ")
        print("      \___/ /                ")
        print("    __|   |/                 ")
        print("   /  |   |                  ")
        print("      |___|                  ")
        print("      /   \                  ")
        print("     /     \                 ")
        sleep(0.3)

        print("                ___________  ")
        print("               |           | ")
        print(f"       ___     | Hurray {winner.title()}! | ")
        print("      /o o\   <____________| ")
        print("   __ \___/ __               ")
        print("     \|   |/                 ")
        print("      |   |                  ")
        print("      |___|                  ")
        print("      /   \                  ")
        print("     /     \                 ")
        sleep(0.3)

        print("                ___________  ")
        print("               |           | ")
        print(f"       ___     | Hurray {winner.title()}! | ")
        print("      /o o\   <____________| ")
        print("    \ \___/                  ")
        print("     \|   |__                ")
        print("      |   |  \               ")
        print("      |___|                  ")
        print("      /   \                  ")
        print("     /     \                 ")
        sleep(0.3)

        print("                ___________  ")
        print("               |           | ")
        print(f"       ___     | Hurray {winner.title()}! | ")
        print("      /o o\   <____________| ")
        print("   __ \___/ __               ")
        print("     \|   |/                 ")
        print("      |   |                  ")
        print("      |___|                  ")
        print("      /   \                  ")
        print("     /     \                 ")
        sleep(0.3)

        print("                ___________  ")
        print("               |           | ")
        print(f"       ___     | Hurray {winner.title()}! | ")
        print("      /o o\   <____________|  ")
        print("      \___/ /                ")
        print("    __|   |/                 ")
        print("   /  |   |                  ")
        print("      |___|                  ")
        print("      /   \                  ")
        print("     /     \                 ")
        sleep(0.3)

        print("                ___________  ")
        print("               |           | ")
        print(f"       ___     | Hurray {winner.title()}! | ")
        print("      /o o\   <____________| ")
        print("   __ \___/ __               ")
        print("     \|   |/                 ")
        print("      |   |                  ")
        print("      |___|                  ")
        print("      /   \                  ")
        print("     /     \                 ")
        sleep(0.3)

        print("                ___________  ")
        print("               |           | ")
        print(f"       ___     | Hurray {winner.title()}! | ")
        print("      /- -\   <____________| ")
        print("    \ \___/                  ")
        print("     \|   |__                ")
        print("      |   |  \               ")
        print("      |___|                  ")
        print("      /   \                  ")
        print("     /     \                 ")
        sleep(0.3)

        print("                ___________  ")
        print("               |           | ")
        print(f"       ___     | Hurray {winner.title()}! | ")
        print("      /o o\   <____________| ")
        print("   __ \___/ __               ")
        print("     \|   |/                 ")
        print("      |   |                  ")
        print("      |___|                  ")
        print("      /   \                  ")
        print("     /     \                 ")
        sleep(0.3)
        
    sleep(0.4)
    print("                ___________            ")
    print("               |           |           ")
    print(f"       ___     |           |           ")
    print("      /o o\   <____________|           ")
    print("    \ \___/ /                          ")
    print("     \|   |/                           ")
    print("      |   |                            ")
    print("      |___|                            ")
    print("      /   \                            ")
    print(f"     /     \      {today}              ")
    sleep(0.1)

    print("                ___________            ")
    print("               |           |           ")
    print(f"       ___     |P          |           ")
    print("      /o o\   <____________|           ")
    print("    \ \___/ /                          ")
    print("     \|   |/                           ")
    print("      |   |                            ")
    print("      |___|                            ")
    print("      /   \                            ")
    print(f"     /     \      {today}              ")
    sleep(0.1)

    print("                ___________            ")
    print("               |           |           ")
    print(f"       ___     |Pl         |           ")
    print("      /o o\   <____________|           ")
    print("    \ \___/ /                          ")
    print("     \|   |/                           ")
    print("      |   |                            ")
    print("      |___|                            ")
    print("      /   \                            ")
    print(f"     /     \      {today}              ")
    sleep(0.1)

    print("                ___________            ")
    print("               |           |           ")
    print(f"       ___     |Pla        |           ")
    print("      /o o\   <____________|           ")
    print("    \ \___/ /                          ")
    print("     \|   |/                           ")
    print("      |   |                            ")
    print("      |___|                            ")
    print("      /   \                            ")
    print(f"     /     \      {today}              ")
    sleep(0.1)

    print("                ___________            ")    
    print("               |           |           ")
    print(f"       ___     |Play       |           ")
    print("      /o o\   <____________|           ")
    print("    \ \___/ /                          ")
    print("     \|   |/                           ")
    print("      |   |                            ")
    print("      |___|                            ")
    print("      /   \                            ")
    print(f"     /     \      {today}              ")
    sleep(0.1)

    print("                ___________            ")
    print("               |           |           ")
    print(f"       ___     |Play a     |           ")
    print("      /o o\   <____________|           ")
    print("    \ \___/ /                          ")
    print("     \|   |/                           ")
    print("      |   |                            ")
    print("      |___|                            ")
    print("      /   \                            ")
    print(f"     /     \      {today}              ")
    sleep(0.1)

    print("                ___________            ")    
    print("               |           |           ")
    print(f"       ___     |Play ag    |           ")
    print("      /o o\   <____________|           ")
    print("    \ \___/ /                          ")
    print("     \|   |/                           ")
    print("      |   |                            ")
    print("      |___|                            ")
    print("      /   \                            ")
    print(f"     /     \      {today}              ")
    sleep(0.1)

    print("                ___________            ")    
    print("               |           |           ")
    print(f"       ___     |Play aga   |           ")
    print("      /o o\   <____________|           ")
    print("    \ \___/ /                          ")
    print("     \|   |/                           ")
    print("      |   |                            ")
    print("      |___|                            ")
    print("      /   \                            ")
    print(f"     /     \      {today}              ")
    sleep(0.1)

    print("                ___________            ")    
    print("               |           |           ")
    print(f"       ___     |Play agai  |           ")
    print("      /o o\   <____________|           ")
    print("    \ \___/ /                          ")
    print("     \|   |/                           ")
    print("      |   |                            ")
    print("      |___|                            ")
    print("      /   \                            ")
    print(f"     /     \      {today}              ")
    sleep(0.1)

    print("                ___________            ")    
    print("               |           |           ")
    print(f"       ___     |Play again?|           ")
    print("      /o o\   <____________|           ")
    print("    \ \___/ /                          ")
    print("     \|   |/                           ")
    print("      |   |                            ")
    print("      |___|                            ")
    print("      /   \                            ")
    print(f"     /     \      {today}              ")
    sleep(0.1)


# plays animation and asks if you wanna play again
def win(winner):
    sleep(1.5)
    win_animation(f"{winner.title()}")
    while True:
        again = input("\nDo you want to play again? ")
        if again == "yes":
            turn = input("\n'x' or 'o': ")
            show_board()
            break
        elif again == "no":
            quit()
        else:
            print("'yes' or 'no'")


# moves the pieces to right the right place
def move_to_pos(board_pos_y, board_pos_x):
    if board[board_pos_y][board_pos_x] == " ":
        board[board_pos_y][board_pos_x] = turn
        show_board()
        

turn = input("Who starts 'x' or 'o': ")

show_board()

while True:

    if turn != "x" and turn != "o":
        print("I said 'x' or 'o'")
        turn = input("Who starts 'x' or 'o': ")
        continue


    move = input(f"Yor turn: {turn.title()}!   [1-9] ")

    if move == "1":
        if board[0][0] != " ":
            print("There are someone there already\n")
            continue
        move_to_pos(0, 0)
    elif move == "2":
        if board[0][1] != " ":
            print("There are someone there already\n")
            continue
        move_to_pos(0, 1)
    elif move == "3":
        if board[0][2] != " ":
            print("There are someone there already\n")
            continue
        move_to_pos(0, 2)
    elif move == "4":
        if board[1][0] != " ":
            print("There are someone there already\n")
            continue
        move_to_pos(1, 0)
    elif move == "5":
        if board[1][1] != " ":
            print("There are someone there already\n")
            continue
        move_to_pos(1, 1)
    elif move == "6":
        if board[1][2] != " ":
            print("There are someone there already\n")
            continue
        move_to_pos(1, 2)
    elif move == "7":
        if board[2][0] != " ":
            print("There are someone there already\n")
            continue
        move_to_pos(2, 0)
    elif move == "8":
        if board[2][1] != " ":
            print("There are someone there already\n")
            continue
        move_to_pos(2, 1)
    elif move == "9":
        if board[2][2] != " ":
            print("There are someone there already\n")
            continue
        move_to_pos(2, 2)

    elif move == "q":
        break
    elif move == "change":
        turn = input("'x' or 'o': ")
        show_board()
    elif move == "reset":
        board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
        ]
        print("Reset the board!")
        show_board()
    elif move == "reset -a":
        board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
        ]
        turn = input("'x' or 'o': ")
        print("Reset the whole game!")
        show_board()
    else:
        print(f"[1-9] not {move}")
        continue


    # winning conditions
    if board[0][0] == turn and board[0][1] == turn and board[0][2] == turn:
        board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
            ]
        win(turn)
    elif board[1][0] == turn and board[1][1] == turn and board[1][2] == turn:
        board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
            ]
        win(turn)

    elif board[2][0] == turn and board[2][1] == turn and board[2][2] == turn:
        board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
            ]
        win(turn)

    elif board[0][0] == turn and board[1][0] == turn and board[2][0] == turn:
        board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
            ]
        win(turn)

    elif board[0][1] == turn and board[1][1] == turn and board[2][1] == turn:
        board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
            ]
        win(turn)

    elif board[0][2] == turn and board[1][2] == turn and board[2][2] == turn:
        board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
            ]
        win(turn)

    elif board[0][0] == turn and board[1][1] == turn and board[2][2] == turn:
        board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
            ]
        win(turn)

    elif board[0][2] == turn and board[1][1] == turn and board[2][0] == turn:
        board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
            ]
        win(turn)


    if turn == "x":
        turn = "o"
    elif turn == "o":
        turn = "x"

print("\n\nThanks For Playing!")