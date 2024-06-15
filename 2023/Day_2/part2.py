"""Solution for Day 2, Part 2 of Advent of Code 2023."""


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
    with a, b, c being non-negative integers.
    """
    result = dict()

    game_id = get_game_id(game_line)

    result[game_id] = get_game_sets(game_line)

    return result


def find_fewest_cubes_game_set(colour: str, input_sets_list: list[dict[str]]) -> int:
    """Given a list of game sets, and a specified colour, returns the fewest
    amount of cubes of that colour in order for each game set to be playable.
    Return None if colour is not in ['blue', 'red', 'green']."""

    if colour not in {'blue', 'red', 'green'}:
        return None

    max_amount = input_sets_list[0][colour]

    for game_set in input_sets_list[1:]:

        if game_set[colour] > max_amount:

            max_amount = game_set[colour]

    return max_amount


if __name__ == "__main__":

    all_lines = get_lines_txt_file()

    total = 0

    for line in all_lines:

        input_line = line.strip()

        input_line_dict = convert_line_to_rgb_dict(input_line)

        line_game_id = list(input_line_dict.keys())[0]

        line_game_sets = list(input_line_dict.values())[0]

        product = 1

        for color in {'red', 'green', 'blue'}:

            product *= find_fewest_cubes_game_set(color, line_game_sets)

        total += product

    print(total)
