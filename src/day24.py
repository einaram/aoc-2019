import pprint
import copy


class GridCalc():
    def __init__(self, initial_grid):
        self.minute = 0
        self.local_grid = []
        self.outer_grid = []
        self.current_coord_local = {
            "r": 0,
            "c": 0
        }
        self.coord_per_lvl={}
        self.full_grid = initial_grid
        self.grid_html = ""
        self.level=0
        self.grids_per_lvl = {}
        self.sum =0

    def get_above(self,r,c,grid):
        try:
            if r-1 == -1:
                #outside grid
                r_o=self.coord_per_lvl[self.level-1]['r']
                c_o=self.coord_per_lvl[self.level-1]['c']
                value = self.grids_per_lvl[self.level-1][r_o-1][c_o]
            else:
                value = grid[r-1][c]
            if type(value) == list:
                value = sum(value[-1])
        except:
            value = 0
        return value
    def get_below(self,r,c,grid):
        try:
            if r+1 == 5:
                #outside grid
                r_o=self.coord_per_lvl[self.level-1]['r']
                c_o=self.coord_per_lvl[self.level-1]['c']
                value = self.grids_per_lvl[self.level-1][r_o+1][c_o]
            else:
                value = grid[r+1][c]
            if type(value) == list:
                value = sum(value[0])
        except:
            value = 0
        return value
    def get_right(self,r,c,grid):
        try:
            if c+1 == 5:
                #outside grid
                r_o=self.coord_per_lvl[self.level-1]['r']
                c_o=self.coord_per_lvl[self.level-1]['c']
                value = self.grids_per_lvl[self.level-1][r_o][c_o+1]
            else:
                value = grid[r][c+1]
            if type(value) == list:
                value = sum([x[0] for x in value])
        except:
            value = 0
        return value
    def get_left(self,r,c,grid):
        try:
            if c-1 == -1:
                #outside grid
                r_o=self.coord_per_lvl[self.level-1]['r']
                c_o=self.coord_per_lvl[self.level-1]['c']
                value = self.grids_per_lvl[self.level-1][r_o][c_o-1]
            else:
                value = grid[r][c-1]

            if type(value) == list:
                value = sum([x[-1] for x in value])
        except:
            value = 0
        return value

    def get_all_adjacent(self, grid):
        r = self.coord_per_lvl[self.level]['r']
        c = self.coord_per_lvl[self.level]['c']
        # print(self.level*"   ", r ,c)
        
        if r == 4 and c == 3 and self.level == 3:
           a=1+1
        above = self.get_above(r, c, grid,)
        below = self.get_below(r, c, grid)
        left = self.get_left(r, c, grid)
        right = self.get_right(r, c, grid)
        surrounding = [above, right, below, left]
        if r == 0 and c == 0 and sum(surrounding) == 0:
            1+1
        return surrounding

    def sum_bugs(self, grid=None):
        if grid is None:
            grid = self.full_grid
        for r, row in enumerate(grid):
            # print("summing row", r)
            for c, col in enumerate(row):
                if type(col) == list:
                    self.sum_bugs(col)
                else:
                    self.sum += col
        


    def new_bug_state(self, grid):

        r=self.coord_per_lvl[self.level]['r']
        c=self.coord_per_lvl[self.level]['c']
        
        current_tile = grid[r][c]

        surrounding = self.get_all_adjacent(grid)

        if type(current_tile) == list:
            self.outer_grid = grid
            current_tile = self.create_new_grid(current_tile)

        elif current_tile == 1:
            if sum(surrounding) != 1:
                current_tile = 0
        else:
            if 1 <= sum(surrounding) <= 2:
                current_tile = 1
        return current_tile

    def run_minute(self):
        self.write_tables()

        self.grids_per_lvl= {}

        #Add empty in bottom:
        value = self.full_grid
        while True:
            if not type(value[2][2]) == list:
                value[2][2] = create_empty()
                break
            value = value[2][2]
        #Add topp
        self.full_grid = create_empty(self.full_grid)

        self.full_grid = self.create_new_grid()
        self.minute += 1
        # print(self.minute)
        self.write_tables()
        

    def create_new_grid(self, grid=None):
        self.level +=1
        if grid is None:
            grid = self.full_grid
        new_grid = []
        self.local_grid = grid
        self.grids_per_lvl[self.level] = grid
        for r, row in enumerate(grid):
            new_row = []
            for c, col in enumerate(row):
                self.coord_per_lvl[self.level]={'r':r, 'c':c}

                new_row.append(self.new_bug_state(grid))
            new_grid.append(new_row)
        self.level -=1
        return new_grid

    def print_tiles(self, grid):
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                print(col, end='')
            print("")
    
    def write_tables(self):
        with open(f"24-{self.minute}.html",'w') as outfile:
            self.grids_to_table()
            outfile.write("""<html><style>table, th, td {
                border: 1px solid black;
                border-collapse: collapse;
                }
                td {width:50px;
                height:50px;}</style>""")
            outfile.write(self.grid_html)

    def grids_to_table(self,grid=None):
        if grid is None:
            grid = self.full_grid
            self.grid_html = "<table>"
        else:
            self.grid_html += f"<table id={self.level}>"
        for r, row in enumerate(grid):
            self.grid_html += "<tr>"
            for c, col in enumerate(row):
                if type(col) == list:
                    self.grid_html +=f"<td>"
                    self.grids_to_table(col)
                    self.grid_html +=f"</td>"
                else:
                    self.grid_html +=f"<td>{col}</td>"
            self.grid_html +="</tr>"
        self.grid_html +="</table>"
        # return grid_html

    def calc_biodiversity(self, grid):
        i = 0
        tiles = []
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if grid[r][c] == 1:
                    tiles.append(2 ** i)
                i += 1

        return tiles


def create_empty(center_grid=None):
    # empty = list([list(["."]*5)]*5)
    empty = [[0 for i in range(5)] for i in range(5)]
    if center_grid:
        empty[2][2] = center_grid

    return empty


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


def cleaned_input(initial):
    initial_replaced = initial.replace(
        ".", "0").replace("#", "1").strip().split("\n")
    initial_lst = [[int(y) for y in x] for x in initial_replaced]
    return initial_lst





def part1(grid):
    GridStack = GridCalc(grid)
    grids = []
    i = 0
    while 1:
        grid = GridStack.create_new_grid(grid)
        if grid in grids:
            print("match", i)
            print(GridStack.print_tiles(grid))
            break
        grids.append(grid)
        i += 1

    print(sum(GridStack.calc_biodiversity(grid)))
    

# initial_lst = cleaned_input(initial)
initial_lst = cleaned_input(initial_real)
# part1(initial_lst)



GridStack = GridCalc(initial_lst)

while GridStack.minute < 200:
    GridStack.run_minute()
GridStack.sum_bugs()
print("sum", GridStack.sum)
# GridStack.run_minute() #2
# GridStack.run_minute() #3
# GridStack.run_minute() #4
# GridStack.run_minute() #5
# pprint.pprint(GridStack.create_new_grid())
a = 1
