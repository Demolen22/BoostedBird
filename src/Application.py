import string

import arcade

from Agent import Agent
from Base import Base


class Application(arcade.Window):
    def __init__(self, width: int, height: int, title: string, scroll_speed: int = 40):
        super().__init__(width, height, title, resizable=True)
        self.agent = Agent()
        self.move_dict = {
            arcade.key.UP: self.agent.move_up,
            arcade.key.DOWN: self.agent.move_down
        }
        self.base = Base('../images/backgrounds/base_rescaled.png', self.width, scroll_speed)
        self.background = arcade.load_texture('../images/backgrounds/bg.png')
        self.base_x = 0
        self.score = 0
        self.scroll_speed = scroll_speed

    def run(self):
        arcade.run()

    def _draw_scene(self):
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)

    def on_draw(self):
        arcade.start_render()
        self._draw_scene()
        self.base.draw()
        self.agent.draw(self.width, self.height)

    def on_update(self, dt: float):
        self.base.update(dt)

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
