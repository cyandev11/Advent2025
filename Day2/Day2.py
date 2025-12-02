import re

def part1(moves):
    total_invalid_ids = 0
    for move in moves:
        ranges = move.split("-")
        lower_range = ranges[0]
        higher_range = ranges[1]
        total_invalid_ids += check_invalid(int(lower_range), int(higher_range))
    return total_invalid_ids
        
def check_invalid(lower, higher):
    total_invalid = 0
    while lower <= higher:
        is_invalid = check_halfs(lower)
        if is_invalid:
            total_invalid += lower
        lower += 1
    return total_invalid

def check_halfs(id):
    half_len = len(str(id)) // 2
    return str(id)[:half_len] == str(id)[half_len:]


# Opens a file and splits lines into inputs
def open_file(filename):
    # opens file and returns all strings
    with open(filename, "r") as file_input:
        input = file_input.read()
        list_of_values = input.split(",")
        return list_of_values


inputs = open_file("Day2/Day2Input.txt")
print(inputs)
print(part1(inputs))
