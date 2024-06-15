"""Tests for Day 2 Part 1 solution of Advent of Code 2023."""

import pytest

from part1 import (get_game_id, get_game_sets, convert_game_set_to_dict)


def test_get_game_id(initial_sample_game_id1, initial_sample_game_id2_no_red):

    assert isinstance(get_game_id(initial_sample_game_id1), int)
    assert isinstance(get_game_id(initial_sample_game_id2_no_red), int)
    assert get_game_id(initial_sample_game_id1) == 1
    assert get_game_id(initial_sample_game_id2_no_red) == 2


def test_get_game_sets_type(initial_sample_game_id1, initial_sample_game_id2_no_red):

    assert isinstance(get_game_sets(initial_sample_game_id1), list)
    assert isinstance(get_game_sets(initial_sample_game_id2_no_red), list)
    assert isinstance(get_game_sets(initial_sample_game_id1)[0], dict)
    assert isinstance(get_game_sets(initial_sample_game_id2_no_red)[0], dict)


def test_convert_game_set_to_dict(sample_game_set):

    assert isinstance(convert_game_set_to_dict(sample_game_set), dict)
    assert set(convert_game_set_to_dict(sample_game_set).keys()) == {
        "red", "blue", "green"}
    for i in convert_game_set_to_dict(sample_game_set).values():
        assert i >= 0
