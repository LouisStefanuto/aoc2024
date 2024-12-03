from aoc2024.day3 import (
    clean_operations,
    concatenate_strings,
    extract_digits,
    get_valid_operations,
    mul,
)


def test_concatenate_strings():
    inputs = ["aaaa", "bbbb" "cccc"]
    expected = "aaaabbbbcccc"
    assert concatenate_strings(inputs) == expected


def test_get_valid_operations():
    inputs = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    expected = ["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"]
    assert get_valid_operations(inputs) == expected


def test_extract_digits():
    inputs = "mul(2,4)"
    expected = (2, 4)
    assert extract_digits(inputs) == expected


def test_clean_operations():
    inputs = ["mul(2,4)", "don't()", "mul(5,5)", "mul(11,8)", "do()", "mul(8,5)"]
    expected = ["mul(2,4)", "mul(8,5)"]
    assert clean_operations(inputs) == expected


def test_mul():
    inputs = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    expected = 161
    assert mul(inputs) == expected
