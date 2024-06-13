"""Solution for Day 2, Part 1 of Advent of Code 2023."""


MIN_NUMBER_OF_RED = 12
MIN_NUMBER_OF_GREEN = 13
MIN_NUMBER_OF_BLUE = 14


def get_lines_txt_file() -> list[str]:
    """
    Given a .txt file with sample entries, returns a list, where
    each element is a line of the sample.txt file.
    """

    with open("sample.txt", "r") as f:
        result = f.readlines()

    return result


def get_game_id(game_line: str) -> int:
    """Given a game line, return its game id."""

    colon_index = game_line.index(":")

    return int(game_line[5: colon_index])


def get_game_sets(game_line: str) -> list[dict[str]]:
    """Given a game line, return the sets of cubes played in
    a game, where each set is represented as a dict object."""

    result = []

    colon_index = game_line.index(":")

    game_line_extract = game_line[colon_index + 2:]

    game_line_sets = game_line_extract.split("; ")

    for game_set in game_line_sets:

        result.append(convert_game_set_to_dict(game_set))

    return result


def convert_game_set_to_dict(input_set: str) -> dict:
    """Given a set where at most 3 type of cubes are pulled out, return a dict
    of the form

    {'red': int, 'green': int, 'blue': int}
    """

    colours = {"red", "green", "blue"}

    result = dict()

    input_set_coloursplit = input_set.split(", ")

    for turn in input_set_coloursplit:

        turn_split = turn.split()

        result[turn_split[1]] = int(turn_split[0])

        for i in colours:

            if result.get(i) is None:

                result[i] = 0

    return result


def convert_line_to_rgb_dict(game_line: str) -> dict[str]:
    """Given a line, representing a game with id X, returns a dict object 
    of the form

    {X: [{1st set}, {2nd set}, {3rd set}]}
    where each set is of the form 

    {'red': a, 'green': b, 'blue': c}
    with a, b, c being positive integers.
    """
    result = dict()

    game_id = get_game_id(game_line)

    result[game_id] = get_game_sets(game_line)

    return result


if __name__ == "__main__":

    all_lines = get_lines_txt_file()

    total = 0

    for line in all_lines:

        input_line = line.strip()

        input_line_dict = convert_line_to_rgb_dict(input_line)

        line_game_id = list(input_line_dict.keys())[0]

        line_game_sets = list(input_line_dict.values())[0]

        all_sets_possible = True

        for game_set in line_game_sets:

            if game_set.get('red') > MIN_NUMBER_OF_RED or game_set.get('green') > MIN_NUMBER_OF_GREEN or game_set.get('blue') > MIN_NUMBER_OF_BLUE:

                all_sets_possible = False

        if all_sets_possible:

            total += line_game_id

    print(total)
