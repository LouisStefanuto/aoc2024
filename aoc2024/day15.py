from enum import StrEnum
from pathlib import Path

import numpy as np

from aoc2024.day4 import convert_to_matrix, read_file_to_list

COMMANDS = {
    ">": (0, 1),
    "<": (0, -1),
    "v": (1, 0),
    "^": (-1, 0),
}


class Config(StrEnum):
    ROBOT = "@"
    WALL = "#"
    VOID = "."
    BOX = "O"


class WareHouse:
    def __init__(self, grid: np.ndarray):
        self.grid = grid
        self.robot_x, self.robot_y = np.argwhere(grid == Config.ROBOT).tolist()[0]

    def update(self, command: str) -> None:
        """
        Look in the direction of the command
        Compute next position

        While next position is in not # or ".":
          Add next position to boxes to move
          position = next
          next = next next

        Move all boxes
        Move robot
        """
        move_x, move_y = COMMANDS[command]
        next_robot_x = self.robot_x + move_x
        next_robot_y = self.robot_y + move_y

        x0 = self.robot_x
        y0 = self.robot_y
        to_move = [(x0, y0)]

        while self.grid[next_robot_x, next_robot_y] not in [Config.WALL, Config.VOID]:
            to_move.append((next_robot_x, next_robot_y))
            next_robot_x = next_robot_x + move_x
            next_robot_y = next_robot_y + move_y

        if self.grid[next_robot_x, next_robot_y] == Config.WALL:
            return

        for x, y in to_move[::-1]:
            self.grid[x + move_x, y + move_y] = self.grid[x, y]

        # Move robot
        self.robot_x += move_x
        self.robot_y += move_y
        self.grid[x0, y0] = Config.VOID

    def compute_cost(self) -> int:
        boxes = np.argwhere(self.grid == Config.BOX).tolist()
        return sum([100 * box[0] + box[1] for box in boxes])


if __name__ == "__main__":
    data = read_file_to_list(Path("inputs/day15b.txt"))
    grid, commands = convert_to_matrix(data[:-2]), list(data[-1])

    warehouse = WareHouse(grid)
    for command in commands:
        warehouse.update(command)

    print(f"Result1: {warehouse.compute_cost()}")
