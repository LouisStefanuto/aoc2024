import numpy as np
import pytest

from aoc2024.day13 import (
    Button,
    Machine,
    Prize,
    build_machines,
    solution1,
)


def test_build_machines():
    lines = [
        "Button A: X+1, Y+1",
        "Button B: X+2, Y+2",
        "Prize: X=3, Y=3",
        "",
        "Button A: X+4, Y+4",
        "Button B: X+5, Y+5",
        "Prize: X=6, Y=6",
    ]

    machines = build_machines(lines)

    expected = [
        Machine(
            Button(1, 1, 3),
            Button(2, 2, 1),
            Prize(3, 3),
        ),
        Machine(
            Button(4, 4, 3),
            Button(5, 5, 1),
            Prize(6, 6),
        ),
    ]

    assert len(machines) == len(expected)

    assert np.array_equal(machines[0].M, np.array([[1, 2], [1, 2]]))
    assert np.array_equal(machines[0].y, np.array([3, 3]))

    assert np.array_equal(machines[1].M, np.array([[4, 5], [4, 5]]))
    assert np.array_equal(machines[1].y, np.array([6, 6]))


def test_compute_cost():
    machine = Machine(Button(1, 1, 3), Button(2, 2, 1), Prize(3, 3))
    assert machine.compute_cost([1.0, 1.0]) == 4
    assert machine.compute_cost([1.0, 4.0]) == 0

    machine = Machine(Button(10, 10, 3), Button(3, 3, 1), Prize(10, 10))
    assert machine.compute_cost([1.0, 0.0]) == 3
    assert machine.compute_cost([1.0, 4.0]) == 0
    assert machine.compute_cost([101.0, 0.0]) == 0


def test_solution1():
    machines = [
        Machine(
            Button(3, 3, 3),
            Button(1, 2, 1),
            Prize(4, 5),
        ),
        Machine(
            Button(4, 4, 3),
            Button(5, 8, 1),
            Prize(6, 6),
        ),
    ]
    assert solution1(machines) == 4


if __name__ == "__main__":
    pytest.main()
