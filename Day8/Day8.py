import math


def part1(inputs):
    while len(inputs > 0):
        shortest_points = solve_shortest_two_points(inputs)

    return 0

def solve_shortest_two_points(inputs):
    smallest_num = 10000000000000
    index_of_point1 = -1
    index_of_point2 = -1
    # find the smallest junction
    # for a list of cords
    # compare each coordinate to every other cordinate
    # keep track of which pair of coordinates results in the least distance
    for i, input in enumerate(inputs):
        for i2, input2 in enumerate(inputs):
            cords = inputs[i].split(",")
            cords2 = inputs[i2].split(",")
            x1 = int(cords[0])
            y1 = int(cords[1])
            z1 = int(cords[2])
            x2 = int(cords2[0])
            y2 = int(cords2[1])
            z2 = int(cords2[2])
            distance_3d = 10000000000000
            if i is not i2:
                distance_3d = solve_distance_3d(x1, x2, y1, y2, z1, z2)
            if distance_3d <= smallest_num:
                smallest_num = distance_3d
                index_of_point1 = i
                index_of_point2 = i2
    print(smallest_num, index_of_point1, index_of_point2)
    return (index_of_point1, index_of_point2)

# sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
def solve_distance_3d(x1, x2, y1, y2, z1, z2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def open_file(filename):
    # opens file and returns all strings
    with open(filename, "r") as file_input:
        input = file_input.read()
        input = input.split("\n")

        return input


inputs = open_file("Day8/Day8Input.txt")
print(part1(inputs))
print(solve_shortest_two_points(inputs))
