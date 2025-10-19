import itertools
from itertools import zip_longest

grid = [
    ['1', '.', '#', '#', '.', '.', '#', '#', '.'],
    ['2', '.', '#', '.', '#', '#', '.', '#', '.'],
    ['3', '#', '.', '.', '.', '.', '.', '.', '#'],
    ['4', '#', '.', '.', '.', '.', '.', '.', '#'],
    ['5', '.', '#', '.', '#', '#', '.', '#', '.'],
    ['6', '.', '#', '#', '.', '.', '#', '#', '.'],
    ['7', '.', '#', '.', '#', '#', '.', '#', '.'],
]

# print ("hello")
# # Use zip to transpose the grid, including the empty row
# tr = list(map(list, zip(*grid)))
# # tr = list(map(list, itertools.zip_longest(*grid, fillvalue=None)))


# # Display the transposed grid
# for row in tr:
#     print(row)


print (grid[:3])
print (grid[3:])


