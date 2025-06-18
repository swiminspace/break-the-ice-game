from game2dboard import Board
from tkinter import messagebox
import random
import time

# Global consts
FIELD_WIDTH = 7
FIELD_HEIGHT = 7
BLOCK_SIZE = 100
MARGIN_SIZE = 15
MSG = "ESC: Close    F2: Restart"


def mouse_click(btn, row, col):
    selected = game[row][col]
    if selected is "penguin_resized.png":
        # Show game over thing
        print("game over")
        time.sleep(5)
        newgame()
    game[row][col] = "titanic_resized.png"
    if "iceberg_resized.png" not in game[row]:
        # Show game over thing
        print("game over")
        time.sleep(5)
        newgame()
    if "iceberg_resized.png" not in game[:][col]:
        # Show game over thing
        print("game over")
        time.sleep(5)
        newgame()


def kb_click(key):
    if key == "Escape":
        game.close()
    elif key == "F2":
        newgame()


def newgame():
    for i in range(FIELD_WIDTH):
        for j in range(FIELD_HEIGHT):
            if i == 0 and j == 0:
                game[i][j] = "penguin_resized.png"
            else:
                game[i][j] = "iceberg_resized.png"
    game.shuffle()
    game.print(MSG)


game = Board(FIELD_HEIGHT, FIELD_WIDTH)
game.cell_size = BLOCK_SIZE
game.title = "Break the Ice Game"
game.margin = MARGIN_SIZE
game.grid_color = "MediumTurquoise"
game.margin_color = "MediumTurquoise"
game.cell_color = "LightCyan"
game.on_key_press = kb_click
game.on_mouse_click = mouse_click
game.on_start = newgame
game.show()
