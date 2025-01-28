from tkinter import Tk, BOTH, Canvas
from .line import Line


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.geometry(f"{width}x{height}")
        self.__root.title("Maze Solver")
        self.__root.resizable(False, False)
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.__is_running = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()

    def close(self):
        self.__is_running = False

    def draw_line(self, line: Line, fill="black"):
        line.draw(self.__canvas, fill)

    def set_size(self, width, height):
        self.__root.geometry(f"{width}x{height}")
        self.__canvas.config(width=width, height=height)
        self.redraw()
