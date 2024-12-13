from pathlib import Path

from aoc2024.day1 import open_txt_file, slice_data


def blink_n_times(stones: list[int], n: int) -> list[int]:
    for _ in range(n):
        stones = blink_one_time(stones)

    return stones


def blink_one_time(stones: list[int]) -> list[int]:
    updated_stones: list[int] = []

    for stone in stones:
        if stone == 0:
            updated_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            string_stone = str(stone)
            first_half = int(string_stone[len(string_stone) // 2 :])
            second_half = int(string_stone[: len(string_stone) // 2])
            updated_stones.append(second_half)
            updated_stones.append(first_half)
        else:
            updated_stones.append(stone * 2024)

    return updated_stones


if __name__ == "__main__":
    inputs = open_txt_file(Path("inputs/day11.txt"))
    data = slice_data(inputs)[0]
    print(len(blink_n_times(data, 25)))
