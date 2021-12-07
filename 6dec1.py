lanternfish_offspring_dict = {}

def open_file():
    file_object = open("6dec.txt", "r")
    lanternfish_list = file_object.read().strip().split(",")
    return lanternfish_list

def total_fish(lanternfish_list):
    """Returns the total amount of lanternfish there will be in 80 days."""
    total_lanternfish = 0
    for lanternfish in lanternfish_list:
        if lanternfish in lanternfish_offspring_dict: #First we check if the value for a lanternfish with that amount of days left to live is already in our dictionary
            total_lanternfish += lanternfish_offspring_dict[lanternfish] #If it is, we add that value to our total count
        else: 
            calculated_offsprings = calculate_new_total(lanternfish) #If the value is not in our dictionary, we calculate it
            lanternfish_offspring_dict[lanternfish] = calculated_offsprings #We then store the value in our dictionary
            total_lanternfish += calculated_offsprings
    return total_lanternfish

def calculate_new_total(lanternfish):
    """Calculates the total offsprings a lanternfish with a certain amount of days to live, will have in 80 days"""
    lanternfish_list = [int(lanternfish)]
    for i in range(80):
        for j in range(len(lanternfish_list)):
            if lanternfish_list[j] == 0:
                lanternfish_list[j] = 6
                lanternfish_list.append(8)
            else:
                lanternfish_list[j] -= 1
    return len(lanternfish_list)


def main():
    lanternfish_list = open_file()
    total_lanternfish = total_fish(lanternfish_list)
    print(total_lanternfish)


main()