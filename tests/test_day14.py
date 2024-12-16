import pytest

from aoc2024.day14 import parse_robot, solution1


def test_parse_robot():
    line = "p=58,84 v=-55,-13"
    assert parse_robot(line) == (84, 58, -13, -55)


def test_solution1():
    lines = [
        "p=0,4 v=3,-3",
        "p=6,3 v=-1,-3",
        "p=10,3 v=-1,2",
        "p=2,0 v=2,-1",
        "p=0,0 v=1,3",
        "p=3,0 v=-2,-2",
        "p=7,6 v=-1,-3",
        "p=3,0 v=-1,-2",
        "p=9,3 v=2,3",
        "p=7,3 v=-1,2",
        "p=2,4 v=2,-3",
        "p=9,5 v=-3,-3",
    ]

    assert solution1(lines, 100, 11, 7) == 12


if __name__ == "__main__":
    pytest.main()
