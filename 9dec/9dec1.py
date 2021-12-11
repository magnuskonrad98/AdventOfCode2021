import os


def open_file():
    script_dir = os.path.dirname(__file__)
    rel_path = "9dec.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    grid = []
    file_object = open(abs_file_path, "r")
    for line in file_object:
        grid.append(line.strip())
    return grid

def sum_of_lowpoints(grid):
    lowpoint_sum = 0
    for i in range(len(grid)):
        j = 0
        while j < len(grid[i]):
            curr = grid[i][j]
            lowpoint = True
            if i != 0: #Only check the position above if we're not in the top line
                if curr >= grid[i - 1][j]:
                    lowpoint = False
            if lowpoint and i != len(grid) - 1: #Only check the line below if we´re not in the bottom line
                if curr >= grid[i + 1][j]:
                    lowpoint = False
            if lowpoint and j != 0: #Only check the position to the left if we're not in the leftmost position
                if curr >= grid[i][j - 1]:
                    lowpoint = False
            if lowpoint and j != len(grid[i]) - 1: #Only check the position to the right if we're not in the rightmost position
                if curr >= grid[i][j + 1]:
                    lowpoint = False
            if lowpoint:
                lowpoint_sum += int(curr) + 1
                j += 2 #Don't need to check the next position if this position is already a lowpoint
            else:
                j += 1
    return lowpoint_sum

def main():
    grid = open_file()
    lowpoint_sum = sum_of_lowpoints(grid)
    print(lowpoint_sum)

main()

