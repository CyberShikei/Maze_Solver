from .window import Window
from .point import Point
from .line import Line

BG_COLOR = "#d9d9d9"
LINE_COLOR = "#000000"


class Cell:
    def __init__(self, x, y, window: Window, size_x=50, size_y=50):
        self.__x1 = x
        self.__y1 = y
        self.__x2 = x + size_x
        self.__y2 = y + size_y
        self.__window = window

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.visited = False

    def draw(self):
        top_left = Point(self.__x1, self.__y1)
        top_right = Point(self.__x2, self.__y1)
        bottom_left = Point(self.__x1, self.__y2)
        bottom_right = Point(self.__x2, self.__y2)

        left_wall = Line(top_left, bottom_left)
        right_wall = Line(top_right, bottom_right)
        top_wall = Line(top_left, top_right)
        bottom_wall = Line(bottom_left, bottom_right)

        if self.has_left_wall:
            self.__window.draw_line(left_wall, LINE_COLOR)
        else:
            self.__window.draw_line(left_wall, BG_COLOR)
        if self.has_right_wall:
            self.__window.draw_line(right_wall, LINE_COLOR)
        else:
            self.__window.draw_line(right_wall, BG_COLOR)
        if self.has_top_wall:
            self.__window.draw_line(top_wall, LINE_COLOR)
        else:
            self.__window.draw_line(top_wall, BG_COLOR)
        if self.has_bottom_wall:
            self.__window.draw_line(bottom_wall, LINE_COLOR)
        else:
            self.__window.draw_line(bottom_wall, BG_COLOR)

    def center_point(self):
        return Point((self.__x1 + self.__x2) // 2, (self.__y1 + self.__y2) // 2)

    def draw_move(self, to_cell, undo=False):
        line_color = "red"
        if undo:
            line_color = "blue"

        from_point = self.center_point()
        to_point = to_cell.center_point()

        line = Line(from_point, to_point)

        self.__window.draw_line(line, line_color)
