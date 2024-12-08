import numpy as np
import pytest

from aoc2024.day6 import Guard, GuardDirection, Terrain


def test_guard():
    guard = Guard(0, 2, GuardDirection.UP)
    assert guard.x == 0
    assert guard.y == 2
    assert guard.direction == "^"


def test_find_guard_1():
    grid = np.array(
        [
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ">", ".", ".", ".", "#", ".", ".", "."],
            [".", ".", ".", "#", ".", "#", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "#", ".", ".", ".", ".", "#", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "#", ".", ".", ".", "#", "#", "."],
        ]
    )
    terrain = Terrain(grid)
    assert terrain.find_guard() == Guard(1, 2, GuardDirection.RIGHT)


def test_find_guard_2():
    grid = np.array(
        [
            [".", ".", ".", "v", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "#", ".", ".", "."],
            [".", ".", ".", "#", ".", "#", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "#", ".", ".", ".", ".", "#", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "#", ".", ".", ".", "#", "#", "."],
        ]
    )
    terrain = Terrain(grid)
    assert terrain.find_guard() == Guard(0, 3, GuardDirection.DOWN)


def test_is_position_out():
    terrain = Terrain(
        np.array(
            [
                ["v", "."],
                [".", "."],
            ]
        )
    )
    assert terrain.is_position_out(3, 3) is True
    assert terrain.is_position_out(0, 0) is False


def test_get_next_move():
    terrain = Terrain(
        np.array(
            [
                [".", ".", ".", "."],
                [".", ".", ".", "."],
                [".", ">", ".", "#"],
                [".", ".", ".", "."],
            ]
        )
    )
    assert terrain.get_next_move() == (Guard(2, 2, GuardDirection.RIGHT), False)


def test_move_guard():
    terrain = Terrain(
        np.array(
            [
                [".", ".", ".", "."],
                [".", ".", ".", "."],
                [".", ">", ".", "#"],
                [".", ".", ".", "."],
            ]
        )
    )

    terminal = terrain.move_guard()
    assert terminal is False
    assert terrain.guard == Guard(2, 2, GuardDirection.RIGHT)

    terminal = terrain.move_guard()
    assert terminal is False
    assert terrain.guard == Guard(3, 2, GuardDirection.DOWN)

    terminal = terrain.move_guard()
    assert terminal is True


def test_solution1():
    terrain = Terrain(
        np.array(
            [
                [".", ".", ".", "."],
                [".", ".", ".", "."],
                [".", ">", ".", "#"],
                [".", ".", ".", "."],
            ]
        )
    )
    result = terrain.solution1()
    assert result == 3


if __name__ == "__main__":
    pytest.main()
