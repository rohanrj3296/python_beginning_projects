def game_board():
    print("PLAYERS, YOUR GAME BOARD IS:")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[1] + "|" + board[2] + "|" + board[3])

def assign_symbol():
    print("PLAYER 1, YOUR SYMBOL IS: X")
    print("PLAYER 2, YOUR SYMBOL IS: O")

def winning():
    if (board[7] == board[8] == board[9] == "X" or
        board[4] == board[5] == board[6] == "X" or
        board[1] == board[2] == board[3] == "X" or
        board[7] == board[4] == board[1] == "X" or
        board[8] == board[5] == board[2] == "X" or
        board[9] == board[6] == board[3] == "X" or
        board[7] == board[5] == board[3] == "X" or
        board[1] == board[5] == board[9] == "X"):
        return 1
    elif (board[7] == board[8] == board[9] == "O" or
          board[4] == board[5] == board[6] == "O" or
          board[1] == board[2] == board[3] == "O" or
          board[7] == board[4] == board[1] == "O" or
          board[8] == board[5] == board[2] == "O" or
          board[9] == board[6] == board[3] == "O" or
          board[7] == board[5] == board[3] == "O" or
          board[1] == board[5] == board[9] == "O"):
        return 2
    else:
        return 0

def game_on(player_symbol):
    player_input = 88
    while player_input not in game_range or board[player_input] in ['X', 'O']:
        player_input = int(input(f"PLAYER {player_symbol} PLEASE ENTER INDEX IN RANGE(1-9): "))

    board[player_input] = player_symbol

if __name__ == "__main__":
    board = ["#", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    game_range = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = "0"

    assign_symbol()

    for _ in range(4):
        game_on("X")
        game_board()
        if winning() == 1:
            print("PLAYER 1 WON THE GAME! BETTER LUCK NEXT TIME PLAYER 2")
            break



        game_on("O")
        game_board()
        if winning() == 2:
            print("PLAYER 2 WON THE GAME! BETTER LUCK NEXT TIME PLAYER 1")
            break

    else:
        print("IT'S A DRAW!")
