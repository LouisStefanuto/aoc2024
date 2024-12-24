import pytest

from aoc2024.day19 import solve1, solve2


def test_solve1():
    patterns = ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]
    designs = ["brwrr", "bggr", "gbbr", "rrbgbr", "ubwu", "bwurrg", "brgr", "bbrgwb"]
    assert solve1(patterns, designs) == 6


def test_solve2():
    patterns = ("r", "wr", "b", "g", "bwu", "rb", "gb", "br")
    designs = ("brwrr", "bggr", "gbbr", "rrbgbr", "ubwu", "bwurrg", "brgr", "bbrgwb")
    assert solve2(patterns, designs) == 16


if __name__ == "__main__":
    pytest.main()
