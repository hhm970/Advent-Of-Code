"""Test file for part2.py"""

import pytest

from part2 import extract_first_digit, extract_last_digit


def test_nonumericdigits():
    assert extract_first_digit("eighttwotthree") == "8"

    assert extract_last_digit("eighttwothree") == "3"


def test_mix1():
    assert extract_first_digit("two1nine") == "2"

    assert extract_last_digit("two1nine") == "9"


def test_mix2():
    assert extract_first_digit("abcone2threexyz") == "1"

    assert extract_last_digit("abcone2threexyz") == "3"
