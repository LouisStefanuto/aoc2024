from dataclasses import dataclass
from pathlib import Path

import numpy as np

from aoc2024.day4 import convert_to_matrix, read_file_to_list


@dataclass
class Antenna:
    x: int
    y: int
    value: str

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.value))


class AntennaMap:
    def __init__(self, grid: np.ndarray):
        self.grid = grid

    def __repr__(self) -> str:
        grid_str = "\n".join("".join(row) for row in self.grid)
        return "\n" + grid_str + "\n"

    def list_antennas(self) -> list[Antenna]:
        positions_x, positions_y = np.where(self.grid != ".")
        antennas: list[Antenna] = []

        for x, y in zip(positions_x, positions_y):
            antenna = Antenna(int(x), int(y), str(self.grid[x, y]))
            antennas.append(antenna)

        return antennas


Position = tuple[int, int]


def compute_antinodes(antenna1: Antenna, antenna2: Antenna) -> list[Position]:
    if antenna1.value != antenna2.value:
        return []

    gap_x = antenna2.x - antenna1.x
    gap_y = antenna2.y - antenna1.y

    return [
        (antenna1.x - gap_x, antenna1.y - gap_y),
        (antenna2.x + gap_x, antenna2.y + gap_y),
    ]


def compute_all_antinodes(antennas: list[Antenna]) -> list[Position]:
    positions: list[Position] = []

    for i in range(len(antennas) - 1):
        for j in range(i + 1, len(antennas)):
            antenna1, antenna2 = antennas[i], antennas[j]
            if antenna1 != antenna2:
                positions += compute_antinodes(antenna1, antenna2)

    return positions


def solution1(antenna_map: AntennaMap) -> set[Position]:
    antennas = antenna_map.list_antennas()
    antinodes = compute_all_antinodes(antennas)

    N, M = antenna_map.grid.shape
    valid_antinodes: list[Position] = []
    for position in antinodes:
        x, y = position
        if 0 <= x and x < N and 0 <= y and y < M:
            valid_antinodes.append(position)

    # Only keep unique antinodes
    return set(valid_antinodes)


if __name__ == "__main__":
    data = read_file_to_list(Path("inputs/day8.txt"))
    grid = convert_to_matrix(data)
    terrain = AntennaMap(grid)
    print(terrain)

    result1 = solution1(terrain)
    print(f"Result1: {len(result1)}")
