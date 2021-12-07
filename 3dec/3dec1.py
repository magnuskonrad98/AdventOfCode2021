import os

def open_file():
    script_dir = os.path.dirname(__file__)
    rel_path = "3dec.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    file_object = open(abs_file_path, "r")
    binary_list = []
    for line in file_object:
        binary_list.append(line.strip())
    return binary_list

def most_common_bits(binary_list):
    binary_shit = ""
    for bit in range(len(binary_list[0])):
        ones = 0
        zeros = 0
        for num in binary_list:
            if num[bit] == "1":
                ones += 1
            else:
                zeros += 1
        if ones > zeros:
            binary_shit += "1"
        else:
            binary_shit += "0"
    return binary_shit

def to_decimals(bit_string):
    gamma = 0
    epsilon = 0
    for i in range(len(bit_string)):
        bit = int(bit_string[len(bit_string) - 1 - i])
        gamma += bit * (2**i)
        epsilon += (0**bit) * (2**i)
    return (gamma, epsilon, gamma*epsilon)


def main():
    binary_list = open_file()
    bit_string = most_common_bits(binary_list)
    values = to_decimals(bit_string)
    print("Gamma: {}\nEpsilon: {}\nConsumption: {}".format(values[0], values[1], values[2]))

main()
