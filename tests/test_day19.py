import pytest

from aoc2024.day19 import solve


def test_solve():
    patterns = ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]
    designs = ["brwrr", "bggr", "gbbr", "rrbgbr", "ubwu", "bwurrg", "brgr", "bbrgwb"]
    assert solve(patterns, designs) == 6


if __name__ == "__main__":
    pytest.main()
