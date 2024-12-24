"""
Initialize the queue with the design

While the list contains designs:

    Take a design
    If the design is empty:
        return True

    For pattern in patterns:
        if design[:len(pattern)] == pattern:
            queue.append(design[len(pattern):])

return False
"""

from pathlib import Path

from aoc2024.day4 import read_file_to_list


def parse_input(file: Path) -> tuple[list[str], list[str]]:
    data = read_file_to_list(file)
    return data[0].split(", "), data[2:]  # patterns, designs


def solve(patterns: list[str], designs: list[str]) -> int:
    craftable_patterns = [is_craftable(design, patterns) for design in designs]
    return sum(craftable_patterns)


def is_craftable(design: str, patterns: list[str]) -> bool:
    queue = []
    queue.append(design)

    while queue:
        d = queue.pop()

        if len(d) == 0:
            return True

        for pattern in patterns:
            if pattern == d[: len(pattern)]:
                queue.append(d[len(pattern) :])

    return False


if __name__ == "__main__":
    patterns, designs = parse_input(Path("inputs/day19.txt"))
    print("Result1:", solve(patterns, designs))
