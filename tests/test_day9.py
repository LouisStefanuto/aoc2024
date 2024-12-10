import pytest

from aoc2024.day9 import Disk, checksum


class TestsDisk:
    def test_init(self):
        disk = Disk("12345")
        assert disk.state == "12345"
        assert disk.processed == [1, 2, 3, 4, 5]

    def test_encode_case1(self):
        disk = Disk("12345")
        assert disk.encode() == [str(x) for x in "0..111....22222"]

    def test_encode_case2(self):
        disk = Disk("121212")
        assert disk.encode() == [str(x) for x in "0..1..2.."]

    def test_compact(self):
        disk = Disk("12345")
        assert disk.compact() == [str(x) for x in "022111222......"]


def test_checksum():
    numbers = [1, 2, 3, 4, 5]
    expected = 0 + 2 + 6 + 12 + 20
    assert checksum(numbers) == expected


if __name__ == "__main__":
    pytest.main()
