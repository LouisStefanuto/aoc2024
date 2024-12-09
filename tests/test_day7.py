import pytest

from aoc2024.day7 import Equation, solution1, split_line


def test_equation():
    equation = Equation(11111, [111, 222, 333])
    assert equation.result == 11111
    assert equation.numbers == [111, 222, 333]


def test_equation_compute_operation():
    equation = Equation(11111, [111, 222, 333])
    assert equation.compute_operation(["+", "+"]) == 666


def test_equation_list_operations():
    equation = Equation(11111, [111, 222, 333])
    expected = [
        ["+", "+"],
        ["+", "*"],
        ["*", "+"],
        ["*", "*"],
    ]

    assert equation.list_operations() == expected


def test_equation_list_operations_2():
    equation = Equation(11111, [111, 222, 333, 444])
    expected = [
        ["+", "+", "+"],
        ["+", "+", "*"],
        ["+", "*", "+"],
        ["+", "*", "*"],
        ["*", "+", "+"],
        ["*", "+", "*"],
        ["*", "*", "+"],
        ["*", "*", "*"],
    ]
    print(equation.list_operations())
    assert equation.list_operations() == expected


def test_equation_has_solution_true():
    equation = Equation(66, [11, 22, 33])
    assert equation.has_solution() is True

    equation = Equation(18, [1, 2, 9])
    assert equation.has_solution() is True

    equation = Equation(35, [1, 4, 7])
    assert equation.has_solution() is True


def test_equation_has_solution_false():
    equation = Equation(99, [11, 22, 33])
    assert equation.has_solution() is False


def test_split_line():
    line = "3267: 81 40 27"
    assert split_line(line) == Equation(3267, [81, 40, 27])


def test_solution1():
    equations = [
        Equation(66, [11, 22, 33]),  # True
        Equation(18, [1, 2, 9]),  # True
        Equation(111111, [1, 2, 9]),  # False
    ]

    assert solution1(equations) == 66 + 18


if __name__ == "__main__":
    pytest.main()
