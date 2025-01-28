from .point import Point
from tkinter import Canvas


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Canvas, fill="black"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x,
                           self.p2.y, fill=fill, width=2)
