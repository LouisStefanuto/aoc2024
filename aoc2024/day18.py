from collections import deque
from pathlib import Path

import numpy as np

from aoc2024.day4 import read_file_to_list

Position = tuple[int, int]


def split_line(s: str) -> Position:
    a, b = s.split(",")
    return int(a), int(b)


def build_matrix(n: int, obstacles: list[Position]) -> np.ndarray:
    matrix = np.full((n, n), ".")
    for i, j in obstacles:
        matrix[i, j] = "#"
    return matrix


class Maze:
    def __init__(self, grid: np.ndarray):
        self.grid = grid
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def bfs(self) -> int:
        queue: deque = deque()
        queue.append((0, 0, 0))
        visited = set()

        while queue:
            x, y, distance = queue.popleft()

            if (x, y) == (self.grid.shape[0] - 1, self.grid.shape[1] - 1):
                return distance

            if (x, y) in visited:
                continue

            visited.add((x, y))
            for dx, dy in self.directions:
                new_x, new_y = x + dx, y + dy
                if (
                    0 <= new_x < self.grid.shape[0]
                    and 0 <= new_y < self.grid.shape[1]
                    and self.grid[new_x, new_y] != "#"
                ):
                    queue.append((new_x, new_y, distance + 1))

        return -1

    def __repr__(self) -> str:
        lines = ["".join(x) for x in self.grid]
        return "\n".join(lines)


if __name__ == "__main__":
    lines = read_file_to_list(Path("inputs/day18.txt"))
    data = [split_line(line) for line in lines][:1024]
    matrix = build_matrix(71, data)
    maze = Maze(matrix)
    print("Result1:", maze.bfs())
    print(maze)
