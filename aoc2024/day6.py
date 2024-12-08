"""
Step1:

Draw guard trajectory

    Get next position of the guard.
        next = look in direction
        while next is obstacle:
            turn direction to the right
            compute new next position
    Move the guard to next.

Count the number of X

"""

from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path

import numpy as np

from aoc2024.day4 import convert_to_matrix, read_file_to_list


class GuardDirection(StrEnum):
    RIGHT = ">"
    LEFT = "<"
    UP = "^"
    DOWN = "v"


# For updates when hitting an obstacle
DIR_CLOCKWISE = {
    GuardDirection.UP: GuardDirection.RIGHT,
    GuardDirection.RIGHT: GuardDirection.DOWN,
    GuardDirection.DOWN: GuardDirection.LEFT,
    GuardDirection.LEFT: GuardDirection.UP,
}


@dataclass
class Guard:
    x: int
    y: int
    direction: GuardDirection


class Terrain:
    def __init__(self, grid: np.ndarray):
        self.grid = grid
        self.nb_x: int = 0

        self.guard = self.find_guard()
        # Track visited positions as (x, y, direction)
        self.visited: set[tuple[int, int, GuardDirection]] = set()

    def __repr__(self) -> str:
        grid_str = "\n".join("".join(row) for row in self.grid)
        return "\n" + grid_str + "\n"

    def find_guard(self) -> Guard:
        """
        Assume there is only one guard in the terrain.
        """
        N, M = self.grid.shape
        for i in range(N):
            for j in range(M):
                if self.grid[i, j] in GuardDirection:
                    direction = GuardDirection(self.grid[i, j])
                    return Guard(i, j, direction)
        raise ValueError("Guard not found in the terrain.")

    def is_position_out(self, x: int, y: int) -> bool:
        N, M = self.grid.shape
        return x < 0 or x >= N or y < 0 or y >= M

    def get_next_move(self) -> tuple[Guard, bool]:
        direction = self.guard.direction

        # Force at least one iteration
        next_is_obstacle = True

        while next_is_obstacle:
            if direction == GuardDirection.RIGHT:
                next_x = self.guard.x
                next_y = self.guard.y + 1
            elif direction == GuardDirection.LEFT:
                next_x = self.guard.x
                next_y = self.guard.y - 1
            elif direction == GuardDirection.UP:
                next_x = self.guard.x - 1
                next_y = self.guard.y
            elif direction == GuardDirection.DOWN:
                next_x = self.guard.x + 1
                next_y = self.guard.y
            else:
                raise ValueError(f"Direction is not in {GuardDirection}")

            if self.is_position_out(next_x, next_y):
                # Next is out, return terminal is True
                return Guard(next_x, next_y, direction), True

            # The next position is in the grid.
            next_is_obstacle = self.grid[next_x, next_y] in ["#", "O"]

            if next_is_obstacle:
                # Case obstacle: Turn guard to the right and retry
                direction = DIR_CLOCKWISE[direction]

        # If next is found, return terminal is False
        return Guard(next_x, next_y, direction), False

    def move_guard(self) -> tuple[bool, bool]:
        """
        Move the guard to the next valid position. Return a pair of booleans:
        - loop: If the guard has already been in this position/direction in a previously visited state.
        - terminal: True if state is terminal, False otherwise.
        """
        if (self.guard.x, self.guard.y, self.guard.direction) in self.visited:
            return True, False  # Loop, not terminal

        # State never visited before. Add it to visited states
        self.visited.add((self.guard.x, self.guard.y, self.guard.direction))
        self.grid[self.guard.x, self.guard.y] = "X"

        next_guard, terminal = self.get_next_move()
        if terminal:
            return False, True  # No loop, terminal

        # Update guard position
        self.guard = next_guard

        return False, False  # No loop, not terminal

    def solution1(self) -> tuple[int, bool]:
        loop, terminal = False, False

        while (not terminal) and (not loop):
            loop, terminal = self.move_guard()

        unique_pos: set[tuple[int, int]] = set()
        for pos in self.visited:
            unique_pos.add((pos[0], pos[1]))

        return len(unique_pos), loop

    def is_loop(self) -> bool:
        return self.solution1()[1]


def solution2(input_path: Path) -> int:
    # Initialize
    data = read_file_to_list(input_path)
    arr = convert_to_matrix(data)
    terrain = Terrain(arr)
    guard = terrain.find_guard()

    N, M = arr.shape
    result2 = 0

    for i in range(N):
        for j in range(M):
            data = read_file_to_list(input_path)
            arr = convert_to_matrix(data)
            terrain = Terrain(arr)

            # Ignore the case where the object is in the guard
            if (i, j) != (guard.x, guard.y):
                terrain.grid[i, j] = "O"  # obstacle
                is_loop = terrain.is_loop()
                result2 += int(is_loop)

                print(f"Tested ({i:03}, {j:03} - {is_loop})")
                if is_loop:
                    print(terrain)

    return result2


if __name__ == "__main__":
    input_path = Path("inputs/day6.txt")

    data = read_file_to_list(input_path)
    arr = convert_to_matrix(data)
    terrain = Terrain(arr)
    print(terrain)

    result1, _ = terrain.solution1()
    print(f"Result1: Unique visited positions: {result1}")

    result2 = solution2(input_path)
    print(f"Result2: {result2}")
