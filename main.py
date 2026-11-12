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
players = {"X": "Player 1", "O": "Player 2"}

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



@when("mouseover", ".cell")
def handle_mouseover(event):
    if game_state["game_started"]:
        event.target.style.cursor = "pointer"


# Starts game and randomly selects a player to start
@when('click', "#start-button")
def start_game():
    global current_player
    global game_started
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
    # current_player.borderBottom = "2px solid black"
    print(game_state["current_player"])
    for c in cell:
        c.textContent = ""

# start_game()

# Handles cell clicking 
@when("click", ".cell")
def handle_click(event):
    if game_state["game_started"] == False:
        event.preventDefault()
        print("Please start the game first!")
        return
    global current_player
    # event.target.textContent = current_player
    if game_state["current_player"] == "X":
        if event.target.textContent != "":
            print('please choose another box')
        else:
            player_1.style.borderBottom = "none"
            event.target.textContent = "X"
            check_winner("X")
            game_state["current_player"] = "O"
            player_status.textContent = "Player 2's turn"
            player_2.style.borderBottom = "2px solid black"

    else:
        # player_2.innerText = "Player 2's turn"
        if event.target.textContent != "":
            print('please choose another box')
        else:
            player_2.style.borderBottom = "none"
            event.target.textContent = "O"
            check_winner("O")
            game_state["current_player"] = "X"
            player_status.textContent = "Player 1's turn"
            player_1.style.borderBottom = "2px solid black"
            # print("Now it is Player 2's turn")

# Check Winner
def check_winner(symbol):
    for combination in winning_combinations:
        if all(cell[position].textContent == symbol for position in combination):
            return True
    return False


# Resets the game
@when("click", "#reset-button")
def handle_reset(event):
    global current_player
    game_state["current_player"] = None
    game_state["game_started"] = False
    player_1.style.borderBottom = "none"
    player_2.style.borderBottom = "none"
    for c in cell:
        c.textContent = ""

# output_div = document.getElementById("game-board")
# output_div.innerText = "Hey did this work?"

# @when('click',"button")
# def handle_click(event):
#     cell_index = event.target.getAttribute("data-cell-index")
#     "x" == cell_index.innerHTML
