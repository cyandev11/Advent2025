import textwrap
import re


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
            if int(lower) <= int(ingredient) <= int(higher) and found == False:
                # found gets set to true so there are no repeats and we count it as fresh
                found = True
                num_fresh += 1

    return num_fresh


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
