import arcade
from Agent import Agent
from Drawing import draw_rectangle
from Position import Position


def _draw_scene(width: float, height: float):
    draw_rectangle(0, 0, width, height, color=arcade.color.AERO_BLUE)
    draw_rectangle(0, 0, width, int(height * 0.1), color=arcade.color.GO_GREEN)


class Application(arcade.Window):

    def __init__(self):
        super().__init__(1920, 1080, resizable=True)
        self.agent = Agent()
        self.move_dict = {arcade.key.LEFT: self.agent.move_left,
                          arcade.key.RIGHT: self.agent.move_right,
                          arcade.key.UP: self.agent.move_up,
                          arcade.key.DOWN: self.agent.move_down}

    def run(self):
        arcade.run()

    def on_draw(self):
        self.clear()
        _draw_scene(self.width, self.height)
        self.agent.draw(self.width, self.height)

    def on_update(self, dt: float):
        pass

    def on_mouse_drag(self, x: float, y: float, dx: float, dy: float, buttons: int, modifiers: int):
        pass

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        pass

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        pass

    def on_resize(self, width: float, height: float):
        pass

    def on_key_press(self, symbol: int, modifiers: int):
        action = self.move_dict.get(symbol)
        if action is not None:
            action()











