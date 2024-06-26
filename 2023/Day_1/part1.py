"""Solution for Day 1, Part 1 of Advent of Code 2023."""


def get_lines_txt_file() -> list[str]:
    """
    Given a .txt file with sample entries, returns a list, where
    each element is a line of the .txt file.
    """

    with open("sample.txt", "r") as f:
        result = f.readlines()

    return result


def extract_first_digit(line: str) -> str:
    """Given a string of alphanumeric characters, returns the first 
    numeric character."""

    n = len(line)

    for i in range(n):
        if line[i].isnumeric():
            return line[i]


def extract_last_digit(line: str) -> str:
    """Given a string of alphanumeric characters, returns the last 
    numeric character."""

    n = len(line)

    for i in range(n, 0, -1):
        if line[i - 1].isnumeric():
            return line[i - 1]


if __name__ == "__main__":

    all_lines = get_lines_txt_file()

    total = 0

    for line in all_lines:

        input_line = line.strip()

        output_digits = extract_first_digit(
            input_line) + extract_last_digit(input_line)

        total += int(output_digits)
