"""
Day 1: Historian Hysteria
"""

from pathlib import Path


def compute_distances(list1: list, list2: list):
    list1 = sorted(list1)
    list2 = sorted(list2)
    offsets = [abs(x - y) for (x, y) in zip(list1, list2)]
    return sum(offsets)


def open_txt_file(file_path: Path) -> list[str]:
    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines


def slice_data(lines: list[str]) -> list[list[int]]:
    data = []
    for line in lines:
        data_line = list(map(int, line.split()))
        data.append(data_line)
    return data


def preprocess_data(lines: list[list[int]]) -> tuple[list[int], list[int]]:
    list1, list2 = [], []
    for x, y in lines:
        list1.append(x)
        list2.append(y)
    return list1, list2


def occurences(a: list[int]) -> dict[int, int]:
    counts: dict[int, int] = dict()
    for x in a:
        counts[x] = counts.get(x, 0) + 1
    return counts


def similarity_score(left: list[int], right: list[int]) -> int:
    unique_left = set(left)
    right_counts = occurences(right)
    return sum([x * right_counts.get(x, 0) for x in unique_left])


if __name__ == "__main__":
    inputs = open_txt_file(Path("inputs/day1.txt"))
    data = slice_data(inputs)
    list1, list2 = preprocess_data(data)

    result1 = compute_distances(list1, list2)
    print(result1)

    result2 = similarity_score(list1, list2)
    print(result2)
