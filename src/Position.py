class Position:
    def __init__(self, init_x: float = 0.0, init_y: float = 0.0):
        self.x: float = init_x
        self.y: float = init_y

    def shift(self, value_x: float, value_y: float):
        self.x += value_x
        self.y += value_y
