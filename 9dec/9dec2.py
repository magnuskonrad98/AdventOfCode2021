import os

class Basin:
    def __init__(self):
        self.size = 0
        self.last_line = [0,0,0] 

def open_file():
    script_dir = os.path.dirname(__file__)
    rel_path = "9dec.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    grid = []
    file_object = open(abs_file_path, "r")
    for line in file_object:
        grid.append(line.strip())
    return grid


def get_basins(grid):
    basins = []
    grid_visited = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))] #We only want to visit each position once
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
                size = get_size(grid, grid_visited, i, j)
                basins.append(size)
                j += 2 #Don't need to check the next position if this position is already a lowpoint
            else:
                j += 1
    return basins

def get_size(grid, grid_visited, i, j):
    #Recursively visits all positions of a basin and finds its size
    if 0 <= i <= len(grid) - 1 and 0 <= j <= len(grid[i]) - 1:
        if grid_visited[i][j] == True or grid[i][j] == "9": #We only visit positions not visited before which are not 9
            return 0
        else:
            grid_visited[i][j] = True
            return 1 + get_size(grid, grid_visited, i-1, j) + get_size(grid, grid_visited, i+1, j) + get_size(grid, grid_visited, i, j-1) + get_size(grid, grid_visited, i, j+1) #Check all directions from the position
    else:
        return 0

def three_max(basins): 
    #Find the three biggest basins and return the product of them
    basins_sorted = sorted(basins)
    product = basins_sorted[-1] * basins_sorted[-2] * basins_sorted[-3]
    return product

def main():
    grid = open_file()
    basins = get_basins(grid)
    product = three_max(basins)
    print(product)

main()

