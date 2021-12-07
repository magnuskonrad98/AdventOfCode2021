import os

def open_file():
    script_dir = os.path.dirname(__file__)
    rel_path = "1dec.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    file_object = open(abs_file_path, "r")
    depth_list = []
    for line in file_object:
        depth_list.append(int(line.strip()))
    return depth_list

def calculate_deeper(depth_list):
    """How many times is the sliding window of 3 measurements bigger than the last one"""
    got_deeper = 0
    oldest = depth_list.pop(0)
    older = depth_list.pop(0)
    old = depth_list.pop(0)
    old_trio = oldest + older + old
    for depth in depth_list:
        depth_trio = older + old + depth
        if depth_trio > old_trio:
            got_deeper += 1
        older = old
        old = depth
        old_trio = depth_trio
    return got_deeper

def main():
    depth_list = open_file()
    got_deeper = calculate_deeper(depth_list)
    print(got_deeper)

main()