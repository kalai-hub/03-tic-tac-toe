def board_print(board):
    for j in range(len(board)):
        for i in range(len(board[j])):
            print(board[j][i], end='')
            if i != len(board[j]) - 1:
                print("|", end='')
        if j != len(board) - 1:
            print("\n--------")


def place_player(board, position, symbol):
    print(symbol)
    if position <= 3:
        board[0][position - 1] = symbol
    elif position <= 6:
        board[1][position - 4] = symbol
    elif position <= 9:
        board[2][position - 7] = symbol
    board_print(board)
    winner = find_winner(board=board, player=symbol)
    if winner == symbol:
        return True


def find_winner(board, player):
    for x in range(3):
        if board[x][0] == player and board[x][1] == player and board[x][2] == player:
            return player
    for y in range(3):
        if board[0][y] == player and board[1][y] == player and board[2][y] == player:
            return player
    for z in range(0, 3, 2):
        if board[z][0] == player and board[1][1] == player and board[2][2-z] == player:
            return player



def tic_tac_toe():
    continue_game = True
    while continue_game:
        board = []
        for _ in range(3):
            col = ["  " for _ in range(3)]
            board.append(col)
        board_print(board)
        player_name_1 = input("\nEnter Player 1 name: ")
        player_name_2 = input("\nEnter Player 2 name: ")
        player1 = input(f"\n{player_name_1}: Which symbol you want? X or O ").upper()
        if player1 == "X":
            player2 = "O"
        else:
            player2 = "X"
        while True:
            position_player1 = int(input(f"\n{player_name_1}: Which position do you want to place your {player1}? "))
            continue_1 = place_player(board=board, position=position_player1, symbol=f" {player1} ")
            if continue_1:
                print(f"\nCongrats! {player_name_1} is the winner")
                break
            position_player2 = int(input(f"\n{player_name_2}: Which position do you want to place your {player2}? "))
            continue_2 = place_player(board=board, position=position_player2, symbol=f" {player2} ")
            if continue_2:
                print(f"\nCongrats! {player_name_2} is the winner")
                break
        user_input = input("Do you want to continue? Type Y or N ").upper()
        if user_input == "N":
            continue_game = False


if __name__ == "__main__":
    tic_tac_toe()
