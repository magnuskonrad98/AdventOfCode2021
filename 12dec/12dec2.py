import os

def open_file():
    script_dir = os.path.dirname(__file__)
    rel_path = "12dec.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    caves = {}
    file_object = open(abs_file_path, "r")
    for line in file_object: #We make a dict where caves are the keys and the values are the caves you can get to from that cave
        cave1, cave2 = line.strip().split("-")
        if cave1 in caves:
            caves[cave1].append(cave2)
        else:
            caves[cave1] = [cave2]
        
        if cave2 in caves:
            caves[cave2].append(cave1)
        else:
            caves[cave2] = [cave1]
    return caves

def find_routes(caves, current, visited, visited_twice):
    #Find recursively how many routes are possible from start to end
    if current == "start" and len(visited) > 0: #We only want start once
        return 0
    if current == "end":
        return 1
    if current in visited and current.islower(): #We only need to think about small caves
        if visited_twice == True: #We can only visit one small cave twice
            return 0
        else:
            visited_twice = True
    visited.append(current)
    current_sum = 0
    for i in caves[current]:
        current_sum += find_routes(caves, i, visited, visited_twice) #Recurse for every aligning cave
    visited.pop()
    return current_sum


def main():
    caves = open_file()
    routes = find_routes(caves, "start", [], False)
    print(routes)
    

main()