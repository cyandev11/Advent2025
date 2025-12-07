import numpy
import textwrap


def part1(map):
    total_splits = 0
    # sends beams down
    for r, row in enumerate(map[:-1]):
        for c, col in enumerate(row):
            current_symbol = map[r][c]
            if current_symbol == "S":
                map[r + 1][c] = "|"
            elif current_symbol == "|" and map[r + 1][c] == "^":
                map[r + 1][c - 1] = "|"
                map[r + 1][c + 1] = "|"
                total_splits += 1
            elif current_symbol == "|" and map[r + 1][c] == ".":
                map[r + 1][c] = "|"
        # print_2d_array(map) # for animation
    return total_splits


def part2(map):
    total_beams = 0
    # sends beams down
    for r, row in enumerate(map[:-1]):
        for c, col in enumerate(row):
            current_symbol = map[r][c]
            if current_symbol == "S":
                map[r + 1][c] = "|"
            elif current_symbol == "|" and map[r + 1][c] == "^":
                map[r + 1][c - 1] = "|"
                map[r + 1][c + 1] = "|"
                total_beams += 0
            elif current_symbol == "|" and map[r + 1][c] == ".":
                map[r + 1][c] = "|"
        # print_2d_array(map)  # for animation

    return 0


# Opens a file and splits lines into inputs
def open_file(filename):
    # opens file and returns all strings
    with open(filename, "r") as file_input:
        input = file_input.read()
        map = []
        rows = input.split("\n")
        for row in rows:
            map.append(textwrap.wrap(row, 1))
        return map


def print_2d_array(array):
    for row in array:
        for col in row:
            print(col, end="")
        print()


inputs = open_file("Day7/Day7Input.txt")
print(part1(inputs))
print(part2(inputs))
