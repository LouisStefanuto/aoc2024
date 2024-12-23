from pathlib import Path
from typing import Optional

from aoc2024.day4 import read_file_to_list


class Game:
    def __init__(self, lines: list[str]):
        self.a = int(lines[0].split(": ")[-1])
        self.b = int(lines[1].split(": ")[-1])
        self.c = int(lines[2].split(": ")[-1])
        self.program = [int(n) for n in lines[4].split(": ")[-1].split(",")]

        self.pointer_instruction = 0

    def run(self) -> str:
        results = []
        while 0 <= self.pointer_instruction < len(self.program) - 1:
            result = self.apply()
            if result is not None:
                results.append(result)
        return ",".join([str(x) for x in results])

    def combo(self, operand: int) -> int:
        if operand == 4:
            return self.a
        elif operand == 5:
            return self.b
        elif operand == 6:
            return self.c

        return operand

    def apply(self) -> Optional[int]:
        instruction = self.program[self.pointer_instruction]
        operand = self.program[self.pointer_instruction + 1]
        jump = 2
        result = None

        if instruction == 0:
            self.a = self.a // (2 ** self.combo(operand))

        elif instruction == 1:
            self.b = self.b ^ operand

        elif instruction == 2:
            self.b = self.combo(operand) % 8

        elif instruction == 3 and self.a != 0:
            self.pointer_instruction = operand
            jump = 0

        elif instruction == 4:
            self.b = self.b ^ self.c

        elif instruction == 5:
            result = self.combo(operand) % 8

        elif instruction == 6:
            self.b = self.a // (2 ** self.combo(operand))

        elif instruction == 7:
            self.c = self.a // (2 ** self.combo(operand))

        self.pointer_instruction += jump

        return result


if __name__ == "__main__":
    lines = read_file_to_list(Path("inputs/day17.txt"))
    game = Game(lines)
    print("A:", game.a)
    print("B:", game.b)
    print("C:", game.c)
    print("Program:", game.program)

    result = game.run()
    print(result)
