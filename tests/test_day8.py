import numpy as np
import pytest

from aoc2024.day8 import (
    Antenna,
    AntennaMap,
    compute_all_antinodes,
    compute_antinodes,
    solution1,
)


@pytest.fixture
def antenna_grid() -> AntennaMap:
    grid = np.full((5, 5), ".")
    return AntennaMap(grid)


def test_map_init(antenna_grid):
    grid = np.full((5, 5), ".")
    assert np.array_equal(antenna_grid.grid, grid)


def test_antenna_init():
    antenna = Antenna(2, 3, "A")
    assert antenna.x == 2
    assert antenna.y == 3
    assert antenna.value == "A"


def test_map_list_antennas():
    grid = np.array(
        [
            [".", ".", ".", "."],
            [".", "a", ".", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."],
        ]
    )
    antenna_grid = AntennaMap(grid)
    assert antenna_grid.list_antennas() == [Antenna(1, 1, "a")]


def test_compute_antinodes():
    antenna1 = Antenna(1, 1, "a")
    antenna2 = Antenna(2, 2, "a")
    assert compute_antinodes(antenna1, antenna2) == [(0, 0), (3, 3)]

    antenna1 = Antenna(1, 1, "a")
    antenna2 = Antenna(2, 2, "b")
    assert compute_antinodes(antenna1, antenna2) == []


def test_compute_all_antinodes():
    antenna1 = Antenna(1, 1, "a")
    antenna2 = Antenna(2, 2, "a")
    antenna3 = Antenna(1, 2, "a")
    antennas = [antenna1, antenna2, antenna3]

    result = compute_all_antinodes(antennas)
    expected = [(0, 0), (3, 3), (1, 0), (1, 3), (3, 2), (0, 2)]
    assert set(result) == set(expected)


def test_solution1_case1():
    grid = np.array(
        [
            [".", ".", "."],
            [".", "a", "a"],
            [".", ".", "a"],
        ]
    )
    antenna_grid = AntennaMap(grid)
    result = solution1(antenna_grid)
    expected = [(0, 0), (1, 0), (0, 2)]
    assert set(result) == set(expected)


def test_solution1_case2():
    grid = np.array(
        [
            [".", ".", "."],
            [".", "a", "a"],
            [".", ".", "b"],
        ]
    )
    antenna_grid = AntennaMap(grid)
    result = solution1(antenna_grid)
    expected = [(1, 0)]
    assert set(result) == set(expected)


if __name__ == "__main__":
    pytest.main()
