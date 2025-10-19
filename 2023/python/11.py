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


def keep_alpnum_spaces(text):
  ret = ''.join(ch if ch.isalnum() or ch.isspace() else '' for ch in text)
  return ret

def remove_chars (text, chs):
  ret = ''.join([ch for ch in text if ch not in chs])
  return ret

def expand_grid (grid):
  """
  Not required in this question.
  Required if needed to traverse the modified grid
  Method used to make copies of rows and cols.
  Takes 2D string as argument and returns 2D list
  - Dont use R and C for looping as the grid expands
  - Dont change r and c inside the loop and istead use dr, dc, as loop var (r / c) would be affected
  """

  G = [[ch for ch in row] for row in grid]

  # Row scan
  dr = 0
  # len(G) changes during loop execution if there are row copies
  for r in range(len(G)):
    ok = True
    for c in range(len(G[0])):
      nr = r + dr
      if G[nr][c] == '#':
        ok = False
        break
    if ok:
      G = G[:nr] + [G[nr]] + G[nr:]
      dr += 1

  # Col scan
  dc = 0
  # len(G[0]) changes during loop execution if there are col copies
  for c in range(len(G[0])):
    ok = True
    nc = c + dc
    for r in range(len(G)):
      if G [r][nc] == '#':
        ok = False
        break
    if ok:
      nG = []
      for row_num, row in enumerate(G):
        new_row = row[:nc] + [row[nc]] + row[nc:]
        nG.append(new_row)
      G = nG
      dc += 1

  return G


# Solution starts

grid = []
for ln,line in enumerate(LINES):
  grid.append(line)

# for g in grid:
#   print (g)

# exp_grid = expand_grid(grid)
# for g in exp_grid:
#   print (g)


def solve (grid, expand):
  expand -= 1
  R = len (grid)
  C = len (grid[0])
  rows, cols = [], []

  # rows
  for r in range(R):
    ok = True
    for c in range(C):
      if grid[r][c] == '#':
        ok = False
        break
    if ok:
      rows.append(r)

  #cols
  for c in range(C):
    ok = True
    for r in range(R):
      if grid[r][c] == '#':
        ok = False
        break
    if ok:
      cols.append(c)


  galaxy = []
  for r in range (R):
    dr = sum (1 for rr in rows if rr < r)
    for c in range (C):
      dc = sum (1 for cc in cols if cc < c)
      if grid[r][c] == '#':
        galaxy.append((r + dr*expand, c + dc*expand))


  ans = 0
  for (r, c), (rr, cc) in itertools.combinations(galaxy, 2):
    ans += abs(rr - r) + abs(cc - c)

  return ans

print ("Part 1:", solve (grid, expand=2))
print ("Part 2:", solve (grid, expand=int(1e6)))




























