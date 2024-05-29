"""Solution for Day 1 of Advent of Code 2023."""

def get_lines_txt_file() -> list[str]:
    """
    Given a .txt file with sample entries, returns a list, where
    each element is a line of the .txt file.
    """

    with open("sample.txt", "r") as f:
        result = f.readlines()
    
    return result


def extract_first_num_str(code: str) -> str:
    """Returns the first numeric character of the input string, or the first
    text string of a given numeric character from 0 to 9 inclusive."""

    num_text_list = []

    num_dict = {"one": "1", "two": "2", "three": "3", 
                "four": "4", "five": "5", "six": "6", 
                "seven": "7", "eight": "8", "nine": "9", 
                "zero": "0"}
    
    for i in code:
        if i.isnumeric():
            result = i
            return result
        else:
            num_text_list.append(i)
            num_text = "".join(num_text_list)
            if num_text in num_dict.keys():
                result = num_dict[num_text]
                return result



def extract_last_num_str(code: str) -> str:
    """Returns the first numeric character of the input string, or the first
    text string of a given numeric character from 0 to 9 inclusive."""

    num_text_list = []

    num_dict = {"one": "1", "two": "2", "three": "3", 
                "four": "4", "five": "5", "six": "6", 
                "seven": "7", "eight": "8", "nine": "9", 
                "zero": "0"}
    
    for i in code:
        if i.isnumeric():
            result = i
            return result
        else:
            num_text_list.append(i)
            num_text = "".join(num_text_list)[::-1]
            if num_text in num_dict.keys():
                result = num_dict[num_text]
                return result
            # else:
            #     for num_key in num_dict.keys():
            #         if num_text


def generate_num_list(code: str) -> list[str]:
    """
    Given a line of code with a mix of numeric and text characters, returns 
    a list of integers if the integer, or its text equivalent, appears in the 
    line of code.
    """

    result = [extract_first_num_str(code), extract_last_num_str(code[::-1])]

    return result



def get_first_last_digit_list(num_list: list[int]) -> int:
    """
    Given a line of code with a mix of numeric and text characters, returns
    the first and last numeric characters as an integer.
    """
    
    result = int("".join([num_list[0], num_list[-1]]))

    return result


if __name__ == "__main__":

    # all_lines = get_lines_txt_file()

    # total = 0

    # for line in all_lines:

    #     line_no_newline = line.strip("\n")

    #     print(line_no_newline)

    #     line_num_list = generate_num_list(line_no_newline)

    #     print(line_num_list)

    #     line_int = get_first_last_digit_list(line_num_list)

    #     print(line_int)

    #     total += line_int

    # print(total)

    input = "hnineeighttworhtvxdtxp8twoneh"

    print(extract_first_num_str(input))

    print(extract_first_num_str(input))