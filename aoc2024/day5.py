"""
TODO
Would be better to use classes for the updates and for the OrderDict
"""

import logging
from pathlib import Path

from aoc2024.day4 import read_file_to_list

Update = list[int]
OrderDict = dict[int, list[int]]


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


def build_order_dict(orders: list[str]) -> OrderDict:
    order_dict: OrderDict = {}
    for order in orders:
        a, b = split_order(order)
        order_dict[a] = order_dict.get(a, []) + [b]
    return order_dict


def is_valid_update(update: Update, order_dict: OrderDict) -> bool:
    pages_seen: set[int] = set()

    for page in update:
        pages_after = set(order_dict.get(page, []))

        for page_seen in pages_seen:
            if page_seen in pages_after:
                return False
        pages_seen.add(page)

    return True


def get_updates_status(
    updates: list[Update], order_dict: OrderDict
) -> tuple[list[int], list[int]]:
    bool_list = [is_valid_update(update, order_dict) for update in updates]
    true_indices = [i for i, val in enumerate(bool_list) if val]
    false_indices = [i for i, val in enumerate(bool_list) if not val]
    return true_indices, false_indices


def get_middle_page(update: Update) -> int:
    return update[len(update) // 2]


def sum_middle_pages(valid_updates: list[Update]) -> int:
    counter = 0
    for update in valid_updates:
        counter += get_middle_page(update)

    return counter


def move_up_first_error(update: Update, order_dict: OrderDict) -> Update:
    pages_seen: set[int] = set()

    for i, page in enumerate(update):
        pages_after = set(order_dict.get(page, []))

        for page_seen in pages_seen:
            if page_seen in pages_after:
                # Swap page with the one before
                update[i], update[i - 1] = update[i - 1], update[i]
                return update
        pages_seen.add(page)

    logging.warning("No error found in this update.")
    return update


def order_update(update: Update, order_dict: OrderDict) -> Update:
    while not is_valid_update(update, order_dict):
        update = move_up_first_error(update, order_dict)
    return update


def fix_false_updates(updates: list[Update], order_dict: OrderDict) -> list[Update]:
    return [order_update(false_update, order_dict) for false_update in updates]


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
    fixed_updates = fix_false_updates(false_updates, order_dict)
    result2 = sum_middle_pages(fixed_updates)
    print("Part2:", result2)
