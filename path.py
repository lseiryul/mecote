import numpy as np


def wrap_maze(maze, return_np_array=False):
    # 미로 형태를 받았을 때 외곽처리 등을 해주는 함수.
    x, y = len(maze[0]), len(maze)
    new_maze = np.ones([x + 2, y + 2])
    new_maze[1:(x+1), 1:(y+1)] = maze
    if return_np_array:
        pass  # TODO
    return new_maze.tolist()


def create_graph_matrix(n, e, v):
    """

    :param n: int number of vertices
    :param e: edge
    :param v: ... vertex name alias
    :return:
    """
    # 정점과 간선 정보를 받아 해당 그래프를 나타내는 행렬을 만드는 함수.
    pass

