from unittest import TestCase
import unittest
from path import create_graph_matrix, wrap_maze


class Test(TestCase):

    def test_wrap_maze(self):

        maze1 = [
            [0, 1, 1],
            [0, 0, 0],
            [1, 0, 0]
        ]
        maze1_res = [
            [1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 0, 0, 1],
            [1, 1, 1, 1, 1]
        ]
        self.assertEqual(wrap_maze(maze1), maze1_res)

    def test_create_graph_matrix(self):
        # self.fail()
        pass


if __name__ == '__main__':
    unittest.main()
