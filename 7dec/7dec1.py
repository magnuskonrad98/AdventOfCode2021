import os

def open_file():
    script_dir = os.path.dirname(__file__)
    rel_path = "7dec.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    file_object = open(abs_file_path, "r")
    position_list = file_object.read().strip().split(",")
    return position_list

def sort_list(position_list):
    integer_list = [int(i) for i in position_list] #From list of strings to list of integers
    integer_list.sort()
    return integer_list

def get_lowest(sorted_list):
    lower_or_equal = 0 #Number of crabs with lower or equal position than the current position
    higher = len(sorted_list) #Crabs with higher position than the current position
    curr_pos = 0
    current_cost = sum(sorted_list) #Current cost at position 0
    lowest_cost = current_cost #Current cost is the lowest known cost to begin with
    change = 0
    while sorted_list[curr_pos] == 0: #Begin by checking if there are any crabs located at position 0
        curr_pos += 1
        lower_or_equal +=1
        higher -= 1

    for i in range(1, sorted_list[-1] + 1): #We iterate through every position
        while sorted_list[curr_pos] <= i: #We keep count of the crabs that are moving from 'higher' to 'lower' as the current position increases
            change += 1
            curr_pos += 1
            if curr_pos == len(sorted_list):
                break
        current_cost = current_cost - higher + lower_or_equal #The change of the current cost depends on how many crabs there are on each side when moving
        lower_or_equal += change
        higher -= change

        change = 0
        if current_cost < lowest_cost:
            lowest_cost = current_cost
    return lowest_cost




def main():
    position_list = open_file()
    sorted_list = sort_list(position_list)
    lowest_cost = get_lowest(sorted_list)
    print(lowest_cost)

main()