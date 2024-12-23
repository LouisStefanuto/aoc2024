import pytest

from aoc2024.day17 import Game


def test_load():
    lines = [
        "Register A: 46323429",
        "Register B: 0",
        "Register C: 0",
        "",
        "Program: 2,4,1,1,7,5,1,5,4,3,0,3,5,5,3,0",
    ]

    game = Game(lines)

    assert game.a == 46323429
    assert game.b == 0
    assert game.c == 0
    assert game.program == [2, 4, 1, 1, 7, 5, 1, 5, 4, 3, 0, 3, 5, 5, 3, 0]


def test_run_case1():
    lines = [
        "Register A: 0",
        "Register B: 0",
        "Register C: 9",
        "",
        "Program: 2,6",
    ]

    game = Game(lines)
    game.run()
    assert game.b == 1


def test_run_case2():
    lines = [
        "Register A: 10",
        "Register B: 0",
        "Register C: 0",
        "",
        "Program: 5,0,5,1,5,4",
    ]

    game = Game(lines)
    assert game.run() == "0,1,2"


def test_run_case3():
    lines = [
        "Register A: 2024",
        "Register B: 0",
        "Register C: 0",
        "",
        "Program: 0,1",
    ]

    game = Game(lines)
    assert game.run() == ""
    assert game.a == 1012


def test_run_case4():
    lines = [
        "Register A: 0",
        "Register B: 29",
        "Register C: 0",
        "",
        "Program: 1,7",
    ]

    game = Game(lines)
    game.run()
    assert game.b == 26


def test_run_case5():
    lines = [
        "Register A: 0",
        "Register B: 2024",
        "Register C: 43690",
        "",
        "Program: 4,0",
    ]

    game = Game(lines)
    game.run()
    assert game.b == 44354


def test_run_case6():
    lines = [
        "Register A: 0",
        "Register B: 0",
        "Register C: 0",
        "",
        "Program: 3,0",
    ]

    game = Game(lines)
    assert game.run() == ""


def test_run_case7():
    lines = [
        "Register A: 1",
        "Register B: 0",
        "Register C: 0",
        "",
        "Program: 3,11",
    ]

    game = Game(lines)
    assert game.run() == ""
    assert game.pointer_instruction == 11


def test_run_case8():
    lines = [
        "Register A: 1",
        "Register B: 0",
        "Register C: 0",
        "",
        "Program: 3,3,0,5,0",
    ]

    game = Game(lines)
    assert game.run() == "0"


def test_run_case9():
    lines = [
        "Register A: 2024",
        "Register B: 0",
        "Register C: 0",
        "",
        "Program: 0,1,5,4",
    ]

    game = Game(lines)
    assert game.run() == "4"
    assert game.a == 1012


def test_run_case10():
    lines = [
        "Register A: 2024",
        "Register B: 0",
        "Register C: 0",
        "",
        "Program: 0,1,5,4,3,0",
    ]

    game = Game(lines)
    assert game.run() == "4,2,5,6,7,7,7,7,3,1,0"
    assert game.a == 0


if __name__ == "__main__":
    pytest.main()
