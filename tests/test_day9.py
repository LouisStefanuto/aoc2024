import pytest

from aoc2024.day9 import (
    Disk,
    DiskV2,
    File,
    FreeSpace,
    checksum,
    defragment,
    extract_numbers_str,
    fill,
)


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


class TestFile:
    def test_init(self):
        file = File(1000, 111, 999)
        assert file.start_idx == 1000
        assert file.size == 111
        assert file.value == 999


class TestFreeSpace:
    def test_init(self):
        free_space = FreeSpace(222, 333)
        assert free_space.start_idx == 222
        assert free_space.size == 333


class TestDiskV2:
    def test_init(self):
        disk = DiskV2("12345")
        assert disk.state == "12345"

    def test_create(self):
        disk = DiskV2("12345")
        result = disk.create()

        files = [
            File(start_idx=0, size=1, value=0),
            File(start_idx=3, size=3, value=1),
            File(start_idx=10, size=5, value=2),
        ]
        spaces = [FreeSpace(start_idx=1, size=2), FreeSpace(start_idx=6, size=4)]

        assert result == (files, spaces)


def test_fill():
    file = File(100, 10, 5)
    space = FreeSpace(0, 20)
    expected = (
        File(start_idx=0, size=10, value=5),  # the new file
        FreeSpace(start_idx=10, size=10),  # the space not filled by the files
        FreeSpace(start_idx=100, size=10),  # the space let by the file
    )
    assert fill(file, space) == expected


def test_defragment_case1():
    """Case where the free spaces are too small."""
    files = [
        File(start_idx=0, size=9, value=0),
        File(start_idx=10, size=9, value=1),
        File(start_idx=20, size=9, value=2),
    ]
    spaces = [FreeSpace(start_idx=9, size=1), FreeSpace(start_idx=19, size=1)]
    assert defragment(files, spaces) == (files, spaces)


def test_defragment_case2():
    # Input
    files = [
        File(start_idx=0, size=1, value=0),
        File(start_idx=3, size=1, value=1),
        File(start_idx=10, size=2, value=2),
    ]
    spaces = [FreeSpace(start_idx=1, size=2), FreeSpace(start_idx=6, size=4)]

    # Outputs
    expected_files = [
        File(start_idx=0, size=1, value=0),
        File(start_idx=3, size=1, value=1),
        File(start_idx=1, size=2, value=2),
    ]
    expected_spaces = [
        FreeSpace(start_idx=3, size=0),
        FreeSpace(start_idx=6, size=4),
        FreeSpace(start_idx=10, size=2),
    ]

    assert defragment(files, spaces) == (expected_files, expected_spaces)


def test_checksum():
    numbers = [1, 2, 3, 4, 5]
    expected = 0 + 2 + 6 + 12 + 20
    assert checksum(numbers) == expected


def test_extract_numbers_str_case1():
    data = "3322"
    disk2 = DiskV2(data)
    files, spaces = disk2.create()
    files, spaces = defragment(files, spaces)
    out = extract_numbers_str(files, spaces)
    assert out == ["0", "0", "0", "1", "1", ".", ".", ".", ".", "."]


def test_extract_numbers_str_case2():
    data = "2333133121414131402"
    disk2 = DiskV2(data)
    files, spaces = disk2.create()
    files, spaces = defragment(files, spaces)
    out = extract_numbers_str(files, spaces)
    expected = [str(x) for x in "00992111777.44.333....5555.6666.....8888.."]
    print(out)
    print(expected)
    assert out == expected


if __name__ == "__main__":
    pytest.main()
