import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from aoc2024.day4 import read_file_to_list


def parse_robot(line: str) -> tuple[int, int, int, int]:
    position, speed = line.split(" ")
    position_y, position_x = position.split("p=")[1].split(",")
    speed_y, speed_x = speed.split("v=")[1].split(",")
    return int(position_x), int(position_y), int(speed_x), int(speed_y)


@dataclass
class Robot:
    px: int
    py: int
    vx: int
    vy: int
    max_x: int
    max_y: int

    def update(self) -> None:
        self.px = (self.px + self.vx) % self.max_x
        self.py = (self.py + self.vy) % self.max_y


def count_robots(
    robots: list[Robot], max_x: int, max_y: int
) -> tuple[int, int, int, int]:
    topleft, topright, bottomleft, bottomright = 0, 0, 0, 0

    for robot in robots:
        if robot.px < max_x // 2 and robot.py < max_y // 2:
            topleft += 1
        elif robot.px < max_x // 2 and robot.py > max_y // 2:
            topright += 1
        elif robot.px > max_x // 2 and robot.py < max_y // 2:
            bottomleft += 1
        elif robot.px > max_x // 2 and robot.py > max_y // 2:
            bottomright += 1

    return topleft, topright, bottomleft, bottomright


def solution1(
    lines: list[str], num_updates: int = 100, max_x: int = 103, max_y: int = 101
) -> int:
    robots = [Robot(*parse_robot(line), max_x, max_y) for line in lines]

    for i in range(num_updates):
        for robot in robots:
            robot.update()

        s = display_robots(robots)

        if "#######" in s:  # Detect tree
            print(i)
            print(s)

    quadrants = count_robots(robots, max_x, max_y)
    return math.prod(quadrants)


def display_robots(robots: list[Robot], max_x: int = 103, max_y: int = 101) -> str:
    terrain = np.zeros((max_x, max_y), dtype=int)
    for robot in robots:
        terrain[robot.px, robot.py] += 1

    # Convert the terrain matrix to a readable string
    display = ""
    for y in range(max_y):  # Iterate over rows (Y-axis)
        for x in range(max_x):  # Iterate over columns (X-axis)
            if terrain[x, y] == 0:
                display += "."  # Empty cell
            else:
                display += "#"  # Occupied by at least one robot
        display += "\n"  # Newline after each row

    return display


if __name__ == "__main__":
    lines = read_file_to_list(Path("inputs/day14.txt"))
    print(f"Result1: {solution1(lines, 100000, 103, 101)}")
