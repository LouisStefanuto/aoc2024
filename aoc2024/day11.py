from functools import cache
from pathlib import Path

from aoc2024.day1 import open_txt_file, slice_data


@cache
def update(stone: int) -> tuple[int, int | None]:
    if stone == 0:
        return 1, None
    elif len(str(stone)) % 2 == 0:
        string_stone = str(stone)
        first_half = int(string_stone[len(string_stone) // 2 :])
        second_half = int(string_stone[: len(string_stone) // 2])
        return first_half, second_half
    else:
        return stone * 2024, None


def blink_n_times(freq_dict: dict[int, int], n: int) -> dict[int, int]:
    for i in range(n):
        freq_dict = blink_one_time(freq_dict)
        print(f"Episode {i}: {compute_result(freq_dict)}")
    return freq_dict


def blink_one_time(freq_dict: dict[int, int]) -> dict[int, int]:
    updated_freq_dict: dict[int, int] = {}

    for stone in freq_dict.keys():
        first, second = update(stone)
        updated_freq_dict[first] = updated_freq_dict.get(first, 0) + freq_dict[stone]
        if second:
            updated_freq_dict[second] = (
                updated_freq_dict.get(second, 0) + freq_dict[stone]
            )

    return updated_freq_dict


def build_dict(stones: list[int]) -> dict[int, int]:
    freq_dict: dict[int, int] = {}
    for stone in stones:
        freq_dict[stone] = freq_dict.get(stone, 0) + 1
    return freq_dict


def compute_result(freq_dict: dict[int, int]) -> int:
    return sum(freq_dict.values())


if __name__ == "__main__":
    inputs = open_txt_file(Path("inputs/day11.txt"))
    stones = slice_data(inputs)[0]
    freq_dict = build_dict(stones)
    freq_dict = blink_n_times(freq_dict, 75)
