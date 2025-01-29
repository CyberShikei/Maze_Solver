from interface import Window, Maze

GRID_COLS = 40
GRID_ROWS = 40

CELL_SIZE = 15

CUSHION = 30
WINDOW_WIDTH = GRID_COLS * CELL_SIZE + 2 + CUSHION*2
WINDOW_HEIGHT = GRID_ROWS * CELL_SIZE + 2 + CUSHION*2


def main():
    window = Window(WINDOW_WIDTH, WINDOW_HEIGHT)

    maze = Maze(CUSHION, CUSHION, GRID_ROWS, GRID_COLS,
                CELL_SIZE, CELL_SIZE, window)

    maze.generate()
    maze.solve()

    window.wait_for_close()


if __name__ == "__main__":
    main()
