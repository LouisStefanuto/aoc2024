"""
Start S / Exit E
One move += 1 / Turn += 1000
"""

from heapq import heappop, heappush
from pathlib import Path

import numpy as np

from aoc2024.day4 import convert_to_matrix, read_file_to_list


class Config:
    START = "S"
    END = "E"
    OBSTACLE = "#"


class Maze:
    def __init__(self, grid: np.ndarray):
        self.grid = grid
        self._moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def solve(self) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        start_x, start_y = np.argwhere(self.grid == Config.START)[0].tolist()
        end_x, end_y = np.argwhere(self.grid == Config.END)[0].tolist()

        pq = [(0, start_x, start_y, 0)]
        visited = set()

        while len(pq) > 0:
            cost, x, y, direction = heappop(pq)

            if (x, y) == (end_x, end_y):
                return cost

            if (x, y, direction) in visited:
                continue
            visited.add((x, y, direction))

            # Explore neighbors
            for new_dir, (dr, dc) in enumerate(directions):
                new_row, new_col = x + dr, y + dc

                # Check bounds and if it's a valid path
                if (
                    0 <= new_row < self.grid.shape[0]
                    and 0 <= new_col < self.grid.shape[1]
                    and self.grid[new_row][new_col] != Config.OBSTACLE
                ):
                    # Calculate the cost to move
                    if direction == new_dir:
                        new_cost = cost + 1
                    else:
                        new_cost = cost + 1000 + 1

                    heappush(pq, (new_cost, new_row, new_col, new_dir))

        # No path found
        return -1


if __name__ == "__main__":
    data = read_file_to_list(Path("inputs/day16.txt"))
    grid = convert_to_matrix(data)
    maze = Maze(grid)
    print(maze.solve())
