import textwrap
# pip install natsort
from natsort import natsorted


def part1(moves):
    num_fresh = 0
    ingredient_ids = moves[0]
    ingredient_check = moves[1]
    # for every ingredient we want to check
    for ingredient in ingredient_check:
        found = False
        # compare the ingredient against every range possible
        for id in ingredient_ids:
            range = id.split("-")
            lower = range[0]
            higher = range[1]
            # if the ingredient is bt in any range
            if int(lower) <= int(ingredient) <= int (higher) and found == False:
                # found gets set to true so there are no repeats and we count it as fresh
                found = True
                num_fresh += 1

    return num_fresh

def part2(moves):
    id_ranges = moves[0]
    sorted_id_ranges = natsorted(id_ranges)
    index = 0
    total = 0
    # now the ranges are naturally sorted according to lower end values, i can find
    while index < len(sorted_id_ranges) - 1:
        current_range = sorted_id_ranges[index]
        next_range = sorted_id_ranges[index + 1]
        
        can_merge = check_merge(current_range, next_range)
        if can_merge:
            new_merge = merge(current_range, next_range)
            sorted_id_ranges.insert(index, new_merge)
            sorted_id_ranges.remove(current_range)
            sorted_id_ranges.remove(next_range)
            sorted_id_ranges = natsorted(sorted_id_ranges)
            index = -1
        index += 1
    print(sorted_id_ranges)

    for id_range in sorted_id_ranges:
        total += check_diff(id_range)
    return total
    
def check_merge(range1, range2):
    # 2nd and 3rd num
    lower1 = int(range1.split("-")[0])
    higher1 = int(range1.split("-")[1])
    lower2 = int(range2.split("-")[0])
    higher2 = int(range2.split("-")[1])
    if higher1 >= lower2:
        return True

def merge(range1, range2):
    # 1st and 4th num
    lower1 = int(range1.split("-")[0])
    higher1 = int(range1.split("-")[1])
    lower2 = int(range2.split("-")[0])
    higher2 = int(range2.split("-")[1])
    new_range = str(min(lower1, lower2)) + "-" + str(max(higher1, higher2))
    return new_range

def check_diff(range):
    lower = range.split("-")[0]
    higher = range.split("-")[1]
    diff = int(higher) - int(lower) + 1
    return diff

# Opens a file and splits lines into inputs
def open_file(filename):
    # opens file and returns all strings
    with open(filename, "r") as file_input:
        input = file_input.read()
        # double new line seperates file into two
        list_of_values = input.split("\n\n")
        # return indiviudal lines from two parts as
        return list_of_values[0].split("\n"), list_of_values[1].split("\n")


# inputs is a tuple with ingredient ids and ingredients to check
inputs = open_file("Day5/Day5Input.txt")
print(part1(inputs))
print(part2(inputs))
