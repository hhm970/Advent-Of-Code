"""Tests for solution of Day 3 Part 1 of Advent of Code 2023."""


import pytest

from part1 import get_indices_symbols, get_indices_numbers, get_numbers_adj_symbol


def test_get_indices_symbols_all_periods(sample_line_all_periods):
    assert get_indices_symbols(sample_line_all_periods) == []


def test_get_indices_symbols_all_numbers(sample_line_all_numbers):
    assert get_indices_symbols(sample_line_all_numbers) == []


def test_get_indices_symbols_all_symbols(sample_line_all_symbols):

    n = len(sample_line_all_symbols)

    assert get_indices_symbols(sample_line_all_symbols) == [
        i for i in range(n)]


def test_get_indices_symbols_success(sample_line):
    assert get_indices_symbols(sample_line) == [3, 4, 5, 9, 10, 11, 12]


def test_get_indices_numbers_all_periods(sample_line_all_periods):
    assert get_indices_numbers(sample_line_all_periods) == []


def test_get_indices_numbers_all_symbols(sample_line_all_symbols):
    assert get_indices_numbers(sample_line_all_symbols) == []


def test_get_indices_numbers_all_numbers(sample_line_all_numbers):

    n = len(sample_line_all_numbers)

    assert get_indices_numbers(sample_line_all_numbers) == [
        i for i in range(n)]


def test_get_indices_numbers_success(sample_line):
    assert get_indices_numbers(sample_line) == [0, 1, 2, 6, 7, 8]


def test_get_numbers_adj_symbol_all_periods(sample_list_all_periods):
    assert get_numbers_adj_symbol(sample_list_all_periods) == []


def test_get_numbers_adj_symbol_no_symbols(sample_list_no_symbols):
    assert get_numbers_adj_symbol(sample_list_no_symbols) == []


def test_get_numbers_adj_symbol_no_numbers(sample_list_no_numbers):
    assert get_numbers_adj_symbol(sample_list_no_numbers) == []


def test_get_numbers_adj_symbol_success(sample_list):
    assert get_indices_symbols(sample_list) == [467, 35, 633, 617,
                                                592, 755, 664, 598]
