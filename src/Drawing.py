import arcade


def draw_rectangle(x1, y1, x2, y2, color=arcade.color.SPANISH_VIOLET):
    point_list = (
        (x1, y1),
        (x1, y2),
        (x2, y2),
        (x2, y1)
    )
    arcade.draw_polygon_filled(point_list, color)
