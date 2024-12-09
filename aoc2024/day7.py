from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path

from aoc2024.day4 import read_file_to_list

Operation = list[str]


class Operator(StrEnum):
    ADD = "+"
    MUL = "*"


@dataclass
class Equation:
    result: int
    numbers: list[int]

    def compute_operation(self, operation: Operation) -> int:
        if len(operation) != len(self.numbers) - 1:
            raise ValueError("Invalid operation. Too many/much operators.")

        result = self.numbers[0]

        for i, operator in enumerate(operation):
            if operator == Operator.ADD:
                result += self.numbers[i + 1]
            elif operator == Operator.MUL:
                result *= self.numbers[i + 1]
            else:
                raise ValueError("Invalid operator encountered when computing result.")

        return result

    def list_operations(self) -> list[Operation]:
        num_operators = len(self.numbers) - 1
        operations: list[Operation] = [[]]

        len_operation = 0
        while len_operation < num_operators:
            tmp_operations = []
            for operation in operations:
                tmp_operations.append(operation + ["+"])
                tmp_operations.append(operation + ["*"])
            operations = tmp_operations
            len_operation += 1

        return operations

    def has_solution(self) -> bool:
        operations = self.list_operations()
        for operation in operations:
            if self.compute_operation(operation) == self.result:
                return True
        return False


def split_line(line: str) -> Equation:
    result, numbers = line.split(": ")
    return Equation(int(result), [int(n) for n in numbers.split(" ")])


def solution1(equations: list[Equation]) -> int:
    result = 0
    for equation in equations:
        if equation.has_solution():
            result += equation.result

    return result


if __name__ == "__main__":
    lines = read_file_to_list(Path("inputs/day7.txt"))
    equations = [split_line(line) for line in lines]
    result1 = solution1(equations)
    print(f"Result1: {result1}")
