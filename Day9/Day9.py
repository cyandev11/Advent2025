import math
from collections import Counter


def solve_shortest_two_points(inputs):
    largest_area = 0
    for i, input in enumerate(inputs):
        for i2, input2 in enumerate(inputs):
            cords = inputs[i].split(",")
            cords2 = inputs[i2].split(",")
            col1 = int(cords[0])
            row1 = int(cords[1])
            col2 = int(cords2[0])
            row2 = int(cords2[1])
            # makes sure it doesnt compare to itself
            area = 0
            if i is not i2:
                print(cords, cords2)
                area = (max(col1, col2) - min(col1, col2) + 1) * (
                    max(row1, row2) - min(row1, row2) + 1
                )
            if area > largest_area:
                largest_area = area

    return largest_area


def open_file(filename):
    # opens file and returns all strings
    with open(filename, "r") as file_input:
        input = file_input.read()
        input = input.split("\n")

        return input


inputs = open_file("Day9/Day9Input.txt")
print(solve_shortest_two_points(inputs))
