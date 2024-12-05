from pathlib import Path

import numpy as np


def read_file_to_list(file_path: Path):
    """
    Reads a text file and stores its content in a list.

    Parameters:
        file_path (str): The path to the text file.

    Returns:
        list: A list where each element is a line from the file.
    """
    content_list = []
    try:
        with open(file_path, "r") as file:
            # Read lines and strip newline characters
            content_list = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")

    return content_list


def collate_letters(letters: list[str]) -> str:
    return "".join(letters)


def convert_to_matrix(data: list[str]) -> np.array:
    return np.array([list(string) for string in data])


def count_row(row: str, target) -> int:
    counter = 0
    N = len(target)

    for i in range(len(row) - N + 1):
        if row[i : i + N] == target:
            counter += 1

    return counter


def count_row_double_sens(row: str, target) -> int:
    return count_row(row, target) + count_row(row[::-1], target)


def extract_all_diagonals(matrix: np.array) -> list[list[str]]:
    """
    Extracts all diagonals (main and anti-diagonals) from an NxN NumPy array.

    Parameters:
        matrix (np.ndarray): An NxN NumPy array.

    Returns:
        list: A list of diagonals, each represented as a list of elements.
    """
    n = matrix.shape[0]
    diagonals = []

    # Extract all main diagonals (top-left to bottom-right)
    for offset in range(-n + 1, n):
        diagonals.append(np.diag(matrix, k=offset).tolist())

    # Extract all anti-diagonals (top-right to bottom-left)
    flipped_matrix = np.fliplr(matrix)
    for offset in range(-n + 1, n):
        diagonals.append(np.diag(flipped_matrix, k=offset).tolist())

    return diagonals


def count_matrix(matrix: np.array, target: str = "XMAS") -> int:
    N, M = matrix.shape
    counter = 0

    # Rows
    for i in range(N):
        row = collate_letters(list(matrix[i, :]))
        counter += count_row_double_sens(row, target)

    # Columns
    for j in range(M):
        col = collate_letters(list(matrix[:, j]))
        counter += count_row_double_sens(col, target)

    # Diagonals
    diagonals = extract_all_diagonals(matrix)
    for diagonal in diagonals:
        diagonal_string = collate_letters(diagonal)
        counter += count_row_double_sens(diagonal_string, target)

    return counter


def is_valid_diag(diag: list, target: list[str]) -> bool:
    return diag == target or diag[::-1] == target


def is_valid_x(matrix: np.array, target: list[str]) -> bool:
    diag = [matrix[0, 0], matrix[1, 1], matrix[2, 2]]
    anti_diag = [matrix[2, 0], matrix[1, 1], matrix[0, 2]]
    return is_valid_diag(diag, target) and is_valid_diag(anti_diag, target)


def count_x_matrix(matrix: np.array, target: list[str] = ["M", "A", "S"]) -> int:
    counter = 0
    N, M = matrix.shape

    for i in range(N - 2):
        for j in range(M - 2):
            sub_matrix = matrix[i : i + 3, j : j + 3]
            print(sub_matrix)
            if is_valid_x(sub_matrix, target):
                counter += 1

    return counter


if __name__ == "__main__":
    data = read_file_to_list(Path("inputs/day4.txt"))
    matrix = convert_to_matrix(data)
    print(matrix.shape)

    result = count_matrix(matrix)
    print(result)

    result = count_x_matrix(matrix)
    print(result)
