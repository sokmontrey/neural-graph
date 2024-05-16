import pyray as pr 

class Point:
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col

    def render(self, renderer, color = pr.BLACK):
        renderer.draw(self.row, self.col, color)

    def getPos(self): return pr.Vector2(self.row, self.col)
