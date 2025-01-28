import unittest

from src.interface.maze import Maze


class TestMaze(unittest.TestCase):
    def test_maze(self):
        maze = Maze(10, 10, 10, 10, 50, 50)
        self.assertEqual(maze._Maze__x1, 10)
        self.assertEqual(maze._Maze__y1, 10)
        self.assertEqual(maze._Maze__num_rows, 10)
        self.assertEqual(maze._Maze__num_cols, 10)
        self.assertEqual(maze._Maze__cell_size_x, 50)
        self.assertEqual(maze._Maze__cell_size_y, 50)
        self.assertEqual(len(maze._Maze__cells), 10)
        self.assertEqual(len(maze._Maze__cells[0]), 10)

    def test_break_entrance_and_exit(self):
        maze = Maze(10, 10, 10, 10, 50, 50)
        maze._Maze__break_entance_and_exit()
        self.assertFalse(maze._Maze__cells[0][0].has_top_wall)
        self.assertFalse(maze._Maze__cells[9][9].has_bottom_wall)

    def test_generate(self):
        maze = Maze(10, 10, 10, 10, 50, 50)
        maze.generate()
        self.assertFalse(maze._Maze__cells[0][0].visited)


if __name__ == '__main__':
    unittest.main()
