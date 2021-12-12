import os

def open_file():
    script_dir = os.path.dirname(__file__)
    rel_path = "11dec.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    grid = []
    file_object = open(abs_file_path, "r")
    for line in file_object:
        line_list =[]
        for char in line.strip():
            line_list.append(int(char))
        grid.append(line_list)
    return grid

def get_flashes(grid, loops):
    """Loops n times and returns the sum of flashes"""
    total_flashes = 0
    for _ in range(loops):
        flashes = update(grid)
        total_flashes += flashes
        reset(grid)
    return total_flashes

def update(grid):
    """Iterates through every position and increases every one by 1. If a position reaches above 9, it flashes"""
    flashes = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] < 9:
                grid[i][j] += 1
            else:
                flashes += flash(grid, i, j)
    return flashes

def flash(grid, i, j):
    """Recursively increases all surrounding positions that are 9 or less"""
    if 0 <= i <= len(grid)-1 and 0 <= j <= len(grid[0])-1: #Check if the position exists
        if grid[i][j] < 10:
            grid[i][j] += 1
            if grid[i][j] == 10:
                return 1 + flash(grid, i-1, j-1) + flash(grid, i-1, j) + flash(grid, i-1, j+1) + flash(grid, i, j-1) + flash(grid, i, j+1) + flash(grid, i+1, j-1) + flash(grid, i+1, j) + flash(grid, i+1, j+1)
    return 0

def reset(grid):
    """Sets every 10 to a 0"""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] > 9:
                grid[i][j] = 0


def main():
    grid = open_file()
    flashes = get_flashes(grid, 100)
    print(flashes)

main()