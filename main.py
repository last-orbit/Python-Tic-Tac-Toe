from pyscript import when, document
import random

# Game Board
cell = document.getElementsByClassName("cell")
game_state = {
    "current_player": None,
    "game_started": False
}

# Players
player_status = document.getElementById("player-status")
player_1 = document.getElementById("player-1")
player_2 = document.getElementById("player-2")


players = {
    "X": "Player 1",
    "O": "Player 2"
    }
player_elements = {
    "X": player_1,
    "O": player_2
}

# Winning Combos
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


# Mouseover event to change cursor style
@when("mouseover", ".cell")
def handle_mouseover(event):
    if game_state["game_started"]:
        event.target.style.cursor = "pointer"


# Starts game and randomly selects a player to start
@when('click', "#start-button")
def start_game():
    game_state["game_started"] = True
    game_state["current_player"] = random.choice(list(players.keys()))
    if game_state["current_player"] == "X":
        player_1.style.borderBottom = "2px solid black"
        player_2.style.borderBottom = "none"
        player_status.textContent = "Player 1's turn"
    else:
        player_1.style.borderBottom = "none"
        player_2.style.borderBottom = "2px solid black"
        player_status.textContent = "Player 2's turn"
    print(game_state["current_player"])
    for c in cell:
        c.textContent = ""

def check_game_started():
    if game_state["game_started"] == False:
        print("Please start the game first!")
        return False
    return True

def check_cell(event):
    return event.target.textContent == ""


# Check Winner function
def check_winner(symbol):
    for combination in winning_combinations:
        if all(cell[position].textContent == symbol for position in combination):
            return True
    return False

# Check Tie function
def check_tie():
    if all(c.textContent != "" for c in cell):
        print("Game is a tie!")
        player_status.textContent = "Game is a tie!"
        game_state["game_started"] = False
        return True
    return False

# Handles clicks on the game board
@when("click", ".cell")
def handle_click(event):

    if not check_game_started():
        return

    symbol = game_state["current_player"]
    player_name = players[symbol]
    current_element = player_elements[symbol]


    if not check_cell(event):
        return

    current_element.style.borderBottom = "none"
    event.target.textContent = symbol

    if check_winner(symbol):
        print(f"Player {player_name} wins!")
        player_status.textContent = f"{player_name} wins!"
        return 

    if check_tie():
        return

    next_player = {"X": "O", "O": "X"}

    game_state["current_player"] = next_player[symbol]

    next_symbol = next_player[symbol]

    player_status.textContent = f"{players[next_symbol]}'s turn"
    player_elements[next_symbol].style.borderBottom = "2px solid black"
    player_elements[symbol].style.borderBottom = "none"


# Resets the game
@when("click", "#reset-button")
def handle_reset(event):
    game_state["current_player"] = None
    game_state["game_started"] = False
    player_elements["X"].style.borderBottom = "none"
    player_elements["O"].style.borderBottom = "none"
    player_status.textContent = ""
    for c in cell:
        c.textContent = ""