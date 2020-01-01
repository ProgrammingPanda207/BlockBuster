from tkinter import Tk
from tkinter import Canvas
from tkinter import mainloop
from game import Game

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

window = Tk()

canvas = Canvas(window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
canvas.pack()

game = Game(canvas, SCREEN_WIDTH, SCREEN_HEIGHT)
game.update()

mainloop()
