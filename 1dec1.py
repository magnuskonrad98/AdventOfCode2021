def open_file():
    depth_list = []
    fileobject = open("1dec1.txt", "r")
    for line in fileobject:
        depth_list.append(int(line.strip()))
    return depth_list

def calculate_deeper(depth_list):
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