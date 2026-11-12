board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

players = {"X": "Player 1", "O": "Player 2"}

winning_combinations = (
    (0, 1, 2),  # Top row
    (3, 4, 5),  # Middle row
    (6, 7, 8),  # Bottom row
    (0, 3, 6),  # Left column
    (1, 4, 7),  # Middle column
    (2, 5, 8),  # Right column
    (0, 4, 8),  # Diagonal from top-left to bottom-right
    (2, 4, 6),  # Diagonal from top-right to bottom-left
)

occupied = set()

def display_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(symbol):
    for combination in winning_combinations:
        if all(board[position] == symbol for position in combination):
            return True
    return False

def make_move(symbol):
    while True:
        choice = input(f"{players[symbol]} ({symbol}), enter a position (1-9): ")
        if not choice.isdigit():
            print("Please enter a valid number.")
        position = int(choice) -1

        if position < 0 or position > 8:
            print("Invalid position. Please choose a number between 1 and 9.")
            continue
        if position in occupied:
            print("That position is already occupied. Please choose another position.")
            continue
        board[position] = symbol
        occupied.add(position)
        break

print("Welcome to Tic-Tac-Toe!")

current_player = "X"

while True:
    display_board()

    make_move(current_player)

    if check_winner(current_player):
        display_board()
        print(f"{players[current_player]} ({current_player}) wins!")
        break

    if len(occupied) == 9:
        display_board()
        print("The game is a tie!")
        break

    current_player = "O" if current_player == "X" else "X"

print('\n Thanks for playing ')