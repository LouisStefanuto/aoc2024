import numpy as np
import pytest

from aoc2024.day18 import Maze, build_matrix


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


if __name__ == "__main__":
    pytest.main()
