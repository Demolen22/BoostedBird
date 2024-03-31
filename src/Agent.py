from Position import Position
from Drawing import draw_rectangle
import arcade


class Agent:

    def __init__(self):
        self.position = Position()
        self._size_a = 0.1
        self._size_b = 0.1
        self._body = lambda x, y, width, height: draw_rectangle(
            x - self._size_a * width / 2,
            y - self._size_b * height / 2,
            x + self._size_a * width / 2,
            y + self._size_b * height / 2,
            arcade.color.BLUEBERRY
        )

    def draw(self, width, height):
        self._draw_body(width, height)

    def move(self, position: Position):
        self.position = position

    def move_down(self):
        self.position.shift(0., -100.)

    def move_up(self):
        self.position.shift(0., 100.)

    def _draw_body(self, width, height):
        self._body(self.position.x, self.position.y, width, height)
