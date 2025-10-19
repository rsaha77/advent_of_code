import sys
import itertools
from collections import defaultdict, Counter

file = "in.txt"
try:
  file = sys.argv[1]
except IndexError:
  pass

inp = open(file).read().strip()
LINES = inp.split('\n')


"""
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""

def rotate_grid_90_clockwise(grid):
  transposed_grid = list(map(list, zip(*grid)))
  rotated_grid = [row[::-1] for row in transposed_grid]
  return rotated_grid

def move_north(grid):
  R = len(grid)
  C = len(grid[0])
  ans = 0
  for r in range(R):
    for c in range(C):
      ch = grid[r][c]
      if ch == 'O':
        ans += R - r
      elif ch == '.':
        for rr in range (r + 1, R):
          if grid [rr][c] == 'O':
            ans += R - r
            grid [r][c] = 'O'
            grid [rr][c] = '.'
            break
          elif grid [rr][c] == '#':
            break
  return ans



grid = []
for ln,line in enumerate(LINES):
  grid.append([*line])
  print(grid[-1])


t = 0
total_load = 0
while t < 100:
  for _ in range(4):
    load = move_north(grid)
    grid = rotate_grid_90_clockwise(grid)
    total_load += load
    print(load)
  print()
  t += 1


# ans1 = move_north(grid)

# print("p1:", ans1)

# for g in grid:
#   print(g)

# print()

# grid = rotate_grid_90_clockwise(grid)

# for g in grid:
#   print(g)


























