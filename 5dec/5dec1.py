import os

floor = [{} for _ in range(1000)] #List of 1000 dictionaries. Each dictionary is a row.
double_marked_spots = 0 #Keep count of the number of cordinates that multiple lines cross.


def open_file():
    script_dir = os.path.dirname(__file__)
    rel_path = "5dec.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    file_object = open(abs_file_path, "r")
    cordinates_list = []
    for line in file_object:
        cordinates = []
        begin, end = line.strip().split(" -> ")
        x1, y1 = begin.split(",")
        x2, y2 = end.split(",")
        cordinates.append(int(x1)) #We make a list of each line
        cordinates.append(int(y1))
        cordinates.append(int(x2))
        cordinates.append(int(y2))
        cordinates_list.append(cordinates) #List of lists
    return cordinates_list

def mark_floor(cordinates_list):
    global double_marked_spots #We are changing the value of the global variable
    for cordinates in cordinates_list:
        if cordinates[0] == cordinates[2]: #If the x cordinates are the same (x1 and x2) we have a vertical line
            x_value = cordinates[0]
            if cordinates[1] < cordinates[3]:
                y_min = cordinates[1]
                y_max = cordinates[3]
            else:
                y_min = cordinates[3]
                y_max = cordinates[1]
            for i in range(y_min, y_max+1):
                if x_value in floor[i]:
                    floor[i][x_value] += 1 #Update the dictionary
                    if floor[i][x_value] == 2: #We have to check if this is the second time this point is being crossed
                        double_marked_spots += 1 
                else:
                    floor[i][x_value] = 1 #Insert a new value to the dictionary
        
        elif cordinates[1] == cordinates[3]: #If the y cordinates are the same we have a horizontal line
            y_value = cordinates[1]
            if cordinates[0] < cordinates[2]:
                x_min = cordinates[0]
                x_max = cordinates[2]
            else:
                x_min = cordinates[2]
                x_max = cordinates[0]
            for i in range(x_min, x_max+1):
                if i in floor[y_value]:
                    floor[y_value][i] += 1
                    if floor[y_value][i] == 2:
                        double_marked_spots += 1
                else:
                    floor[y_value][i] = 1
    return double_marked_spots


def main():
    cordinates_list = open_file()
    double_marked = mark_floor(cordinates_list)
    print(double_marked)

main()

