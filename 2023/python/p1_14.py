import sys
from collections import defaultdict, Counter

file = "in.txt"
try:
  file = sys.argv[1]
except IndexError:
  pass

inp = open(file).read().strip()
LINES = inp.split('\n')


grid = []
for ln,line in enumerate(LINES):
  grid.append([*line])

R = len(grid)
C = len(grid[0])

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

ans = 0
for r in range(R):
  for c in range(C):
    ch = grid[r][c]
    if ch == 'O':
      ans += R - r
    elif ch == '.':
      for rr in range (r + 1, R):
        if grid [rr][c] in ['#', 'O']:
          if grid [rr][c] == 'O':
            ans += R - r
            grid [r][c] = 'O'
            grid [rr][c] = '.'
          break

print(ans)
























