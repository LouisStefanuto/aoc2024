from pathlib import Path

import numpy as np

from aoc2024.day4 import convert_to_matrix, read_file_to_list

Area = int
Perimeter = int


class CropWorld:
    def __init__(self, grid: np.ndarray):
        self.grid = grid
        self.visited = np.zeros_like(self.grid, dtype=int)
        self._neighbors = {(-1, 0), (1, 0), (0, -1), (0, 1)}

    def solve(self) -> int:
        N, M = self.grid.shape
        parcels = []

        for i in range(N):
            for j in range(M):
                if not self.visited[i, j]:
                    area, perimeter = self.dfs(i, j)
                    parcels.append((area, perimeter))

        return compute_price(parcels)

    def dfs(self, i: int, j: int) -> tuple[Area, Perimeter]:
        """
        Depth-first search algorithm.
        """
        N, M = self.grid.shape

        area: Area = 0
        perimeter: Perimeter = 0

        queue = []
        queue.append((i, j))

        while len(queue) > 0:
            i, j = queue.pop()

            if not self.visited[i, j]:
                self.visited[i, j] = 1
                area += 1

                for di, dj in self._neighbors:
                    nexti, nextj = i + di, j + dj
                    next_is_in = 0 <= nexti and nexti < N and 0 <= nextj and nextj < M

                    if (
                        next_is_in
                        and self.grid[nexti, nextj] == self.grid[i, j]
                        and not self.visited[nexti, nextj]
                    ):
                        # Found similar crop
                        queue.append((nexti, nextj))
                    elif not next_is_in or self.grid[nexti, nextj] != self.grid[i, j]:
                        # We are at a parcel frontier
                        perimeter += 1

        return area, perimeter


def compute_price(parcels: list[tuple[Area, Perimeter]]) -> int:
    return sum([area * perimeter for area, perimeter in parcels])


if __name__ == "__main__":
    data = read_file_to_list(Path("inputs/day12.txt"))
    grid = convert_to_matrix(data)
    world = CropWorld(grid)
    print(f"Result1: {world.solve()}")
