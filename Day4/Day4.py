import textwrap
import time

# this function returns a new list with x values to replace valid @ toilet papers
def part1(moves):
    # create frame of # around maze
    width_maze = len(moves[0])
    new_maze = []
    new_maze.append(["#"] * (width_maze + 2))
    for move in moves:
        new_maze.append(["#"] + move + ["#"])
    new_maze.append(["#"] * (width_maze + 2))

    # for every @ check around it
    indexs_to_change = []
    for r, row in enumerate(new_maze):
        for c, col in enumerate(new_maze[0]):
            if new_maze[r][c] == "@":
                # these are the adjacent values, no index error since we can only ever get execute on a @ on the interior
                adjacents = [
                    new_maze[r - 1][c - 1],
                    new_maze[r - 1][c + 0],
                    new_maze[r - 1][c + 1],
                    new_maze[r + 0][c - 1],
                    new_maze[r + 0][c + 1],
                    new_maze[r + 1][c - 1],
                    new_maze[r + 1][c + 0],
                    new_maze[r + 1][c + 1],
                ]
                accessible = adjacents.count("@")

                # see if valid
                if accessible < 4:
                    indexs_to_change.append((r, c))

    # change list
    for indexs in indexs_to_change:
        new_maze[indexs[0]][indexs[1]] = "x"

    # remove frame
    new_maze = new_maze[1:-1]
    for r, row in enumerate(new_maze):
        new_maze[r].pop(0)
        new_maze[r].pop()

    return new_maze


def part2(maze):
    total_rolls = 0
    # set initial new maze through part 1
    new_maze = part1(maze)
    # while the old maze is not equal to the new maze (old maze that goes through part 1)
    while maze != new_maze:
        # set the old maze to the new maze
        total_rolls += count_x(new_maze)
        new_maze = turn_x_period(new_maze)
        maze = new_maze
        # keep setting new maze to a new round of part 1 until it doesnt change
        # so old maze = new maze
        new_maze = part1(maze)

    return total_rolls

def turn_x_period(maze):
    for r, row in enumerate(maze):
        for c, col in enumerate(maze):
            if maze[r][c] == "x":
                maze[r][c] = "."
    return maze

def count_x(maze):
    rolls_of_accessed_paper = 0
    for row in maze:
        rolls_of_accessed_paper += row.count("x")
    return rolls_of_accessed_paper

# Opens a file and splits lines into inputs
def open_file(filename):
    # opens file and returns all strings
    with open(filename, "r") as file_input:
        input = file_input.read()
        list_of_values = input.split("\n")
        return list_of_values


def print_maze(maze):
    for i in range(10):
        print()
    for row in maze:
        joined_row = "".join(row)
        print(joined_row)
    time.sleep(1)
    
def visualization(maze):
    total_rolls = 0
    # set initial new maze through part 1
    print(maze)
    new_maze = part1(maze)
    print_maze(new_maze)

    # while the old maze is not equal to the new maze (old maze that goes through part 1)
    while maze != new_maze:
        # set the old maze to the new maze
        total_rolls += count_x(new_maze)
        new_maze = turn_x_period(new_maze)
        maze = new_maze
        print_maze(maze)
        # keep setting new maze to a new round of part 1 until it doesnt change
        # so old maze = new maze
        new_maze = part1(maze)
        print_maze(new_maze)

    return total_rolls

inputs = open_file("Day4/Day4Input.txt")
# split rows into individual elemnts
for i, row in enumerate(inputs):
    inputs[i] = [char for char in row]


# find x's of part 1
part_1_maze = part1(inputs)
print(count_x(part_1_maze))


# find x's of part 2
print(part2(inputs))

# visualization
print_maze(inputs)
visualization(inputs)