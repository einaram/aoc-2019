
def get_adjacent(r,c,grid):
    if r < 0 or c < 0:
        value = "."
    elif r > 4 or c > 4 :
        value = "."       
    else:
        value = grid[r][c]
    return value

def new_bug_state(r,c,grid):
    current_space = grid[r][c]
    above = get_adjacent(r-1,c,grid)
    below = get_adjacent(r+1,c,grid)
    left = get_adjacent(r,c-1,grid)
    right = get_adjacent(r,c+1,grid)
    surrounding = [above, right, below, left]

    if current_space == "#":
        if surrounding.count("#") != 1:
            current_space = "."
    else:
        if 1 <= surrounding.count("#")  <=2:
            current_space = "#"
    return current_space

def create_new_grid(grid):
    new_grid=[]

    for r,row in enumerate(grid):
        new_row=[]
        for c,col in enumerate(row):
            new_row.append(new_bug_state(r,c,grid))
        new_grid.append(new_row)
    return new_grid


def print_tiles(grid):
    for r,row in enumerate(grid):
        for c,col in enumerate(row):
            print(col,end = '')
        print("")

def calc_biodiversity(grid):
    i = 0
    tiles = []
    for r,row in enumerate(grid):
        for c,col in enumerate(row):
            if grid[r][c] == "#":
                tiles.append(2 ** i)
            i += 1

    return tiles

initial =\
"""
....#
#..#.
#..##
..#..
#...."""

initial_real =\
"""
#..##
##...
.#.#.
#####
####."""

initial = initial_real.strip().split("\n")
initial_lst = [[y for y in x ] for x in initial]




grids = []
grid = initial_lst
i = 0
while 1:
    grid = create_new_grid(grid)
    if grid in grids:
        print("match", i)
        print(print_tiles(grid))
        break
    grids.append(grid)
    i +=1

print_tiles(initial_lst)
print(sum(calc_biodiversity(grid)))





