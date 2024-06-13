"""Solution for Day 1, Part 2 of Advent of Code 2023."""

NUMBER_TEXT_TO_NUMERIC = {"one": "1", "two": "2", "three": "3",
                          "four": "4", "five": "5", "six": "6",
                          "seven": "7", "eight": "8", "nine": "9",
                          "zero": "0"}


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
        elif check_for_num_text(True, line[i:]) is not None:
            return check_for_num_text(True, line[i:])


def extract_last_digit(line: str) -> str:
    """Given a string of alphanumeric characters, returns the last 
    numeric character."""

    n = len(line)

    for i in range(n, 0, -1):
        if line[i - 1].isnumeric():
            return line[i - 1]
        elif check_for_num_text(False, line[:i]) is not None:
            return check_for_num_text(False, line[:i])


def check_for_num_text(direction: bool, line_extract: str) -> str:
    """Given a direction - True for extracting first digit and False for extracting
    last digit - as well as the line index, outputs an integer from 0 to 9, if its
    text name is found in the string, and None otherwise."""

    print(f"Currently in check_num_for_text for line extract: {line_extract}")

    result = ""

    line_character_count = 0

    if not direction:

        line_extract_rev = line_extract[::-1]

        for character in line_extract_rev:

            possible_number_characters = [a[::-1][line_character_count]
                                          for a in NUMBER_TEXT_TO_NUMERIC.keys()
                                          if len(a) >= line_character_count + 1]

            if character in possible_number_characters:
                line_character_count += 1
                result = character + result

            else:
                return None

            result_int = NUMBER_TEXT_TO_NUMERIC.get(result)

            if result_int is not None:
                return result_int

    else:

        for character in line_extract:

            possible_number_characters = [a[line_character_count]
                                          for a in NUMBER_TEXT_TO_NUMERIC.keys()
                                          if len(a) >= line_character_count + 1]

            if character in possible_number_characters:
                line_character_count += 1
                result += character

            else:
                return None

            if result in NUMBER_TEXT_TO_NUMERIC.keys():
                return NUMBER_TEXT_TO_NUMERIC.get(result)


if __name__ == "__main__":

    all_lines = get_lines_txt_file()

    total = 0

    for line in all_lines:

        input_line = line.strip()

        output_digits = extract_first_digit(
            input_line) + extract_last_digit(input_line)

        total += int(output_digits)

    print(total)
