from itertools import cycle


def part1(moves):
    current_dial = 50
    times_at_zero = 0
    for move in moves:
        num_of_pass = move_lock(current_dial, move)
        if num_of_pass > 0:
            times_at_zero += 1
    return times_at_zero

def part2(moves):
    current_dial = 50
    times_at_zero = 0
    for move in moves:
        current_dial = move_lock(current_dial, move)
        if current_dial == 0:
            times_at_zero += 1
    return times_at_zero

def move_lock(current_dial, move):
    direction = move[0]
    steps = int(move[1:])
    if direction == "R":
        current_dial += steps
    if direction == "L":
        current_dial -= steps

    number_of_passes = abs(current_dial // 100)
    current_dial = current_dial % 100

    if current_dial == 100:
        current_dial = 0
    if current_dial < 0:
        current_dial = 100 - abs(current_dial)
    if current_dial == 0:
        number_of_passes += 1

    return number_of_passes

def open_file(filename):
    # opens file and returns all strings
    with open(filename, "r") as file_input:
        input = file_input.read()
        list_of_values = input.split("\n")
        return list_of_values


inputs = open_file("Day1Input")
print(part1(inputs))