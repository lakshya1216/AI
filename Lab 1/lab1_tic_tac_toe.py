import random

board = [" " for _ in range(9)]

def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(player):
    win_positions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a,b,c in win_positions:
        if board[a] == player and board[b] == player and board[c] == player:
            return True
    return False

def computer_move():
    empty_positions = [i for i in range(9) if board[i] == " "]
    choice = random.choice(empty_positions)
    board[choice] = "O"

def play_game():
    moves_done = 0
    
    while True:
        print_board()
       
        user_pos = int(input("Player X, enter a position (1-9): ")) - 1

        if board[user_pos] != " ":
            print("That spot is already taken. Try again.")
            continue

        board[user_pos] = "X"
        moves_done += 1

        if check_winner("X"):
            print_board()
            print("Player X wins!")
            break

        if moves_done == 9:
            print_board()
            print("It's a tie!")
            break

        computer_move()
        moves_done += 1

        if check_winner("O"):
            print_board()
            print("Computer (O) wins!")
            break

        if moves_done == 9:
            print_board()
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()
