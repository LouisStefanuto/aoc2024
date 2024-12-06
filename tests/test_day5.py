from aoc2024.day5 import (
    build_order_dict,
    get_middle_page,
    is_valid_update,
    split_order,
    split_orders_updates,
    split_update,
    sum_middle_pages,
)


def test_split_orders_updates():
    input = [
        "75|13",
        "53|13",
        "",
        "75,47,61,53,29",
        "97,61,53,29,1",
    ]
    expected = (
        [
            "75|13",
            "53|13",
        ],
        [
            "75,47,61,53,29",
            "97,61,53,29,1",
        ],
    )
    result = split_orders_updates(input)
    assert result == expected


def test_split_orders():
    assert split_order("3|178") == (3, 178)
    assert split_order("311|178") == (311, 178)


def test_split_update():
    assert split_update("41,42,99,65,12") == [41, 42, 99, 65, 12]


def test_build_order_dict():
    orders = ["75|13", "53|13"]
    result = build_order_dict(orders)
    expected = {75: [13], 53: [13]}

    assert result == expected


def test_is_valid_update():
    update = [75, 47, 61, 53, 29]
    order_dict = {
        75: [12, 12, 47],
        47: [61],
        53: [29],
    }
    assert is_valid_update(update, order_dict) is True


def test_is_not_valid_update():
    update = [75, 47, 61, 53, 29]
    order_dict = {
        75: [12, 12, 47],
        47: [61],
        53: [29, 61],
    }
    assert is_valid_update(update, order_dict) is False


def test_get_middle_page():
    assert get_middle_page([1]) == 1
    assert get_middle_page([1, 2, 3]) == 2
    assert get_middle_page([1, 2, 3, 4, 5]) == 3


def test_sum_middle_pages():
    assert sum_middle_pages([[1, 2, 3], [1, 2, 3]]) == 4
    assert sum_middle_pages([[1, 7, 3], [1, 2, 3, 6, 7]]) == 10
