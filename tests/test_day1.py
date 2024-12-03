import pytest

from aoc2024.day1 import (
    compute_distances,
    occurences,
    preprocess_data,
    similarity_score,
    slice_data,
)


class TestFirstHalf:
    @pytest.mark.parametrize(
        ["list1", "list2", "expected"],
        [
            ([0, 0, 0], [0, 0, 0], 0),
            ([0, 0, 0], [1, 1, 1], 3),
            ([1, 2, 3], [2, 3, 4], 3),
        ],
    )
    def test_compute_distances(self, list1: list[int], list2: list[int], expected: int):
        assert compute_distances(list1, list2) == expected

    def test_preprocess_data(self):
        inputs = [[1, 1], [2, 2], [3, 3]]
        expected = ([1, 2, 3], [1, 2, 3])
        assert preprocess_data(inputs) == expected

    def test_slice_data(self):
        inputs = ["47078   87818\n", "99261   15906\n", "44723   23473\n"]
        result = [[47078, 87818], [99261, 15906], [44723, 23473]]
        assert slice_data(inputs) == result


class TestSecondHalf:
    @pytest.mark.parametrize(
        ["a", "expected"],
        [
            ([1, 1, 1, 2, 2, 3], {1: 3, 2: 2, 3: 1}),
            ([1, 1, 1, 1, 1, 1], {1: 6}),
            ([1, 1, 1, 1, 1, 0], {1: 5, 0: 1}),
        ],
    )
    def test_occurences(self, a: list[int], expected: dict[int, int]):
        assert occurences(a) == expected

    @pytest.mark.parametrize(
        ["list1", "list2", "expected"],
        [
            ([0, 0, 0], [0, 0, 0], 0),
            ([0, 0, 0], [1, 1, 1], 0),
            ([1, 2, 3], [2, 3, 4], 5),
            ([1, 1, 1], [1, 1, 1], 3),
            ([1, 1, 1], [1, 1, 2], 2),
            ([1, 1, 1, 2, 2, 2], [1, 1, 1, 2, 2, 2], 9),
        ],
    )
    def test_similarity_score(self, list1: list[int], list2: list[int], expected: int):
        assert similarity_score(list1, list2) == expected
