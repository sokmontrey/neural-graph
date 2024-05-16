from point import Point
from snake import Snake
from renderer import Renderer
import pyray as pr
import random

class Game:
    def __init__(self, width, height, grid_size):
        self.food = Point(0, 0)
        self.width = width
        self.height = height
        self.rows = height // grid_size
        self.cols = width // grid_size
        self.grid_size = grid_size

        self.renderer = Renderer(grid_size)
        self.snake = Snake(5, 5)
        self.spawn_food()

    def spawn_food(self):
        self.food.row = random.randint(0, self.rows - 1)
        self.food.col = random.randint(0, self.cols - 1)

    def update(self, delay = 0.1):
        self.snake.move()
        if self.snake.checkBodyCollision(self.snake.getHead()):
            # TODO: game over
            pr.close_window()
        if self.snake.checkHeadCollision(self.food):
            self.snake.grow()
            self.spawn_food()
        pr.wait_time(delay)

    def checkInput(self):
        key = pr.get_key_pressed()
        if key == pr.KeyboardKey.KEY_RIGHT:
            self.snake.turn(Snake.RIGHT)
        elif key == pr.KeyboardKey.KEY_LEFT:
            self.snake.turn(Snake.LEFT)
        elif key == pr.KeyboardKey.KEY_UP:
            self.snake.turn(Snake.UP)
        elif key == pr.KeyboardKey.KEY_DOWN:
            self.snake.turn(Snake.DOWN)

    def render(self):
        pr.begin_drawing()
        pr.clear_background(pr.WHITE)
        self.snake.render(self.renderer)
        self.food.render(self.renderer, pr.RED)
        pr.end_drawing()



