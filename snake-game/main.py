from game import Game
import pyray as pr

WIDTH = 500
HEIGHT = 500
GRID_SIZE = 25

game = Game(WIDTH, HEIGHT, GRID_SIZE)

pr.init_window(WIDTH, HEIGHT, "snake game")
while not pr.window_should_close():
    game.render()
    game.checkInput()
    game.update(0.2)

pr.close_window()
