"""Conftest file for test files of Day 3 of Advent of Code 2023."""


import pytest


@pytest.fixture
def sample_line():
    return "234@£$789()()"


@pytest.fixture
def sample_line_all_periods():
    return "................."


@pytest.fixture
def sample_line_all_numbers():
    return "1233427349223482390479823"


@pytest.fixture
def sample_line_all_symbols():
    return "?!@£!££@$&£@(&*$*&£(*$&£*($@&(£@*$&))))"


@pytest.fixture
def sample_list():
    return ["467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598.."]


@pytest.fixture
def sample_list_all_periods():
    return ["..........",
            "..........",
            "..........",
            ".........."]


@pytest.fixture
def sample_list_no_symbols():
    return ["2342343242",
            "..9...12..",
            ".123..123.",
            "1.2.3.4.5."]


@pytest.fixture
def sample_list_no_numbers():
    return ["!@£$()[]..",
            ".....^^^..",
            ".***......",
            "...()()()."]
