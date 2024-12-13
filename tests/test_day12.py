import numpy as np
import pytest

from aoc2024.day12 import CropWorld, compute_price


def test_solve_case0():
    world = CropWorld(
        np.array(
            [
                ["A", "A"],
                ["A", "A"],
            ]
        )
    )
    assert world.solve() == 32


def test_solve_case1():
    world = CropWorld(
        np.array(
            [
                ["A", "A", "A", "A"],
                ["B", "B", "C", "D"],
                ["B", "B", "C", "C"],
                ["E", "E", "E", "C"],
            ]
        )
    )
    assert world.solve() == 140


def test_solve_case2():
    world = CropWorld(
        np.array(
            [
                ["O", "O", "O", "O", "O"],
                ["O", "X", "O", "X", "O"],
                ["O", "O", "O", "O", "O"],
                ["O", "X", "O", "X", "O"],
                ["O", "O", "O", "O", "O"],
            ]
        )
    )
    assert world.solve() == 772


def test_compute_price():
    parcels = [(1, 3), (1, 3), (1, 3), (1, 3)]
    assert compute_price(parcels) == 12


if __name__ == "__main__":
    pytest.main()
