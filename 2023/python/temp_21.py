import sys
from itertools import chain
from collections import defaultdict, Counter

# sys.setrecursionlimit(10000)

#tr = list(map(list, zip(*G)))
#tr = list(map(list, itertools.zip_longest(*grid, fillvalue=None))) #when one or more lists are empty, the above won't work

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

def ins (r, c, R, C):
  return 0 <= r < R and 0 <= c < C

direction = [[-1,0], [1,0], [0,1], [0,-1]]
mp = defaultdict (int)


grid = []
sr,sc = 0,0
for ln,line in enumerate(LINES):
  grid.append(line)
  for c,ch in enumerate(line):
    if ch == 'S':
      sr,sc = ln,c


steps = 0
R,C = len(grid), len(grid[0])
curr_loc = set()
curr_loc.add ((sr,sc))
step_grid = [['_' for bar in range(C)] for foo in range(R)]

while steps < 64:
  steps += 1
  new_loc = set()
  for r,c in curr_loc:
    for dr,dc in direction:
      nr,nc = r+dr, c+dc
      if ins(nr, nc, R, C) and grid[nr][nc] in ['.', 'S']:
        step_grid[nr][nc] = 'O'
        new_loc.add((nr,nc))
      step_grid[r][c] = '_'
  curr_loc = new_loc

  for g in step_grid:
    print(g)
  print()


print(sum (1 for row in step_grid for ch in row if ch == 'O'))


















