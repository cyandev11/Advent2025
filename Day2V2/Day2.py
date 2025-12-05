import textwrap
import re


def regex_solution(moves):
    part1 = 0
    part2 = 0
    for move in moves:
        ranges = move.split("-")
        lower_range = int(ranges[0])
        higher_range = int(ranges[1])
        while lower_range <= higher_range:
            # a hit with digits of any length at the start 
            # followed with a single back refrences that must end at the end 
            match1 = re.search(r"(^\d+)(\1$)", str(lower_range))
            # a hit with digits of any length at the start 
            # followed with any amount of back refrences that must continue to the end 
            match2 = re.search(r"(^\d+)(\1+$)", str(lower_range))

            # add invalid ids to sums
            if match1 is not None: part1 += int(match1.group(0))
            if match2 is not None: part2 += int(match2.group(0))
            lower_range += 1
    return part1, part2


# Opens a file and splits lines into inputs
def open_file(filename):
    # opens file and returns all strings
    with open(filename, "r") as file_input:
        input = file_input.read()
        list_of_values = input.split(",")
        return list_of_values


inputs = open_file("Day2V2/Day2Input.txt")
print(regex_solution(inputs))
