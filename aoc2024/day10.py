from pathlib import Path

import numpy as np

from aoc2024.day4 import convert_to_matrix, read_file_to_list

Position = tuple[int, int]


class Config:
    START: int = 0
    END: int = 9


class MountainWorld:
    def __init__(self, grid: np.ndarray):
        self.grid = grid
        self.N, self.M = grid.shape
        self._neighbors = {(-1, 0), (1, 0), (0, -1), (0, 1)}

    def shape(self) -> int:
        return self.grid.shape

    def solve(self) -> int:
        result = 0

        for i in range(self.N):
            for j in range(self.M):
                if self.grid[i, j] == Config.START:
                    ends = self.get_ends_from(i, j, [])
                    result += len(set(ends))  # Unique

        return result

    def solve2(self) -> int:
        result = 0

        for i in range(self.N):
            for j in range(self.M):
                if self.grid[i, j] == Config.START:
                    ends = self.get_ends_from(i, j, [])
                    result += len(ends)  # No unique

        return result

    def get_ends_from(self, i: int, j: int, ends: list[Position]) -> list[Position]:
        if self.grid[i, j] == Config.END:
            # Reached top
            return ends + [(i, j)]

        # Explore neighbor cells
        for dx, dy in self._neighbors:
            nexti, nextj = i + dx, j + dy
            if (
                0 <= nexti
                and nexti < self.N
                and 0 <= nextj
                and nextj < self.M
                and self.grid[nexti, nextj] == self.grid[i, j] + 1
            ):
                ends = self.get_ends_from(nexti, nextj, ends)

        return ends


if __name__ == "__main__":
    data = read_file_to_list(Path("inputs/day10.txt"))
    grid = convert_to_matrix(data)
    grid = grid.astype(int)
    world = MountainWorld(grid)

    print(f"Result1: {world.solve()}")
    print(f"Result2: {world.solve2()}")
