import math
# import numpy as np
from collections import OrderedDict
ast_map34="""
.#..#
.....
#####
....#
...##
"""

ast_map5_8=\
"""......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####"""

ast_map1_2=\
"""#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###."""

# map_file = r"\day10_test1.txt"
map_file = r"\day10.txt"

with open(r"resources"+ map_file) as infile:
    data = infile.readlines()
data = [x.strip() for x in data]
ast_map = data

ast_coords= []
for r,row in enumerate(ast_map):
    for c,col in enumerate(row):
        if col == "#":
            point = (r,c)
            ast_coords.append(point)

seen_per_ast = {}
seen_per_ast_lst = []
for station_coord in ast_coords:
    # print(station_coord)
    seen = []
    for ast in ast_coords:
        
        if not  station_coord == ast:
            dx = ast[0] - station_coord[0]
            dy = ast[1] - station_coord[1]            
            seen.append(math.atan2(dy,dx))
            # print(seen)
    seen_per_ast[station_coord] = seen
    seen_per_ast_lst.append(len(set(seen)))

a = 12
# ast_coords[ma]
max_index = seen_per_ast_lst.index(max(seen_per_ast_lst))

max_coord = ast_coords[max_index]

print(len(set(seen_per_ast[max_coord]))) #326
print(max_coord[1], max_coord[0]) #22 28


#part 2

all_targets = seen_per_ast[max_coord]

all_targets_uniq = list(set(all_targets))
all_targets_uniq.sort()
#TODO
# nr_200 = all_targets_uniq[199]
# print(nr_200)


        
