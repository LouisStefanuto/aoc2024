import numpy as np
import pytest

from aoc2024.day8 import Antenna, AntennaMap, Solution1, Solution2


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


class TestSolution1:
    def test_compute_antinodes(self):
        solution = Solution1()
        antenna1 = Antenna(1, 1, "a")
        antenna2 = Antenna(2, 2, "a")
        expected = [(0, 0), (3, 3)]
        assert solution.compute_antinodes(antenna1, antenna2) == expected

        antenna1 = Antenna(1, 1, "a")
        antenna2 = Antenna(2, 2, "b")
        assert solution.compute_antinodes(antenna1, antenna2) == []

    def test_compute_all_antinodes(self):
        antenna1 = Antenna(1, 1, "a")
        antenna2 = Antenna(2, 2, "a")
        antenna3 = Antenna(1, 2, "a")
        antennas = [antenna1, antenna2, antenna3]

        solution = Solution1()
        result = solution.compute_all_antinodes(antennas)
        expected = [(0, 0), (3, 3), (1, 0), (1, 3), (3, 2), (0, 2)]

        assert set(result) == set(expected)

    def test_compute_case1(self):
        grid = np.array(
            [
                [".", ".", "."],
                [".", "a", "a"],
                [".", ".", "a"],
            ]
        )
        antenna_grid = AntennaMap(grid)

        solution = Solution1()
        result = solution.compute(antenna_grid)
        expected = [(0, 0), (1, 0), (0, 2)]
        assert set(result) == set(expected)

    def test_compute_case2(self):
        grid = np.array(
            [
                [".", ".", "."],
                [".", "a", "a"],
                [".", ".", "b"],
            ]
        )
        antenna_grid = AntennaMap(grid)

        solution = Solution1()
        result = solution.compute(antenna_grid)
        expected = [(1, 0)]
        assert set(result) == set(expected)


class TestSolution2:
    def test_compute_antinodes(self):
        solution = Solution2()
        antenna1 = Antenna(1, 1, "a")
        antenna2 = Antenna(2, 2, "a")
        expected = [(0, 0), (3, 3), (1, 1), (2, 2)]
        map_size = (4, 4)
        result = solution.compute_antinodes(antenna1, antenna2, map_size)

        assert set(result) == set(expected)

        antenna1 = Antenna(1, 1, "a")
        antenna2 = Antenna(2, 2, "b")
        map_size = (4, 4)

        assert solution.compute_antinodes(antenna1, antenna2, map_size) == []

    def test_compute_all_antinodes(self):
        antenna1 = Antenna(1, 1, "a")
        antenna2 = Antenna(2, 2, "a")
        antenna3 = Antenna(1, 2, "a")
        antennas = [antenna1, antenna2, antenna3]
        map_size = (4, 4)

        solution = Solution2()
        result = solution.compute_all_antinodes(antennas, map_size)
        expected = [
            (0, 0),
            (3, 3),
            (1, 0),
            (1, 3),
            (3, 2),
            (0, 2),
            (1, 1),
            (2, 2),
            (1, 2),
        ]

        assert set(result) == set(expected)

    def test_compute_case1(self):
        grid = np.array(
            [
                [".", ".", "."],
                [".", "a", "a"],
                [".", ".", "a"],
            ]
        )
        antenna_grid = AntennaMap(grid)

        solution = Solution2()
        result = solution.compute(antenna_grid)
        expected = [(0, 0), (1, 0), (0, 2), (1, 1), (1, 2), (2, 2)]
        assert set(result) == set(expected)

    def test_compute_case2(self):
        grid = np.array(
            [
                [".", ".", "."],
                [".", "a", "a"],
                [".", ".", "b"],
            ]
        )
        antenna_grid = AntennaMap(grid)

        solution = Solution2()
        result = solution.compute(antenna_grid)
        expected = [(1, 0), (1, 1), (1, 2)]
        assert set(result) == set(expected)

    def test_compute_case3(self):
        grid = np.array(
            [
                [".", ".", ".", ".", "."],
                [".", ".", ".", ".", "."],
                [".", "a", ".", "a", "."],
                [".", ".", ".", ".", "."],
                [".", ".", ".", ".", "."],
                [".", ".", "b", ".", "."],
                [".", ".", ".", ".", "."],
            ]
        )
        antenna_grid = AntennaMap(grid)

        solution = Solution2()
        result = solution.compute(antenna_grid)
        expected = [(2, 1), (2, 3)]
        assert set(result) == set(expected)

    def test_compute_case4(self):
        grid = np.array(
            [
                [".", ".", ".", ".", "."],
                [".", ".", ".", ".", "."],
                [".", ".", ".", "a", "."],
                [".", ".", ".", ".", "."],
                [".", ".", ".", "a", "."],
                [".", "b", "b", ".", "."],
                [".", ".", ".", ".", "."],
                [".", ".", ".", ".", "."],
                [".", ".", ".", ".", "."],
                [".", ".", ".", ".", "."],
            ]
        )
        antenna_grid = AntennaMap(grid)

        solution = Solution2()
        result = solution.compute(antenna_grid)
        expected = [
            # a
            (0, 3),
            (2, 3),
            (4, 3),
            (6, 3),
            (8, 3),
            # b
            (5, 0),
            (5, 1),
            (5, 2),
            (5, 3),
            (5, 4),
        ]
        assert set(result) == set(expected)


if __name__ == "__main__":
    pytest.main()
