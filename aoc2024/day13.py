"""
Button A costs 3 token
Button B costs 1 token

2 axes -> classic plot-like orientation
- X: moving to the right
- Y: moving forward

Machine: claw position + prize position

Goal: for each machine find the combinaison of moves that reaches the prize, in the least number of tokens

----------
Button A: (a,b)
Button B (c,d)
Target: (e,f)

Let (x,y) be the number of pushes on buttons A and B.
(1) ax + cy = e
(2) bx + dy = f

MX = y
    where M = (a c) and y = (e)
              (b d)         (f)

Solution: X = M^{-1} * y

There are essentially 3 possible cases:
- unique solution: det(M) != 0
- no solution -> no case in the input data
- the 2 buttons are equivalent -> no case in the input data
"""

from dataclasses import dataclass
from pathlib import Path

import numpy as np

from aoc2024.day4 import read_file_to_list


def parse_button(line: str) -> tuple[int, int]:
    x, y = [int(a[2:]) for a in line[10:].split(", ")]
    return x, y


def parse_prize(line: str) -> tuple[int, int]:
    x, y = [int(a[2:]) for a in line[7:].split(", ")]
    return x, y


@dataclass
class Button:
    x: int
    y: int
    cost: int


@dataclass
class Prize:
    x: int
    y: int


class Machine:
    def __init__(self, a: Button, b: Button, prize: Prize):
        self.M = np.array(
            [
                [a.x, b.x],
                [a.y, b.y],
            ]
        )
        self.y = np.array([prize.x, prize.y])

    def solve(self) -> np.ndarray:
        return np.linalg.inv(self.M) @ self.y


def build_machines(lines: list[str]) -> list[Machine]:
    machines = []
    for i in range(0, len(lines), 4):
        button_a = Button(*parse_button(lines[i]), 3)
        button_b = Button(*parse_button(lines[i + 1]), 1)
        prize = Prize(*parse_prize(lines[i + 2]))

        machine = Machine(button_a, button_b, prize)
        machines.append(machine)
    return machines


def compute_cost(answer: np.ndarray) -> int:
    # Convert a NumPy float array to integers, raising an error if any value has a decimal part.
    rounded = np.round(answer)  # Round to the nearest integer
    if not np.allclose(answer, rounded, atol=1e-5):
        return 0
    answer = rounded.astype(int)

    a, b = answer
    if a < 0 or b < 0 or a >= 100 or b >= 100:
        return 0

    return 3 * a + b


def solution1(machines: list[Machine]) -> int:
    total_cost = 0
    for machine in machines:
        solution = machine.solve()
        cost = compute_cost(solution)
        total_cost += cost
        print(f"Solution: {solution} | Cost: {cost}")
    return total_cost


if __name__ == "__main__":
    lines = read_file_to_list(Path("inputs/day13.txt"))
    machines = build_machines(lines)
    print(f"Result1: {solution1(machines)}")
