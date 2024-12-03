"""
Day 3: Mull It Over
"""

import re
from pathlib import Path

from aoc2024.day1 import open_txt_file


def get_valid_operations(data: str) -> list[str]:
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    return re.findall(pattern, data)


def extract_digits(operation: str) -> tuple[int, int]:
    a, b = operation[4:-1].split(",")
    return int(a), int(b)


def mul(data: str) -> int:
    valid_operations = get_valid_operations(data)
    digit_pairs = [extract_digits(operation) for operation in valid_operations]
    return sum([a * b for a, b in digit_pairs])


if __name__ == "__main__":
    inputs = open_txt_file(Path("inputs/day3.txt"))
    results = [mul(input) for input in inputs]
    print(sum(results))
