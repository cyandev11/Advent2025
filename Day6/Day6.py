import numpy


def part1(moves):
    # split all into lists and remove white spaces
    for i, problems in enumerate(moves):
        problems = problems.split(" ")
        while "" in problems:
            problems.remove("")
        moves[i] = problems
    # transpose array
    moves = numpy.transpose(moves).tolist()
    total = 0
    # for every equation, solve the equation depending on the operation
    for equation in moves:
        operation = equation[-1]
        numbers = equation[:-1]
        total += solve_equation(numbers, operation)
    return total


def part2(moves):
    numbers = moves[:-1]
    operations = moves[-1]
    total = 0
    # find ranges for each eqaution with the last row
    indexs = []
    for i, operation in enumerate(operations):
        if operation == "*" or operation == "+":
            indexs.append(i)
    indexs.append(len(moves[0]))

    # for every range of numbers find the equation for that
    for i, index in enumerate(indexs[:-1]):
        lower_index = indexs[i]
        higher_index = indexs[i + 1]

        # find equation
        equation = ""
        # numbers for the eqaution are based on index, numbers to the left, the specific digits move veritcally
        while higher_index > lower_index:
            higher_index -= 1
            for number in numbers:
                equation += number[higher_index]
            equation += " "

        # now that we have the new numbers, clean by spliting and removing white space
        current_eqaution = equation.split(" ")
        while "" in current_eqaution:
            current_eqaution.remove("")
        # find if + or *
        current_operation = operations[lower_index]

        # using numbers and operation, solve for solution
        solution = solve_equation(current_eqaution, current_operation)
        total += solution
    return total


def solve_equation(numbers, operation):
    solution = 0
    if operation == "*":
        solution = 1
    for number in numbers:
        if operation == "*":
            solution *= int(number)
        else:
            solution += int(number)
    return solution


# Opens a file and splits lines into inputs
def open_file(filename):
    # opens file and returns all strings
    with open(filename, "r") as file_input:
        input = file_input.read()
        # double new line seperates file into two
        list_of_values = input.split("\n")
        # return indiviudal lines from two parts as
        return list_of_values


inputs = open_file("Day6/Day6Input.txt")
print(part1(inputs))

inputs = open_file("Day6/Day6Input.txt")
print(part2(inputs))
