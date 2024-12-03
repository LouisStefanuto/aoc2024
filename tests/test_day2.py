import pytest

from aoc2024.day2 import is_safe, is_safe_v2


@pytest.mark.parametrize(
    ["inputs", "expected"],
    [
        ([1, 2, 3], True),
        ([3, 2, 1], True),
        ([7, 6, 4, 2, 1], True),
        ([1, 2, 7, 8, 9], False),
        ([9, 7, 6, 2, 1], False),
        ([1, 3, 2, 4, 5], False),
        ([8, 6, 4, 4, 1], False),
    ],
)
def test_is_safe(inputs: list[int], expected: bool):
    assert is_safe(inputs) == expected


@pytest.mark.parametrize(
    ["inputs", "expected"],
    [
        ([1, 2, 3], True),
        ([3, 2, 1], True),
        ([7, 6, 4, 2, 1], True),
        ([1, 2, 7, 8, 9], False),
        ([9, 7, 6, 2, 1], False),
        ([1, 3, 2, 4, 5], True),
        ([8, 6, 4, 4, 1], True),
    ],
)
def test_is_safe_v2(inputs: list[int], expected: bool):
    assert is_safe_v2(inputs) == expected
