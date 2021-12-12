import os

def open_file():
    script_dir = os.path.dirname(__file__)
    rel_path = "10dec.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    lines = []
    file_object = open(abs_file_path, "r")
    for line in file_object:
        lines.append(line.strip())
    return lines

def get_wrong_char(line):
    openers = ["(", "[", "{", "<"]
    closers = [")", "]", "}", ">"]
    open_chunks = []
    for char in line:
        if char in openers:
            open_chunks.append(char)
        else:
            char_index = closers.index(char)
            opener = openers[char_index]
            if open_chunks[-1] == opener:
                open_chunks.pop()
            else:
                return char
    return 0

def do_shit(lines):
    points_dict = {")": 3, "]": 57, "}": 1197, ">": 25137}
    points_sum = 0
    for line in lines:
        char = get_wrong_char(line)
        if char != 0:
            points = points_dict[char]
            points_sum += points
    return points_sum


    
def main():
    lines = open_file()
    total_points = do_shit(lines)
    print(total_points)

main()