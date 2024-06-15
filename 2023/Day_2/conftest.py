"""Conftest file for Day 2 of Advent of Code 2023."""

import pytest


@pytest.fixture
def initial_sample_game_id1():
    return "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"


@pytest.fixture
def initial_sample_game_id2_no_red():
    return "Game 2: 1 blue; 4 green, 5 blue; 3 blue, 11 green; 10 green, 4 blue; 12 green, 7 blue; 3 blue, 19 green"


@pytest.fixture
def sample_game_set():
    return "1 blue, 4 green, 6 red"


@pytest.fixture
def sample_game_set_list():
    return [{'blue': 1, 'red': 2, 'green': 3}, {'blue': 0, 'red': 1, 'green': 2}, {'blue': 1, 'green': 1, 'red': 0}]


@pytest.fixture
def sample_game_set_list_all_zeroes():
    return [{'blue': 0, 'green': 0, 'red': 0}]
