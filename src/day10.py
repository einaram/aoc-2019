import math
import numpy as np

ast_map=""".#..#
.....
#####
....#
...##"""

ast_map = ast_map.split("\n")

ast_coords= []
# map_matrix = np.full([len(ast_map),len(ast_map[0])],99)
for r,row in enumerate(ast_map):
    for c,col in enumerate(row):
        if col == "#":
            point = (r,c)
            ast_coords.append(point)

        # map_matrix[r,c]=point

print(ast_coords)

for station_coord in ast_coords:
    for ast in ast_coords:
        


        
