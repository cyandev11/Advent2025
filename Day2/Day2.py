import textwrap

# split the ranges, then for each range, check if there are invalid ids
def part1(moves):
    total_invalid_ids = 0
    for move in moves:
        ranges = move.split("-")
        lower_range = ranges[0]
        higher_range = ranges[1]
        total_invalid_ids += check_invalid(int(lower_range), int(higher_range))
    return total_invalid_ids

def part2(moves):
    total_invalid_ids = 0
    for move in moves:
        ranges = move.split("-")
        lower_range = ranges[0]
        higher_range = ranges[1]
        total_invalid_ids += check_invalid2(int(lower_range), int(higher_range))
    return total_invalid_ids

# going through every number in the range, check if the number is invalid
def check_invalid(lower, higher):
    total_invalid = 0
    while lower <= higher:
        # if both halves are equal to each other, it is invalid and can be added to total
        is_invalid = check_halfs(lower)
        if is_invalid:
            total_invalid += lower
        lower += 1
    return total_invalid

def check_invalid2(lower, higher):
    total_invalid = 0
    while lower <= higher:
        # if both halves are equal to each other, it is invalid and can be added to total
        is_invalid = check_repitions(lower)
        if is_invalid:
            total_invalid += lower
        lower += 1
    return total_invalid

# logic for checking halfs with flooring to ensure only checking even length numbers
def check_halfs(id):
    half_len = len(str(id)) // 2
    return str(id)[:half_len] == str(id)[half_len:]

# logic for checking repeition in general
def check_repitions(id):
    # find the ways ids can be split evenly with factors
    factors = []
    length = len(str(id))
    for i in range(length):
        i += 1
        if length % (i) == 0:
            factors.append(i)

    # remove multiple of 1s
    factors.remove(length)
    factors.remove(1)

    # split id's into even parts
    for factor in factors:
        # split the id into different possible lengths based on factors
        split_id = textwrap.wrap(str(id), factor)
        # remove dupes
        split_id = list(set(split_id))

        # if there's only one element, there is a pattern
        if len(split_id) == 1:
            return True

    return False


# Opens a file and splits lines into inputs
def open_file(filename):
    # opens file and returns all strings
    with open(filename, "r") as file_input:
        input = file_input.read()
        list_of_values = input.split(",")
        return list_of_values


inputs = open_file("Day2Input.txt")
print(inputs)
print(part1(inputs))
print(part2(inputs))
