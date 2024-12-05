import numpy as np
import pytest

from aoc2024.day4 import (
    count_matrix,
    count_row,
    count_row_double_sens,
    count_x_matrix,
    extract_all_diagonals,
    is_valid_diag,
    is_valid_x,
)


class TestFirstHalf:
    @pytest.mark.parametrize(
        ("row", "counts"),
        [
            ("XMAS", 1),
            ("XXXXXXXXMASXXXXX", 1),
            ("XXXXXXXXXXXXX", 0),
            ("XMASXMAS", 2),
            ("XMASXXXXXMAS", 2),
        ],
    )
    def test_count_row(self, row, counts):
        assert count_row(row, "XMAS") == counts

    @pytest.mark.parametrize(
        ("row", "counts"),
        [
            ("XMAS", 1),
            ("XXXXXXXXMASXXXXX", 1),
            ("XXXXXXXXXXXXX", 0),
            ("XMASXMAS", 2),
            ("XMASXXXXXMAS", 2),
            ("XMASSAMX", 2),
            ("XMASSAMXMASSAMX", 4),
        ],
    )
    def test_count_row_double_sens(self, row, counts):
        assert count_row_double_sens(row, "XMAS") == counts

    def test_extract_all_diagonals(self):
        matrix = np.array(
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
        )
        result = extract_all_diagonals(matrix)

        assert result == [
            [7],
            [4, 8],
            [1, 5, 9],
            [2, 6],
            [3],
            [9],
            [6, 8],
            [3, 5, 7],
            [2, 4],
            [1],
        ]

    def test_count_matrix(self):
        matrix = np.array(
            [
                [".", ".", "X", ".", ".", "."],
                [".", "S", "A", "M", "X", "."],
                [".", "A", ".", ".", "A", "."],
                ["X", "M", "A", "S", ".", "S"],
                [".", "X", ".", ".", ".", "."],
            ]
        )
        result = count_matrix(matrix)
        assert result == 4

    def test_count_matrix_big(self):
        matrix = np.array(
            [
                [".", ".", ".", ".", "X", "X", "M", "A", "S", "."],
                [".", "S", "A", "M", "X", "M", "S", ".", ".", "."],
                [".", ".", ".", "S", ".", ".", "A", ".", ".", "."],
                [".", ".", "A", ".", "A", ".", "M", "S", ".", "X"],
                ["X", "M", "A", "S", "A", "M", "X", ".", "M", "M"],
                ["X", ".", ".", ".", ".", ".", "X", "A", ".", "A"],
                ["S", ".", "S", ".", "S", ".", "S", ".", "S", "S"],
                [".", "A", ".", "A", ".", "A", ".", "A", ".", "A"],
                [".", ".", "M", ".", "M", ".", "M", ".", "M", "M"],
                [".", "X", ".", "X", ".", "X", "M", "A", "S", "X"],
            ]
        )
        result = count_matrix(matrix)
        assert result == 18


class TestSecondHalf:
    def test_is_valid_diag(self):
        diag = ["M", "A", "S"]
        target = ["M", "A", "S"]
        assert is_valid_diag(diag, target)

    def test_is_valid(self):
        matrix = np.array(
            [
                ["M", ".", "M"],
                [".", "A", "."],
                ["S", ".", "S"],
            ]
        )
        target = ["M", "A", "S"]
        result = is_valid_x(matrix, target)
        assert result is True

    def test_count_x_matrix(self):
        target = ["M", "A", "S"]
        matrix = np.array(
            [
                ["M", ".", "M"],
                [".", "A", "."],
                ["S", ".", "S"],
            ]
        )
        result = count_x_matrix(matrix, target)
        assert result == 1
