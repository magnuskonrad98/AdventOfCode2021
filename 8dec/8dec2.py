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

def decode(data):
    decoded = [0 for _ in range(10)]
    fives = []
    sixes = []
    right_top = ""
    right_bottom = ""
    
    for i in range(10):
        curr_num = data[i]
        sorted_characters = sorted(curr_num)
        curr_sorted = "".join(sorted_characters)
        if len(curr_sorted) == 2:
            decoded[1] = curr_sorted
        elif len(curr_sorted) == 3:
            decoded[7] = curr_sorted
        elif len(curr_sorted) == 4:
            decoded[4] = curr_sorted
        elif len(curr_sorted) == 5:
            fives.append(curr_sorted)
        elif len(curr_sorted) == 6:
            sixes.append(curr_sorted)
        elif len(curr_sorted) == 7:
            decoded[8] = curr_sorted

    for num in sixes: #This for loop puts the 0, 6 and the 9 in the decoded numers list
        if decoded[1][0] in num:
            if decoded[1][1] in num: #Could be 0 or 9
                is_zero = 0
                counter = 0
                while counter < 4:
                    if decoded[4][counter] not in num: #All the characters of 4 should also be in 9
                        is_zero = 1
                        break
                    counter += 1
                if is_zero:
                    decoded[0] = num
                else:
                    decoded[9] = num
            else: #6 is the only number of those three that has only one of the two right characters
                decoded[6] = num
                right_top = decoded[1][1]
                right_bottom = decoded[1][0]
        else:
            decoded[6] = num
            right_top = decoded[1][0]
            right_bottom = decoded[1][1]

    for num in fives:
        if right_bottom in num and right_top not in num:
            decoded[5] = num
        elif right_top in num and right_bottom not in num:
            decoded[2] = num
        else:
            decoded[3] = num

    return decoded


def calculate(data_list):
    sum_of_numbers = 0
    for data in data_list:
        decoded_numbers = decode(data)
        num_str = ""
        for i in range(10, 14):
            num = data[i]
            sorted_characters = sorted(num)
            sorted_num = "".join(sorted_characters)
            decoded_num = str(decoded_numbers.index(sorted_num))
            num_str += decoded_num
        sum_of_numbers += int(num_str)
    return sum_of_numbers





def main():
    data_list = open_file()
    sum_of_numbers = calculate(data_list)
    print(sum_of_numbers)

main()