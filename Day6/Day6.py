def part1(moves):
    # i get it, there are 1000 operations and 4000 words (numbers)
    # find the number of and the type of operation first
    length_moves = len(moves) - 1
    list_problems = moves[:length_moves]
    operations = moves[length_moves].split(" ")
    total = 0
    # split all into lists and remove white spaces
    while "" in operations:
        operations.remove("")
    for i, problems in enumerate(list_problems):
        new_problems = problems.split(" ")
        while "" in new_problems:
            new_problems.remove("")
        list_problems[i] = new_problems

    # solve for equation
    columns = len(list_problems[0])
    rows = len(list_problems)

    solution = 0
    for col in range(columns):
        operation = operations[col]
        if operation == "*":
            solution = 1
        else:
            solution = 0
        print(operation)
        for row in range(rows):
            if operation == "*":
                solution *= int(list_problems[row][col])
            else:
                solution += int(list_problems[row][col])
        total += solution
    return total


# Opens a file and splits lines into inputs
def open_file(filename):
    # opens file and returns all strings
    with open(filename, "r") as file_input:
        input = file_input.read()
        # double new line seperates file into two
        list_of_values = input.split("\n")
        # return indiviudal lines from two parts as
        return list_of_values


# inputs is a tuple with ingredient ids and ingredients to check
inputs = open_file("Day6/Day6Input.txt")
print(part1(inputs))
