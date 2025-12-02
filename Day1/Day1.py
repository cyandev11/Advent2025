from itertools import cycle


def part1(moves):
    current_dial = 50
    times_at_zero = 0
    for move in moves:
        current_dial = move_lock(current_dial, move)
        if current_dial == 0:
            times_at_zero += 1
    return times_at_zero

def part2(moves):
    current_dial = 50
    times_at_zero = 0
    for move in moves:
        direction = move[0]
        steps = int(move[1:])
        for i in range(steps):
            # move dial one by one
            if direction == "R":
                current_dial += 1
            if direction == "L":
                current_dial -= 1
            # adjust dials
            if current_dial == 100:
                current_dial = 0
            if current_dial < 0:
                current_dial = 100 - abs(current_dial)
            # if zero, add
            if current_dial == 0:
                times_at_zero += 1
    return times_at_zero




# moves lock according to direction
def move_lock(current_dial, move):
    # find direction and how many steps
    direction = move[0]
    steps = int(move[1:])

    if direction == "R":
        current_dial += steps
    if direction == "L":
        current_dial -= steps

    current_dial = current_dial % 100

    if current_dial == 100:
        current_dial = 0
    if current_dial < 0:
        current_dial = 100 - abs(current_dial)

    return current_dial


# Opens a file and splits lines into inputs
def open_file(filename):
    # opens file and returns all strings
    with open(filename, "r") as file_input:
        input = file_input.read()
        list_of_values = input.split("\n")
        return list_of_values


inputs = open_file("Day1/Day1Input.txt")
print(part1(inputs))
print(part2(inputs))