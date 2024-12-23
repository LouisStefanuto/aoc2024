import numpy as np
import pytest

from aoc2024.day16 import Maze


@pytest.fixture
def grid():
    grid = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", ".", "E", "#"],
        ["#", ".", "#", ".", "#", "#", "#", ".", "#", ".", "#", "#", "#", ".", "#"],
        ["#", ".", ".", ".", ".", ".", "#", ".", "#", ".", ".", ".", "#", ".", "#"],
        ["#", ".", "#", "#", "#", ".", "#", "#", "#", "#", "#", ".", "#", ".", "#"],
        ["#", ".", "#", ".", "#", ".", ".", ".", ".", ".", ".", ".", "#", ".", "#"],
        ["#", ".", "#", ".", "#", "#", "#", "#", "#", ".", "#", "#", "#", ".", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", "#"],
        ["#", "#", "#", ".", "#", ".", "#", "#", "#", "#", "#", ".", "#", ".", "#"],
        ["#", ".", ".", ".", "#", ".", ".", ".", ".", ".", "#", ".", "#", ".", "#"],
        ["#", ".", "#", ".", "#", ".", "#", "#", "#", ".", "#", ".", "#", ".", "#"],
        ["#", ".", ".", ".", ".", ".", "#", ".", ".", ".", "#", ".", "#", ".", "#"],
        ["#", ".", "#", "#", "#", ".", "#", ".", "#", ".", "#", ".", "#", ".", "#"],
        ["#", "S", ".", ".", "#", ".", ".", ".", ".", ".", "#", ".", ".", ".", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ]
    return np.array(grid)


@pytest.fixture
def maze(grid) -> Maze:
    return Maze(grid)


class TestTerrain:
    def test_update_case1(self, maze: Maze, grid: np.ndarray):
        assert np.array_equal(maze.grid, grid)

    def test_solve(self, maze: Maze):
        assert maze.solve() == 7036


if __name__ == "__main__":
    pytest.main()
