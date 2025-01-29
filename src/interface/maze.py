from .cell import Cell
from .window import Window

import random
import time


class Maze:
    def __init__(self,
                 x1,
                 y1,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 win=None,
                 seed=None
                 ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y

        if win is None:
            self.__win = self.__create_default_window()
        else:
            self.__win = win
            self.__set_window_size()

        if seed is not None:
            random.seed(seed)

        # self.__seed = seed

        self.__cells = []
        self.__create_cells()
        # self.__draw_cells()

    def generate(self):
        self.__break_walls_r(0, 0)
        self.__break_entance_and_exit()
        self.__reset_visited()
        self.__draw_cells()

    def solve(self):
        self.__solve_r(0, 0)

    def __solve_r(self, i=0, j=0):
        self.__animate()
        if self.__is_end(i, j):
            return True
        # print("OK")
        if i < 0 or i >= self.__num_rows or j < 0 or j >= self.__num_cols:
            return False

        if self.__cells[i][j].visited:
            return False

        self.__cells[i][j].visited = True
        walls = self.__ceck_walls(i, j)
        for u in range(len(walls)):
            wall = random.choice(walls)
            walls.remove(wall)
            self.__cells[i][j].draw_move(self.__cells[wall[0]][wall[1]])
            if self.__solve_r(wall[0], wall[1]):
                self.__cells[i][j].draw_move(self.__cells[wall[0]][wall[1]])
                return True
            else:
                self.__cells[i][j].draw_move(
                    self.__cells[wall[0]][wall[1]], True)

        return False

    def __ceck_walls(self, i, j):
        curr_cell = self.__cells[i][j]

        directions = []
        if not curr_cell.has_top_wall:
            if not self.__cells[i-1][j].visited:
                directions.append((i-1, j))
        if not curr_cell.has_bottom_wall:
            if not self.__cells[i+1][j].visited:
                directions.append((i+1, j))
        if not curr_cell.has_left_wall:
            if not self.__cells[i][j-1].visited:
                directions.append((i, j-1))
        if not curr_cell.has_right_wall:
            if not self.__cells[i][j+1].visited:
                directions.append((i, j+1))

        return directions

    def __is_end(self, i, j):
        return (i == self.__num_rows - 1
                and j == self.__num_cols - 1)

    def __break_walls_r(self, i, j):
        if i < 0 or i >= self.__num_rows or j < 0 or j >= self.__num_cols:
            return

        if self.__cells[i][j].visited:
            return

        self.__cells[i][j].visited = True
        while True:
            possible_directions = self.__check_adjacent_cells(i, j)
            if possible_directions == []:
                return
            next_cell = random.choice(possible_directions)

            self.__break_walls(i, j, next_cell[0], next_cell[1])
            self.__break_walls_r(next_cell[0], next_cell[1])

    def __reset_visited(self):
        for line in self.__cells:
            for cell in line:
                cell.visited = False

    def __break_walls(self, i_1, j_1, i_2, j_2):
        if i_1 == i_2:
            if j_1 < j_2:
                self.__cells[i_1][j_1].has_right_wall = False
                self.__cells[i_2][j_2].has_left_wall = False
            else:
                self.__cells[i_1][j_1].has_left_wall = False
                self.__cells[i_2][j_2].has_right_wall = False
        else:
            if i_1 < i_2:
                self.__cells[i_1][j_1].has_bottom_wall = False
                self.__cells[i_2][j_2].has_top_wall = False
            else:
                self.__cells[i_1][j_1].has_top_wall = False
                self.__cells[i_2][j_2].has_bottom_wall = False

    def __ensure_valid_direction(self, i, j):
        if ((i < 0 or i >= self.__num_rows or j < 0 or j >= self.__num_cols)
                or self.__cells[i][j].visited):
            return False
        return True

    def __check_adjacent_cells(self, i, j):
        if i < 0 or i >= self.__num_rows or j < 0 or j >= self.__num_cols:
            return

        cells_to_visit = []
        directions = [
            (i+1, j),
            (i-1, j),
            (i, j+1),
            (i, j-1)
        ]
        direction = directions[0]
        if self.__ensure_valid_direction(direction[0], direction[1]):
            cells_to_visit.append(direction)
        direction = directions[1]
        if self.__ensure_valid_direction(direction[0], direction[1]):
            cells_to_visit.append(direction)
        direction = directions[2]
        if self.__ensure_valid_direction(direction[0], direction[1]):
            cells_to_visit.append(direction)
        direction = directions[3]
        if self.__ensure_valid_direction(direction[0], direction[1]):
            cells_to_visit.append(direction)

        return cells_to_visit

    def __break_entance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__cells[self.__num_rows -
                     1][self.__num_cols - 1].has_bottom_wall = False
        self.__draw_cells()

    def __set_window_size(self):
        grid_size_x, grid_size_y = self.__get_window_size()
        self.__win.set_size(grid_size_x, grid_size_y)

    def __create_default_window(self):
        grid_size_x = self.__num_cols * self.__cell_size_x
        grid_size_y = self.__num_rows * self.__cell_size_y
        win = Window(grid_size_x + self.__x1*2,
                     grid_size_y + self.__y1*2)

        return win

    def __get_window_size(self):
        grid_size_x = (self.__num_cols * self.__cell_size_x) + (self.__x1 * 2)
        grid_size_y = (self.__num_rows * self.__cell_size_y) + (self.__y1 * 2)

        return grid_size_x, grid_size_y

    def __draw_cells(self):
        for line in self.__cells:
            for cell in line:
                cell.draw()

    def __animate(self):
        self.__win.redraw()
        time.sleep(0.002)

    def __create_cells(self):
        for i in range(self.__num_rows):
            second_dim = []
            for j in range(self.__num_cols):
                cell = Cell(self.__x1 + j * self.__cell_size_x,
                            self.__y1 + i * self.__cell_size_y,
                            self.__win,
                            self.__cell_size_x,
                            self.__cell_size_y
                            )
                second_dim.append(cell)
            self.__cells.append(second_dim)

    def win(self):
        return self.__win
