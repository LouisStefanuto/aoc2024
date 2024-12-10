from pathlib import Path

from aoc2024.day4 import read_file_to_list

SPACE = "."


class Disk:
    def __init__(self, state: str):
        self.state = state
        self.processed = [int(x) for x in state]

    def __len__(self) -> int:
        return len(self.state)

    def encode(self) -> list[str]:
        s = []
        for i, x in enumerate(self.processed):
            if i % 2 == 0:
                s += [str(i // 2)] * (x)
            else:
                s += [SPACE] * x
        return s

    def compact(self) -> list[str]:
        code = self.encode()
        left, right = 0, len(code) - 1

        while left < right:
            if code[left] == SPACE:
                if code[right] != SPACE:
                    code[left], code[right] = code[right], code[left]
                right -= 1
            else:
                left += 1

        return code


def checksum(numbers: list[str]) -> int:
    s = 0
    for i, n in enumerate(numbers):
        if n != SPACE:
            s += i * int(n)
    return s


if __name__ == "__main__":
    data = read_file_to_list(Path("inputs/day9.txt"))[0]
    disk = Disk(data)
    code_compacted = disk.compact()
    result1 = checksum(code_compacted)
    print(f"Result1: {result1}")
