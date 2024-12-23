import numpy as np
import pytest

from aoc2024.day18 import Maze, build_matrix, solve


def test_build_matrix():
    data = [(0, 0), (1, 1), (1, 2)]
    expected = np.array(
        [
            ["#", ".", "."],
            [".", "#", "#"],
            [".", ".", "."],
        ]
    )
    assert np.array_equal(build_matrix(3, data), expected)


def test_solve1_case1():
    grid = np.array(
        [
            [".", "#", "."],
            [".", "#", "#"],
            [".", ".", "."],
        ]
    )
    maze = Maze(grid)
    assert maze.bfs() == 4


def test_solve1_case2():
    grid = np.array(
        [
            [".", ".", ".", "#", ".", ".", "."],
            [".", ".", "#", ".", ".", "#", "."],
            [".", ".", ".", ".", "#", ".", "."],
            [".", ".", ".", "#", ".", ".", "#"],
            [".", ".", "#", ".", ".", "#", "."],
            [".", "#", ".", ".", "#", ".", "."],
            ["#", ".", "#", ".", ".", ".", "."],
        ]
    )
    maze = Maze(grid)
    assert maze.bfs() == 22


def test_solve():
    data = [
        (5, 4),
        (4, 2),
        (4, 5),
        (3, 0),
        (2, 1),
        (6, 3),
        (2, 4),
        (1, 5),
        (0, 6),
        (3, 3),
        (2, 6),
        (5, 1),
        (1, 2),
        (5, 5),
        (2, 5),
        (6, 5),
        (1, 4),
        (0, 4),
        (6, 4),
        (1, 1),
        (6, 1),
        (1, 0),
        (0, 5),
        (1, 6),
        (2, 0),
    ]
    assert solve(data, 7) == (6, 1)


if __name__ == "__main__":
    pytest.main()
