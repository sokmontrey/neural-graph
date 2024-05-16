import pyray as pr
from point import Point
from renderer import Renderer

class Snake:
    RIGHT = pr.Vector2(1,0)
    LEFT = pr.Vector2(-1,0)
    UP = pr.Vector2(0,-1)
    DOWN = pr.Vector2(0,1)

    def __init__(self, row, col) -> None:
        self.body = [Point(row, col)]
        self.dir = Snake.RIGHT

    def move(self):
        head = self.body[0]
        new_head = Point(head.row + self.dir.y, head.col + self.dir.x)
        self.body.insert(0, new_head)
        self.body.pop()

    def checkBodyCollision(self, point):
        for body_part in self.body[1:]:
            if body_part.row == point.row and body_part.col == point.col:
                return True
        return False

    def checkHeadCollision(self, point):
        head = self.getHead()
        if head.row == point.row and head.col == point.col:
            return True
        return False

    def getHead(self):
        return self.body[0]

    def turn(self, dir):
        if self.dir.x + dir.x == 0 and self.dir.y + dir.y == 0:
            return
        self.dir = dir

    def grow(self):
        tail = self.body[-1]
        new_tail = Point(tail.row, tail.col)
        self.body.append(new_tail)

    def render(self, renderer): 
        for point in self.body:
            point.render(renderer)

