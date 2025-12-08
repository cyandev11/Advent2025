import math
from collections import Counter


def part1(inputs):
    total = 1
    connected_points = []
    pairs = []
    iteration = len(inputs)
    # finds every single pair of shortest points
    while iteration > 0:
        shortest_points = solve_shortest_two_points(inputs, connected_points)
        # make sure points are not the same
        if shortest_points[0] != shortest_points[1]:
            point1 = shortest_points[0]
            point2 = shortest_points[1]
            connected_points.append(point1)
            connected_points.append(point2)
            pairs.append([point1, point2])
        iteration -= 1

    # we now have connected_points a list of all the points connected to each other
    # and also pairs, which is connected points orgnaized
    # now time to link up all the points that are in common
    print(pairs)
    for i in range(3):
        # find the most common index for connections via connected points (mode)
        circuit = []
        most_common = Counter(connected_points).most_common(1)
        circuit.append(most_common[0][0])

        # add pairs until there are no connections
        index = 0
        while index < len(pairs):
            current_pair = pairs[index]
            if current_pair[0] in circuit or current_pair[1] in circuit:
                circuit.append(current_pair[0])
                circuit.append(current_pair[1])
                pairs.pop(index)
                index = -1 # index at -1 so we get reset to 0
            index += 1
        
        # now have the largest circuit
        circuit = set(circuit)
        total *= len(circuit)

        # update connected points
        new_connected_points = connected_points[:]
        for point in connected_points:
            if point in circuit:
                new_connected_points.remove(point)
        connected_points = new_connected_points

        print(circuit)

    return 0


def solve_shortest_two_points(inputs, connected_points):
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
            # makes sure it doesnt compare to itself
            # and doesnt compare any points already in a circuit
            if i is not i2 and (
                i not in connected_points or i2 not in connected_points
            ):
                distance_3d = solve_distance_3d(x1, x2, y1, y2, z1, z2)
            if distance_3d <= smallest_num:
                smallest_num = distance_3d
                index_of_point1 = i
                index_of_point2 = i2
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
