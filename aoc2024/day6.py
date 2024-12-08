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
        # Add initial position to visited
        self.visited.add((self.guard.x, self.guard.y, self.guard.direction))

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

            # If next is out, return terminal is True
            if self.is_position_out(next_x, next_y):
                return Guard(next_x, next_y, direction), True

            # The next position is in the grid.
            next_is_obstacle = self.grid[next_x, next_y] == "#"

            if next_is_obstacle:
                # Case obstacle: Turn guard to the right and retry
                direction = DIR_CLOCKWISE[self.guard.direction]

        # If next is found, return terminal is False
        return Guard(next_x, next_y, direction), False

    def move_guard(self) -> bool:
        """
        Move the guard to the next valid position. Returns True if terminal, False otherwise.
        """
        self.visited.add((self.guard.x, self.guard.y, self.guard.direction))

        next_guard, terminal = self.get_next_move()
        if terminal:
            return True  # End movement

        # Update guard position and add to visited set
        self.guard = next_guard

        return False

    def solution1(self):
        terminal = False
        while not terminal:
            terminal = self.move_guard()

        unique_pos: set[str] = set()
        for pos in self.visited:
            unique_pos.add((pos[0], pos[1]))

        return len(unique_pos)


if __name__ == "__main__":
    data = read_file_to_list(Path("inputs/day6.txt"))
    arr = convert_to_matrix(data)
    terrain = Terrain(arr)

    result1 = terrain.solution1()
    print(f"Result1: Unique visited positions: {result1}")
