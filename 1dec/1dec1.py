import os

def open_file():
    script_dir = os.path.dirname(__file__)
    rel_path = "1dec.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    depth_list = []
    fileobject = open(abs_file_path, "r")
    for line in fileobject:
        depth_list.append(int(line.strip()))
    return depth_list

def calculate_deeper(depth_list):
    """How many times is the new measurement deeper than the last one"""
    lower_depths = 0
    old_depth = depth_list.pop(0)
    for depth in depth_list:
        if depth > old_depth:
            lower_depths += 1
        old_depth = depth
    return lower_depths

def main():
    depth_list = open_file()
    lower_depths = calculate_deeper(depth_list)
    print(lower_depths)

main()