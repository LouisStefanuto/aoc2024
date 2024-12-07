from pathlib import Path

from aoc2024.day4 import read_file_to_list


def split_orders_updates(lines: list[str]) -> tuple[list[str], list[str]]:
    for i, line in enumerate(lines):
        if line == "":
            return lines[:i], lines[i + 1 :]
    raise ValueError("Should contain a '' line.")


def split_order(order_string: str) -> tuple[int, int]:
    a, b = order_string.split("|")
    return int(a), int(b)


def split_update(update: str) -> list[int]:
    return list(int(x) for x in update.split(","))


def build_order_dict(orders: list[str]) -> dict[int, list[int]]:
    order_dict: dict[int, list[int]] = {}
    for order in orders:
        a, b = split_order(order)
        order_dict[a] = order_dict.get(a, []) + [b]
    return order_dict


def is_valid_update(update: list[int], order_dict: dict[int, list[int]]) -> bool:
    pages_seen: set[int] = set()

    for page in update:
        pages_after = set(order_dict.get(page, []))

        for page_seen in pages_seen:
            if page_seen in pages_after:
                return False
        pages_seen.add(page)

    return True


def get_updates_status(
    updates: list[list[int]], order_dict: dict[int, list[int]]
) -> tuple[list[int], list[int]]:
    bool_list = [is_valid_update(update, order_dict) for update in updates]
    true_indices = [i for i, val in enumerate(bool_list) if val]
    false_indices = [i for i, val in enumerate(bool_list) if not val]
    return true_indices, false_indices


def get_middle_page(update: list[int]) -> int:
    return update[len(update) // 2]


def sum_middle_pages(valid_updates: list[list[int]]) -> int:
    counter = 0
    for update in valid_updates:
        counter += get_middle_page(update)

    return counter


if __name__ == "__main__":
    data = read_file_to_list(Path("inputs/day5.txt"))
    orders, updates_str = split_orders_updates(data)
    updates = [split_update(update) for update in updates_str]
    order_dict = build_order_dict(orders)

    true_indices, false_indices = get_updates_status(updates, order_dict)
    valid_updates = [updates[i] for i in true_indices]
    false_updates = [updates[i] for i in false_indices]

    result1 = sum_middle_pages(valid_updates)
    print("Part1:", result1)

    result2 = 0
    print(order_dict)
    print("Part2:", result2)
