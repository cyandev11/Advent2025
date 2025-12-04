import textwrap


# split the ranges, then for each range, check if there are invalid ids
def part1(moves):
    # create frame of # around maze
    width_maze = len(moves[0])
    new_maze = []
    new_maze.append("#"*(width_maze + 2))
    for move in moves:
        new_maze.append("#" + move + "#")
    new_maze.append("#"*(width_maze + 2))

    # split rows into individual elemnts
    for i, row in enumerate(new_maze):
        new_maze[i] = [char for char in row]

    # for every @ check around it
    rolls_of_accessed_paper = 0
    indexs_to_change = []
    for r, row in enumerate(new_maze):
        for c, col in enumerate(new_maze[0]):
            if new_maze[r][c] == '@':
                # these are the adjacent values, no index error since we can only ever get execute on a @ on the interior
                adjacents = [ 
                    new_maze[r-1][c-1], new_maze[r-1][c+0], new_maze[r-1][c+1],
                    new_maze[r+0][c-1], new_maze[r+0][c+1],
                    new_maze[r+1][c-1], new_maze[r+1][c+0], new_maze[r+1][c+1],
                ]
                accessible = adjacents.count("@")

                # see if valid
                if (accessible < 4):
                    indexs_to_change.append((r,c))

    # change list
    for indexs in indexs_to_change:
        new_maze[indexs[0]][indexs[1]] = "x"

    # find x's
    for row in new_maze:
        rolls_of_accessed_paper += row.count("x")
        
    return rolls_of_accessed_paper





# Opens a file and splits lines into inputs
def open_file(filename):
    # opens file and returns all strings
    with open(filename, "r") as file_input:
        input = file_input.read()
        list_of_values = input.split("\n")
        return list_of_values

inputs = open_file("Day4/Day4Input.txt")
print(part1(inputs))

