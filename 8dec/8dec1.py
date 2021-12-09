import os
import re


def open_file():
    script_dir = os.path.dirname(__file__)
    rel_path = "8dec.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    file_object = open(abs_file_path, "r")
    data_list = []
    for line in file_object:
        data_list.append(re.findall(r"[\w']+", line.strip())) #Split on ' ' and '|'
    return data_list

def number_unique_length(data_list):
    counter = 0
    unique_lengths = [2,3,4,7]
    for data in data_list:
        for i in range(10, 14):
            if len(data[i]) in unique_lengths:
                counter += 1
    return counter


def main():
    data_list = open_file()
    unique_length_nums = number_unique_length(data_list)
    print(unique_length_nums)

main()