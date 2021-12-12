import os
import statistics

def open_file():
    script_dir = os.path.dirname(__file__)
    rel_path = "10dec.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    lines = []
    file_object = open(abs_file_path, "r")
    for line in file_object:
        lines.append(line.strip())
    return lines

def get_line_points(line):
    openers = ["(", "[", "{", "<"]
    closers = [")", "]", "}", ">"]
    points_dict = {"(": 1, "[": 2, "{": 3, "<": 4}
    total_score = 0

    open_chunks = []
    for char in line:
        if char in openers:
            open_chunks.append(char) #Append all openers to the list
        else:
            char_index = closers.index(char) #If char is a closer, we check if it is relative to the last opener
            opener = openers[char_index]
            if open_chunks[-1] == opener:
                open_chunks.pop() #We pop the last opener when it gets closed
            else:
                return 0
    
    for i in reversed(open_chunks): #To find the points of the line, we multiply its current score (initially 0) by 5 and then add points to it according to the points_dict
        total_score *= 5
        total_score += points_dict[i]

    return total_score
        

def get_median_points(lines):
    points_list = []
    for line in lines:
        points = get_line_points(line)
        if points != 0:
            points_list.append(points)
    median = statistics.median(points_list) #Return the median of the points_list
    return median


def main():
    lines = open_file()
    median = get_median_points(lines)
    print(median)

main()