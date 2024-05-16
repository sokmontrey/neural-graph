import pyray as pr

class Renderer:
    def __init__(self, grid_size):
        self.grid_size = grid_size

    def draw(self, row, col, color = pr.BLACK):
        pr.draw_rectangle_v(
                pr.vector2_scale(pr.Vector2(col, row), self.grid_size), 
                pr.Vector2(self.grid_size, self.grid_size),
                color)

