import os
quantity_list = [0, 0, 0, 0, 0, 0, 0, 0, 0] #Keep count of the quantity of fish with each possible value of "days left"

def open_file():
    script_dir = os.path.dirname(__file__)
    rel_path = "6dec.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    file_object = open(abs_file_path, "r")
    lanternfish_list = file_object.read().strip().split(",")
    return lanternfish_list

def populate_list(lanternfish_list):
    for lanternfish in lanternfish_list:
        quantity_list[int(lanternfish)] += 1
    
def total_fish(days):
    for i in range(days):
        new_fish = quantity_list.pop(0) #Pop the amount of fish with 0 days left and add it to both fish with 6 days and 8 days left
        quantity_list[6] += new_fish
        quantity_list.append(new_fish)
    return sum(quantity_list)


def main():
    lanternfish_list = open_file()
    populate_list(lanternfish_list)
    total_lanternfish = total_fish(256)
    print(total_lanternfish)


main()