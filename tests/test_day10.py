import numpy as np
import pytest

from aoc2024.day10 import MountainWorld


class TestSolution1:
    def test_case1(self):
        data = np.array(
            [
                [-1, -1, -1, 0, -1, -1, -1],
                [-1, -1, -1, 1, -1, -1, -1],
                [-1, -1, -1, 2, -1, -1, -1],
                [6, 5, 4, 3, 4, 5, 6],
                [7, -1, -1, -1, -1, -1, 7],
                [8, -1, -1, -1, -1, -1, 8],
                [9, -1, -1, -1, -1, -1, 9],
            ]
        )
        world = MountainWorld(data)
        assert world.solve() == 2

    def test_solution_case2(self):
        data = np.array(
            [
                [-1, -1, 9, 0, -1, -1, 9],
                [-1, -1, -1, 1, -1, 9, 8],
                [-1, -1, -1, 2, -1, -1, 7],
                [6, 5, 4, 3, 4, 5, 6],
                [7, 6, 5, -1, 9, 8, 7],
                [8, 7, 6, -1, -1, -1, -1],
                [9, 8, 7, -1, -1, -1, -1],
            ],
        )
        world = MountainWorld(data)
        assert world.solve() == 4


if __name__ == "__main__":
    pytest.main()
