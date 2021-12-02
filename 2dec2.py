def open_file():
    file_object = open("2dec.txt", "r")
    instruction_list = []
    for line in file_object:
        direction, quantity = line.strip().split(" ")
        instruction_list.append((direction, int(quantity)))
    return instruction_list

def calculate_position(instruction_list):
    depth = 0
    horizontal = 0
    aim = 0
    for instruction in instruction_list:
        if instruction[0] == "forward":
            horizontal += instruction[1]
            depth += aim*instruction[1]
        elif instruction[0] == "down":
            aim += instruction[1]
        elif instruction[0] == "up":
            aim -= instruction[1]
    return (depth, horizontal)

def main():
    instruction_list = open_file()
    position = calculate_position(instruction_list)
    depth = position[0]
    horizontal = position[1]
    multiplication = depth * horizontal
    print("Depth:      {}\nHorizontal: {}\nMultiplication: {}".format(depth, horizontal, multiplication))

main()