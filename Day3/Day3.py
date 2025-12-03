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


# seperate the last parts for the guarenteed end part
# keep finding the maximum digit of the left side
# when the amount of batteries to switch are eqaul to the number of batteries at the end
# add the batteries at the end to the on switches
def find_highest_joltage(bank, desired_length):
    # highest digits
    highest_digits = []
    original_desired_length = desired_length

    # while the length of the bank is greater than necessary number of switches
    while len(bank) > (desired_length) and desired_length > 0:
        # cut amount of digits left by 1
        desired_length -= 1
        # find that digit to find in the area before the renaububg
        area_for_digit = bank[: (len(bank) - desired_length)]
        digit = max(area_for_digit)
        index_digit = bank.index(digit)
        highest_digits.append(digit)
        bank = bank[(index_digit + 1) :]

    # if the switches are not the size desired
    # add the rest of the bank in becuase the bank will complete the size
    if len(highest_digits) != original_desired_length:
        highest_digits = highest_digits + bank

    # join for final voltage
    joltage = "".join(str(battery) for battery in highest_digits)
    joltage = int(joltage)
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
