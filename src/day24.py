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
        self.current_coord_outer = {
            "r": 0,
            "c": 0
        }
        self.full_grid = initial_grid

    def get_above(self,r,c,grid):
        try:
            if r-1 == -1:
                #outside grid
                r_o=self.current_coord_outer['r']
                c_o=self.current_coord_outer['c']
                value = self.outer_grid[r_o-1][c_o]
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
                r_o=self.current_coord_outer['r']
                c_o=self.current_coord_outer['c']
                value = self.outer_grid[r_o+1][c_o]
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
                r_o=self.current_coord_outer['r']
                c_o=self.current_coord_outer['c']
                value = self.outer_grid[r_o][c_o+1]
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
                r_o=self.current_coord_outer['r']
                c_o=self.current_coord_outer['c']
                value = self.outer_grid[r_o][c_o-1]
            else:
                value = grid[r][c-1]
            if type(value) == list:
                value = sum([x[-1] for x in value])
        except:
            value = 0
        return value

    def get_adjacent(self, r, c, grid):
        try:
            # Only defined/used outer exists
            outer_r = self.current_coord_outer['r']
            outer_c = self.current_coord_outer['c']
        except:
            pass
            print("outer not defined")
        # if r == 2 and c == 1:
        #     breakpoint()
        try:
            # catch when looking outside current grids
            if r < 0:
                # above
                value = self.outer_grid[outer_r-1][outer_c]
                if type(value) == list:
                    breakpoint()

            elif r > 4:
                # below
                value = self.outer_grid[outer_r+1][outer_c]
                if type(value) == list:
                    breakpoint()
            elif c < 0:
                # left
                value = self.outer_grid[outer_r][outer_c-1]
                if type(value) == list:
                    breakpoint()
            elif c > 4:
                # right
                value = self.outer_grid[outer_r][outer_c+1]
                if type(value) == list:
                    breakpoint()
            else:
                value = grid[r][c]
        except:
            print(f'Skipping r{r}, c{c}')
            value = 0

        return value

    def get_all_adjacent(self, grid):
        r = self.current_coord_local['r']
        c = self.current_coord_local['c']
        above = self.get_above(r, c, grid,)
        below = self.get_below(r, c, grid)
        left = self.get_left(r, c, grid)
        right = self.get_right(r, c, grid)
        surrounding = [above, right, below, left]
        return surrounding

    def new_bug_state(self, grid):

        r = self.current_coord_local['r']
        c = self.current_coord_local['c']
        current_tile = grid[r][c]
        surrounding = self.get_all_adjacent(grid)
        if type(current_tile) == list:
            self.outer_grid = grid
            self.current_coord_outer['r'] = r
            self.current_coord_outer['c'] = c
            current_tile = self.create_new_grid(current_tile)

        elif current_tile == 1:
            if surrounding.count(1) != 1:
                current_tile = 0
        else:
            if 1 <= surrounding.count(1) <= 2:
                current_tile = 1
        return current_tile

    def run_minute(self):
        self.full_grid = self.create_new_grid()
        self.minute += 1

    def create_new_grid(self, grid=None):
        if grid is None:
            grid = self.full_grid
        new_grid = []
        self.local_grid = grid
        for r, row in enumerate(grid):
            new_row = []
            self.current_coord_local['r'] = r
            for c, col in enumerate(row):
                self.current_coord_local['c'] = c
                new_row.append(self.new_bug_state(grid))
            new_grid.append(new_row)
        return new_grid

    def print_tiles(self, grid):
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                print(col, end='')
            print("")

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
        empty[2][2] = copy.deepcopy(center_grid)

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
    

initial_lst = cleaned_input(initial_real)
part1(initial_lst)

exit()

initial_lst[2][2] = create_empty()
stack = create_empty(initial_lst)

GridStack = GridCalc(stack)

GridStack.run_minute()
# pprint.pprint(GridStack.create_new_grid())
a = 1
