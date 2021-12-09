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

def to_dict(sorted_list):
    dict_list = [0 for i in range(sorted_list[-1] + 1)] #Change the list into a dictionary made with a list
    for j in sorted_list:
        dict_list[j] += 1
    return dict_list

def get_lowest(dict_list):
    lowest_cost = None
    current_cost = 0
    cost = 1
    change_of_cost = 1

    for i in range(len(dict_list)):
        for j in range(i - 1, -1, -1): #Iterate through crabs with lower position
            current_cost += dict_list[j] * cost #Multiply the number of crabs with the cost of each one
            change_of_cost += 1 #The change of cost increases by every step
            cost += change_of_cost

        cost = 1
        change_of_cost = 1
        for k in range(i + 1, len(dict_list)): #Iterate through crabs with higher position
            current_cost += dict_list[k] * cost
            change_of_cost += 1
            cost += change_of_cost
        
        if lowest_cost == None or current_cost < lowest_cost:
            lowest_cost = current_cost
        current_cost = 0
        cost = 1
        change_of_cost = 1

    return lowest_cost



def main():
    position_list = open_file()
    sorted_list = sort_list(position_list)
    dict_list = to_dict(sorted_list)
    lowest_cost = get_lowest(dict_list)
    print(lowest_cost)

main()