import sys
import copy
from collections import deque

sys.setrecursionlimit(100000)

file = "in.txt"
try:
  file = sys.argv[1]
except IndexError:
  pass

inp = open(file).read().strip()
LINES = inp.split('\n')


def keep_alpnum_spaces(text):
  ret = ''.join(ch if ch.isalnum() or ch.isspace() else '' for ch in text)
  return ret

def remove_chars (text, chs):
  ret = ''.join([ch for ch in text if ch not in chs])
  return ret


"""

| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.


  N
W   E
  S


..F7.
.FJ|.
SJ.L7
|F--J
LJ...

"""

directions = [[-1,0], [1,0], [0,1], [0,-1]]


def ins (r, c, R, C):
  return 0 <= r < R and 0 <= c < C


def connects (r, c, so, nr, nc, de):

  # print (so, de)

  if any(x == 'S' for x in [so, de]):
    return True

  # Right
  if (nr, nc) == (r, c+1):
    if so in ['-', 'L', 'F'] and de in ['-', 'J', '7']:
      return True

  # Left
  if (nr, nc) == (r, c-1):
    if de in ['-', 'L', 'F'] and so in ['-', 'J', '7']:
      return True

  # Up
  if (nr,nc) == (r-1, c):
    if so in ['|', 'L','J'] and de in ['|', '7', 'F']:
      return True

  # Down
  if (nr,nc) == (r+1, c):
    if de in ['|', 'L','J'] and so in ['|', '7', 'F']:
      return True

  return False


def dfs_cycle (grid):

  R = len (grid)
  C = len (grid[0])
  sr, sc = 0, 0

  mark_grid = [['.' for _ in range(C)] for _ in range(R)]

  for r in range (R):
    for c in range (C):
      if grid[r][c] == 'S':
        mark_grid [r][c] = 'S'
        sr, sc = r, c

  # print("start")
  # print(sr,sc)
  # print("=============")

  vis = set ()
  cnt = [0]
  plots = []

  def dfs (r, c, par_r, par_c, R, C):
    # Plot has to be in steps
    plots.append((r,c))
    cnt[0] += 1
    # print(cnt[0])
    if par_c >= 0:
      # print (grid [par_r][par_c], grid [r][c])
      mark_grid [r][c] = 'x'
    vis.add((r, c))
    for dr, dc in directions:
      nr = r + dr
      nc = c + dc
      # print (r, c, nr, nc)
      if ins (nr, nc, R, C) and (nr, nc) != (par_r, par_c) and connects(r, c, grid[r][c], nr, nc, grid[nr][nc]):
        if (nr, nc) == (sr, sc):
          # This if condition is not needed. Just used for tracking.
          # print (r, c, nr, nc)
          # print ("Main cycle found from: ", r, c, "to", nr, nc, " -> cnt:", cnt[0]//2)
          return
        if (nr, nc) in vis:
          # print ("cycle found from: ", r, c, "to", nr, nc)
          return
        dfs (nr, nc, r, c, R, C)

  dfs (sr, sc, -1, -1, R, C)

  return plots, cnt[0]


grid = []

for ln,line in enumerate(LINES):
  grid.append (line)

# for g in grid:
  # print(g)

plots, cycle_length = dfs_cycle (grid)

print ("Part 1: ", cycle_length // 2)



for r in range (len(grid)):
  for c in range (len(grid[0])):
    if (r,c) in plots:
      print ('x', end="")
    else:
      print ('.', end="")
  print ()


# I had to use hint for part 2 since it was driving me crazy and found a great one but it will time out in cp contests where you submit your code

# from matplotlib.path import Path
# p2 = 0
# path = Path(plots)
# for y in range(len(grid)):
#   for x in range(len(grid[0])):
#     if (x, y) not in plots and path.contains_point((x, y)):
#       # print(x+1,y+1)
#       p2 += 1

print("Part 2: ", p2)





















