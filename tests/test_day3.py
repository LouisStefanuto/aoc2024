from aoc2024.day3 import extract_digits, get_valid_operations, mul


def test_get_valid_operations():
    inputs = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    expected = ["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"]
    assert get_valid_operations(inputs) == expected


def test_extract_digits():
    inputs = ["mul(2,4)"]
    expected = (2, 4)
    assert extract_digits(inputs) == expected


def test_mul():
    inputs = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    expected = 161
    assert mul(inputs) == expected
