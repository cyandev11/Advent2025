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
    total_realities = 0
    # set all the beams and then set beams to 1
    for r, row in enumerate(map[:-1]):
        for c, col in enumerate(row):
            current_symbol = map[r][c]
            if current_symbol == "S":
                map[r + 1][c] = 1
            elif isinstance(current_symbol, int) and map[r + 1][c] == "^":
                map[r + 1][c - 1] = 1
                map[r + 1][c + 1] = 1
            elif isinstance(current_symbol, int) and map[r + 1][c] == ".":
                map[r + 1][c] = 1

    for r, row in enumerate(map):
        for c, col in enumerate(row):
            if map[r][c] == 1 and r != 0 and row != len(map) and c != 0 and c != len(row) - 1:
                new_num = 1
                left = map[r][c - 1]
                right = map[r][c + 1]
                above = map[(r - 1)][c]
                print(left, right, above)
                if left == "^" or right == "^" or isinstance(above, int):
                    new_num = 0

                if left == "^" and isinstance(map[r - 1][c - 1], int):
                    new_num += map[r - 1][c - 1]
                if right == "^" and isinstance(map[r - 1][c + 1], int):
                    new_num += map[r - 1][c + 1]
                if isinstance(above, int):
                    new_num += map[r - 1][c]
                map[r][c] = new_num
    for col in map[-1]:
        if isinstance(col, int):
            total_realities += col
    # print_2d_array(map)  # for animation

    return total_realities


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

inputs = open_file("Day7/Day7Input.txt")
print(part2(inputs))
