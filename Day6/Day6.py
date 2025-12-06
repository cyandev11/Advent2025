def part1(problems, operations):
    # solve for equation
    columns = len(problems[0])
    rows = len(problems)

    total = 0
    solution = 0
    for col in range(columns):
        operation = operations[col]
        if operation == "*":
            solution = 1
        else:
            solution = 0
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
# i get it, there are 1000 operations and 4000 words (numbers)
# find the number of and the type of operation first
length_inputs = len(inputs) - 1
list_problems = inputs[:length_inputs]
operations = inputs[length_inputs].split(" ")

# split all into lists and remove white spaces
while "" in operations:
    operations.remove("")
for i, problems in enumerate(list_problems):
    problems = problems.split(" ")
    while "" in problems:
        problems.remove("")
    list_problems[i] = problems

print(part1(list_problems, operations))
