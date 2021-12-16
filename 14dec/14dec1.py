import os

def open_file():
    script_dir = os.path.dirname(__file__)
    rel_path = "14dec.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    rules = {}
    file_object = open(abs_file_path, "r")
    for line in file_object:
        if "->" in line.strip():
            letters, new_letter = line.strip().split(" -> ")
            rules[letters] = new_letter
        else:
            if line.strip() != "":
                template = line.strip()
    return rules, template

def get_total_string(rules, template):
    for _ in range(10):
        new_string = ""
        for i in range(len(template)):
            new_string += template[i]
            if i != len(template) - 1:
                new_char = rules[template[i:i+2]]
                new_string += new_char
        template = new_string
    return template
    

def most_minus_least_common(string):
    quantity_dict = {}
    for char in string:
        if char in quantity_dict:
            quantity_dict[char] += 1
        else:
            quantity_dict[char] = 1
    highest = None
    lowest = None
    for key, value in quantity_dict.items():
        if highest is None or value > highest:
            highest = value
        if lowest is None or value < lowest:
            lowest = value
    return highest - lowest



def main():
    data = open_file()
    rules = data[0]
    template = data[1]
    total_string = get_total_string(rules, template)
    value = most_minus_least_common(total_string)
    print(value)

main()
