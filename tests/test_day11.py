import pytest

from aoc2024.day11 import blink_n_times, blink_one_time, build_dict


def test_blink_one_time_case1():
    assert blink_one_time({125: 1, 17: 1}) == {253000: 1, 1: 1, 7: 1}


def test_blink_one_time_case2():
    assert blink_one_time({253000: 1, 1: 1, 7: 1}) == {253: 1, 0: 1, 2024: 1, 14168: 1}


def test_blink_one_time_case3():
    assert blink_one_time({253: 1, 0: 1, 2024: 1, 14168: 1}) == {
        512072: 1,
        1: 1,
        20: 1,
        24: 1,
        28676032: 1,
    }


def test_solution():
    data = [125, 17]
    expected = {
        2097446912: 1,
        14168: 1,
        4048: 1,
        2: 4,
        0: 2,
        4: 1,
        40: 2,
        48: 2,
        2024: 1,
        80: 1,
        96: 1,
        8: 1,
        6: 2,
        7: 1,
        3: 1,
    }

    freq_dict = build_dict(data)
    freq_dict = blink_n_times(freq_dict, 6)

    assert freq_dict == expected


if __name__ == "__main__":
    pytest.main()
