import pytest

from part2 import find_fewest_cubes_game_set


def test_find_fewest_cubes_game_set(sample_game_set_list):

    assert find_fewest_cubes_game_set('blue', sample_game_set_list) == 1
    assert find_fewest_cubes_game_set('green', sample_game_set_list) == 3
    assert find_fewest_cubes_game_set('red', sample_game_set_list) == 2


def test_find_fewest_cubes_game_set_all_zeroes(sample_game_set_list_all_zeroes):

    for colour in {'red', 'green', 'blue'}:

        assert find_fewest_cubes_game_set(
            colour, sample_game_set_list_all_zeroes) == 0


def test_find_fewest_cubes_game_set_invalid_colour(sample_game_set_list):

    assert find_fewest_cubes_game_set('yellow', sample_game_set_list) is None
