from pyscript import when, document
import random

# Game Board
cell = document.getElementsByClassName("cell")

# Players
player_status = document.getElementById("player-status")
player_1 = document.getElementById("player-1")
player_2 = document.getElementById("player-2")
# players = {"X": "Player 1", "O": "Player 2"}


@when("mouseover", ".cell")
def handle_mouseover(event):
    event.target.style.cursor = "pointer"


current_player = "X"
player_1.style.borderBottom = "2px solid black"



@when("click", ".cell")
def handle_click(event):
    global current_player
    # event.target.textContent = current_player
    if current_player == "X":
        if event.target.textContent != "":
            print('please choose another box')
        else:
            player_1.style.borderBottom = "none"
            event.target.textContent = "X"
            current_player = "O"
            player_2.style.borderBottom = "2px solid black"

    else:
        # player_2.innerText = "Player 2's turn"
        if event.target.textContent != "":
            print('please choose another box')
        else:
            player_2.style.borderBottom = "none"
            event.target.textContent = "O"
            current_player = "X"
            player_1.style.borderBottom = "2px solid black"
            # print("Now it is Player 2's turn")



@when("click", "#reset-button")
def handle_reset(event):
    global current_player
    current_player = "X"
    player_1.style.borderBottom = "2px solid black"
    player_2.style.borderBottom = "none"
    for c in cell:
        c.textContent = ""

# output_div = document.getElementById("game-board")
# output_div.innerText = "Hey did this work?"

# @when('click',"button")
# def handle_click(event):
#     cell_index = event.target.getAttribute("data-cell-index")
#     "x" == cell_index.innerHTML
