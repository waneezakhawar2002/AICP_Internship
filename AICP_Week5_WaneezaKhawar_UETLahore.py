"""
Create a simple Tic Tac Toe game that can be played between two players.

"""

import os

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    print(f"{board[0]} | {board[1]} | {board[2]}\n---------")
    print(f"{board[3]} | {board[4]} | {board[5]}\n---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(0, 3):
        if board[i] == board[i + 3] == board[i + 6] != ' ':
            return board[i]  # Check Columns
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] != ' ':
            return board[i * 3]  # Check rows
    if board[0] == board[4] == board[8] != ' ' or board[2] == board[4] == board[6] != ' ':
        return board[4]  # Check diagonals
    return None

def is_board_full(board):
    return ' ' not in board

def is_valid_move(move, board):
    return 1 <= move <= 9 and board[move - 1] == ' '

def play_game():
    board = [' '] * 9
    current_player = 'X'

    while True:
        print_board(board)

        move = int(input(f"Player {current_player}, enter your move (1-9): "))

        if is_valid_move(move, board):
            board[move - 1] = current_player
            winner = check_winner(board)

            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

play_game()
