def part1(moves):
    print()


# Opens a file and splits lines into inputs
def open_file(filename):
    # opens file and returns all strings
    with open(filename, "r") as file_input:
        input = file_input.read()
        list_of_values = input.split("\n")
        return list_of_values


inputs = open_file("Day2/Day2Input.txt")
print(part1(inputs))