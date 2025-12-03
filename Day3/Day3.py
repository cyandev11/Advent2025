import textwrap


# split the ranges, then for each range, check if there are invalid ids
def part1(moves):
    total_joltage = 0
    for move in moves:
        # split all the batteries
        split_batteries = textwrap.wrap(move, 1)
        for i, battery in enumerate(split_batteries):
            split_batteries[i] = int(split_batteries[i])

        print(split_batteries)
        # find the max values and their indexes
        max1_value = max(split_batteries)
        max1_index = split_batteries.index(max1_value)

        joltage = 0
        # account for the last index
        if max1_value == split_batteries[-1]:
            max2_value = max(split_batteries[:-1])
            joltage = int(str(max2_value) + str(max1_value))
        # if not the last index
        # then the second value is the max value from then onwards
        else:
            max2_value = max(split_batteries[max1_index+1:])
            joltage = int(str(max1_value) + str(max2_value))
        # add joltage
        total_joltage += joltage
    return total_joltage



# Opens a file and splits lines into inputs
def open_file(filename):
    # opens file and returns all strings
    with open(filename, "r") as file_input:
        input = file_input.read()
        list_of_values = input.split("\n")
        return list_of_values


inputs = open_file("Day3/Day3Input.txt")
print(part1(inputs))
