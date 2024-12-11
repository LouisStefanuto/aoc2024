from dataclasses import dataclass
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


# Half2
# Convert the string state into two lists:
# - one for the files
# - one for the free spaces
#
# A free space has 2 fields:
# - a starting idx
# - a size
#
# A file has 3 fields
# - a starting index
# - a size
# - a value (its i-position // 2 in the original string state)
#
# Solution Algorithm
# -------------------
# For each file, in the descending order
#   i = 0
#   while space[i].start_idx < file.start_idx:
#       if space[i].size >= file.size:
#           update the file index -> file.start_idx = space[i].start_idx
#           update the empty space -> space[i].start_idx += file.size
#                                  -> space[i].size -= file.size
#           break
#       i += 1
#
# The lists are now updated -> convert back to string
# Then cumsum
# -------------------


@dataclass
class File:
    start_idx: int
    size: int
    value: int


@dataclass
class FreeSpace:
    start_idx: int
    size: int
    value: str = "."


def fill(file: File, space: FreeSpace) -> tuple[File, FreeSpace, FreeSpace]:
    if file.size > file.size:
        raise ValueError("The space is too small to fit the file inside.")

    replacement_space = FreeSpace(file.start_idx, file.size)

    tmp_start_idx = space.start_idx
    space.start_idx += file.size
    space.size = space.size - file.size
    file.start_idx = tmp_start_idx

    return file, space, replacement_space


class DiskV2:
    def __init__(self, state: str):
        self.state = state
        self.processed = [int(x) for x in state]

    def create(self) -> tuple[list[File], list[FreeSpace]]:
        files: list[File] = []
        spaces: list[FreeSpace] = []
        start_idx = 0

        for i, n in enumerate(self.processed):
            if i % 2 == 0:
                files.append(File(start_idx, n, i // 2))
            else:
                spaces.append(FreeSpace(start_idx, n))
            start_idx += n

        return files, spaces


def defragment(
    files: list[File], spaces: list[FreeSpace]
) -> tuple[list[File], list[FreeSpace]]:
    """
    Return the defragmented lists.

    Pseudo-code:

    For each file, in the descending order
      i = 0
      while spaces[i].start_idx < file.start_idx:
          if spaces[i].size >= file.size:
              update the file index -> file.start_idx = spaces[i].start_idx
              update the empty space -> spaces[i].start_idx += file.size
                                     -> spaces[i].size -= file.size
              break
          i += 1
    """

    for file in files[::-1]:
        i = 0
        while i < len(spaces) and spaces[i].start_idx < file.start_idx:
            if spaces[i].size >= file.size:
                # Swap, break and move to the next file
                file, spaces[i], replacement_space = fill(file, spaces[i])
                spaces.append(replacement_space)
                break
            i += 1

    return files, spaces


def extract_numbers_str(files: list[File], spaces: list[FreeSpace]) -> list[str]:
    concat = files + spaces
    concat.sort(key=lambda x: x.start_idx)

    out: list[str] = []
    for content in concat:
        out += [str(content.value)] * content.size

    return out


if __name__ == "__main__":
    data = read_file_to_list(Path("inputs/day9.txt"))[0]
    disk = Disk(data)
    code_compacted = disk.compact()
    result1 = checksum(code_compacted)
    print(f"Result1: {result1}")

    disk2 = DiskV2(data)
    files, spaces = disk2.create()
    files, spaces = defragment(files, spaces)
    code_compacted = extract_numbers_str(files, spaces)
    result2 = checksum(code_compacted)
    print(f"Result2: {result2}")
