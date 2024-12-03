"""
Day 2: Red-Nosed Reports
"""

from pathlib import Path

from aoc2024.day1 import open_txt_file, slice_data


def is_safe(levels: list[int]) -> bool:
    ascending = True  # by default, will be set at first iteration

    for i in range(len(levels) - 1):
        left = levels[i]
        right = levels[i + 1]
        diff = right - left

        if i == 0:
            # Set mode with the first difference
            ascending = diff > 0

        if (diff == 0) or (abs(diff) > 3) or (ascending != (diff > 0)):
            return False

    return True


def is_safe_v2(levels: list[int]) -> bool:
    safe_sub_levels = []
    for i in range(len(levels)):
        safe_sub_levels.append(is_safe(levels[:i] + levels[i + 1 :]))
    return sum(safe_sub_levels) > 0


if __name__ == "__main__":
    inputs = open_txt_file(Path("inputs/day2.txt"))
    reports = slice_data(inputs)

    valid_reports = [is_safe(levels) for levels in reports]
    print(sum(valid_reports))

    valid_reports = [is_safe_v2(levels) for levels in reports]
    print(sum(valid_reports))
