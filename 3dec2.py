def open_file():
    fileobject = open("3dec.txt", "r")
    binary_list = []
    for line in fileobject:
        binary_list.append(line.strip())
    return binary_list


def find_oxygen(binary_list):
    """Check how many numbers have 1s and how many have 0s in the first bit. Eliminate those that are FEWER of. 
    Repeat with the second, third bit, until there is 1 number left"""
    for i in range(len(binary_list[0])):
        ones = 0
        zeros = 0
        ones_list = []
        zeros_list = []
        for binary_num in binary_list:
            num = binary_num[i]
            if num == "1":
                ones +=1
                ones_list.append(binary_num)
            else:
                zeros += 1
                zeros_list.append(binary_num)
        if len(ones_list) >= len(zeros_list):
            binary_list = ones_list
        else:
            binary_list = zeros_list
        if len(binary_list) == 1:
            return binary_list[0]


def find_co2(binary_list):
    """Check how many numbers have 1s and how many have 0s in the first bit. Eliminate those that are MORE of. 
    Repeat with the second, third bit, until there is 1 number left"""
    for i in range(len(binary_list[0])):
        ones = 0
        zeros = 0
        ones_list = []
        zeros_list = []
        for binary_num in binary_list:
            num = binary_num[i]
            if num == "1":
                ones +=1
                ones_list.append(binary_num)
            else:
                zeros += 1
                zeros_list.append(binary_num)
        if len(ones_list) < len(zeros_list):
            binary_list = ones_list
        else:
            binary_list = zeros_list
        if len(binary_list) == 1:
            return binary_list[0]

def to_decimals(bit_string):
    decimal = 0
    for i in range(len(bit_string)):
        bit = int(bit_string[len(bit_string) - 1 - i])
        decimal += bit * (2**i)
    return decimal

def main():
    binary_list = open_file()
    oxygen_binary = find_oxygen(binary_list)
    co2_binary = find_co2(binary_list)
    oxygen = to_decimals(oxygen_binary)
    co2 = to_decimals(co2_binary)
    life_support_rating = oxygen * co2
    print("Oxygen: {}\nCO2: {}\nLSR: {}".format(oxygen, co2, life_support_rating))

main()