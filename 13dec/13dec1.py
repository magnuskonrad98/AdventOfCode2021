import os

def open_file():
    script_dir = os.path.dirname(__file__)
    rel_path = "13dec.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    cordinates = []
    instructions = []
    file_object = open(abs_file_path, "r")
    for line in file_object:
        stripped_line = line.strip()
        if "," in stripped_line: #We make a list of tuples for the cordinates
            x, y = stripped_line.split(",")
            cordinates.append((int(x), int(y)))
        if "fold" in stripped_line: #We make a list of lists for the instructions
            axis, value = stripped_line[11:].split("=")
            instructions.append([axis, value])
    return (cordinates, instructions)

def fold(cordinates, instructions):
    instruction = instructions[0] #For this example, we only read the first instruction
    axis = instruction[0] #x or y
    value = int(instruction[1])
    for i in range(len(cordinates)):
        x = cordinates[i][0]
        y = cordinates[i][1]
        if axis == "x": #Fold horizontally
            if x > value: #The cordinates don't change if they are above the line of the fold
                difference = x - value
                new_X = value - difference #Calculate the new value of the x cordinate
                cordinates[i] = (new_X, y)
        if axis == "y": #Fold vertically
            if y > value:
                difference = y - value
                new_y = value - difference
                cordinates[i] = (x, new_y)
    cordinates = list(dict.fromkeys(cordinates))
    return cordinates

def main():
    data = open_file()
    cordinates = data[0]
    instructions = data[1]
    cordinates = fold(cordinates, instructions)
    print(len(cordinates))

main()