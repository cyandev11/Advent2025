import textwrap


# split the ranges, then for each range, check if there are invalid ids
def part1(moves):
    total_joltage = 0
    for move in moves:
        # split all the batteries
        split_batteries = textwrap.wrap(move, 1)
        for i, battery in enumerate(split_batteries):
            split_batteries[i] = int(split_batteries[i])

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
            max2_value = max(split_batteries[max1_index + 1 :])
            joltage = int(str(max1_value) + str(max2_value))
        # add joltage
        total_joltage += joltage
    return total_joltage


def part2(moves):
    total_joltage = 0
    for move in moves:
        # split all the batteries
        split_batteries = textwrap.wrap(move, 1)
        for i, battery in enumerate(split_batteries):
            split_batteries[i] = int(split_batteries[i])

        # find joltage
        joltage = find_highest_joltage(split_batteries, 12)
        total_joltage += joltage
    return total_joltage


# find the first starting digit, depending on how long we want our batteies to be
# then cut out the lowest batteries from the batteries after the first digit until desired length
# finally add the first digit and the maximum batteries in the desired length - 1 togeter
# to get the final joltage
# i can adapt part 1 easily with desired_length 2
def find_highest_joltage(bank, desired_length):
    # if the bank is shorter than the desired length, then just return bank
    # unnessary part
    if len(bank) < desired_length:
        joltage = "".join(str(battery) for battery in bank)
        joltage = int(joltage)
        return joltage

    # find the starting digit, this is most important
    area_for_first_digit = bank[: (len(bank) - desired_length)]
    first_digit = max(area_for_first_digit)
    index_first_digit = 0
    # its important to find the value of the last index
    for i, digit in enumerate(area_for_first_digit):
        if first_digit == digit:
            index_first_digit = i
    print(first_digit, index_first_digit)
    # find the rest of the higest batteries
    # then add back in the first digit
    area_for_batteries = bank[(index_first_digit + 1) :]

    while len(area_for_batteries) > (desired_length - 1):
        area_for_batteries.remove(min(area_for_batteries))
    area_for_batteries.insert(0, first_digit)
    
    print(area_for_batteries)

    # join for final voltage
    joltage = "".join(str(battery) for battery in area_for_batteries)
    joltage = int(joltage)
    print(joltage)
    return joltage


# Opens a file and splits lines into inputs
def open_file(filename):
    # opens file and returns all strings
    with open(filename, "r") as file_input:
        input = file_input.read()
        list_of_values = input.split("\n")
        return list_of_values


inputs = open_file("Day3/Day3Input.txt")
print(part1(inputs))
print(part2(inputs))
