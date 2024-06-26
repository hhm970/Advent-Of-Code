"""Solution for Day 3, Part 1 of Advent of Code 2023."""


def get_lines_txt_file() -> list[str]:
    """
    Given a .txt file with sample entries, returns a list, where
    each element is a line of the sample.txt file.
    """

    with open("sample.txt", "r") as f:
        result = f.readlines()

    return result


def get_indices_symbols(line: str) -> list[int]:
    """Given a line, returns a list of indices of elements which are not numeric,
    or a period ('.')."""

    n = len(line)

    result = []

    for i in range(n):
        if line[i] != "." and not line[i].isnumeric():
            result.append(i)

    return result


def get_indices_numbers(line: str) -> list[int]:
    """Given a line, return a list of indices of elements which are numeric."""

    n = len(line)

    result = [i for i in range(n) if line[i].isnumeric()]

    return result


def get_numbers_adj_symbol(line: str, above_line_indices: list[int] = [],
                           below_line_indices: list[int] = [],
                           current_line_indices: list[int] = []) -> list[int]:
    """Given a line, returns a list of integers which are adjacent to a symbol,
    both above and below (if applicable)."""
    pass


if __name__ == "__main__":

    all_lines = get_lines_txt_file()

    for line in all_lines:

        input_line = line.strip()
