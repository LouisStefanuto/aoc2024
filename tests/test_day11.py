import pytest

from aoc2024.day11 import blink_n_times, blink_one_time


def test_blink_one_time_case1():
    assert blink_one_time([125, 17]) == [253000, 1, 7]


def test_blink_one_time_case2():
    assert blink_one_time([253000, 1, 7]) == [253, 0, 2024, 14168]


def test_blink_one_time_case3():
    assert blink_one_time([253, 0, 2024, 14168]) == [512072, 1, 20, 24, 28676032]


def test_solution():
    data = [125, 17]
    expected = [
        2097446912,
        14168,
        4048,
        2,
        0,
        2,
        4,
        40,
        48,
        2024,
        40,
        48,
        80,
        96,
        2,
        8,
        6,
        7,
        6,
        0,
        3,
        2,
    ]
    assert blink_n_times(data, 6) == expected


if __name__ == "__main__":
    pytest.main()
