"""
Day 3: Mull It Over
"""

import re
from pathlib import Path

from aoc2024.day1 import open_txt_file


def concatenate_strings(inputs: list[str]) -> str:
    concatenation = ""
    for x in inputs:
        concatenation += x
    return concatenation


def get_valid_operations(data: str) -> list[str]:
    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    return re.findall(pattern, data)


def clean_operations(operations: list[str]) -> list[str]:
    enabled = True

    cleaned_operations = []
    for operation in operations:
        if operation == "do()":
            enabled = True
            print("Enable")
        elif operation == "don't()":
            enabled = False
            print("Disable")
        else:
            if enabled:
                cleaned_operations.append(operation)
                print("Accepted:", operation)
            if not enabled:
                print("Refused:", operation)

    return cleaned_operations


def extract_digits(operation: str) -> tuple[int, int]:
    a, b = operation[4:-1].split(",")
    return int(a), int(b)


def mul(data: str) -> int:
    valid_operations = get_valid_operations(data)
    valid_operations = clean_operations(valid_operations)
    digit_pairs = [extract_digits(operation) for operation in valid_operations]
    return sum([a * b for a, b in digit_pairs])


if __name__ == "__main__":
    raw_inputs = open_txt_file(Path("inputs/day3.txt"))
    inputs = concatenate_strings(raw_inputs)

    results = mul(inputs)
    print(results)
