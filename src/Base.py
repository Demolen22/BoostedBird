import arcade


class Base(arcade.Sprite):
    def __init__(self, image_path: str, x: int, scroll_speed: int):
        texture = arcade.load_texture(image_path)
        self.base_x = 0
        self.base_y = 0
        self.x = x
        self.scroll_speed = scroll_speed
        super().__init__(texture=texture)

    def update(self, dt: float):
        self.center_x = self.base_x
        self.base_x -= self.scroll_speed * dt
        if self.base_x < -self.x:
            self.base_x = 0
    def draw(self):
        self.center_x = self.base_x
        super().draw()
