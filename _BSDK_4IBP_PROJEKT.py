def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_winner(board):
    #wiersze
    for k in range(0, 9, 3):
        if board[k] == board[k+1] == board[k+2] != " ":
            return board[k]
    #kolumny
    for k in range(3):
        if board[k] == board[k+3] == board[k+6] != " ":
            return board[k]
    #przekątne
        if board[0] == board[4] == board[8] != " ":
            return board[0]
        if board[2] == board[4] == board[6] != " ":
            return board[2]
    #Remis
        return None    

def play_game():
    board = [" "]*9
    player = "X"
    while True:
        print_board(board)
        move = input(f"Ruch gracza {player}: ")
        move = int(move) - 1
        if board[move] == " ":
            board[move] = player
        else:
            print("Nieprawidłowy ruch. Spróbuj ponownie.")
            continue
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Gracz {winner} wygrał!")
            break
        if " " not in board:
            print_board(board)
            print("Remis!")
            break
        player = "O" if player == "X" else "X"
play_game()
