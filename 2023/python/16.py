import sys
from collections import defaultdict, Counter

sys.setrecursionlimit(int(1e6))

file = "in.txt"
try:
    file = sys.argv[1]
except IndexError:
    pass

inp = open(file).read().strip()
LINES = inp.split("\n")


def keep_alpnum_spaces(text):
  ret = "".join(ch if ch.isalnum() or ch.isspace() else "" for ch in text)
  return ret


def remove_chars(text, chs):
  ret = "".join([ch for ch in text if ch not in chs])
  return ret


def ins(r, c, R, C):
  return 0 <= r < R and 0 <= c < C


direction = {
"right": (0, 1),
"left": (0, -1),
"up": (-1, 0),
"down": (1, 0)
}


def get_new_ways (way, nr, nc, ch):
  ways = []

  if way == "right":
    if ch == '|':
      ways.append("up")
      ways.append("down")
    elif ch == '\\':
      ways.append("down")
    elif ch == '/':
      ways.append("up")
    elif ch in ['-', '.']:
      ways.append(way)

  elif way == "left":
    if ch == '|':
      ways.append("up")
      ways.append("down")
    elif ch == '\\':
      ways.append("up")
    elif ch == '/':
      ways.append("down")
    elif ch in ['-', '.']:
      ways.append(way)

  elif way == "up":
    if ch == '-':
      ways.append("left")
      ways.append("right")
    elif ch == '\\':
      ways.append("left")
    elif ch == '/':
      ways.append("right")
    elif ch in ['|', '.']:
      ways.append(way)

  elif way == "down":
    if ch == '-':
      ways.append("left")
      ways.append("right")
    elif ch == '\\':
      ways.append("right")
    elif ch == '/':
      ways.append("left")
    elif ch in ['|', '.']:
      ways.append(way)

  else:
    assert(False)

  return ways


def dfs (grid, G, R, C, r, c, way, vis):
  vis.add((r,c,way))
  G[r][c] = '#'

  new_ways = get_new_ways (way, r, c, grid[r][c])
  for nway in new_ways:
    dr, dc = direction[nway]
    nr = r + dr
    nc = c + dc
    if ins(nr, nc, R, C) and (nr, nc, nway) not in vis:
      dfs (grid, G, R, C, nr, nc, nway, vis)


def get_ans (grid, r, c, way):
  R, C = len(grid), len(grid[0])
  G = [['.' for c in range(C)] for r in range(R)]
  vis = set()
  dfs (grid, G, R, C, r, c, way, vis)
  return sum (1 for g in G for ch in g if ch == '#')


def solve (grid, p1=False):
  if p1:
    return get_ans(grid, 0, 0,"right")
  else:
    ans = 0
    R, C = len(grid), len(grid[0])
    for c in range(C-1):
      ans = max (ans, get_ans(grid, 0, c,"down"))
      ans = max (ans, get_ans(grid, R-1, c,"up"))
    for r in range(R-1):
      ans = max (ans, get_ans(grid, r, 0,"right"))
      ans = max (ans, get_ans(grid, r, C-1,"left"))
    return ans


def main():
  grid = []
  for ln, line in enumerate(LINES):
    grid.append(line)
  print("p1:", solve (grid, True))
  print("p2:", solve (grid))





# Time: 27 + 27 + 20 + 20 + 20 ....
# Fun part 1
# Realised need to find a loop
# Finding a loop only with (r,c) and struggled for almost an hour. Dissapointed.
# Kept visualising the grid to find out that loop need to be found out with (r,c,dir)
# sample passed but input failed. 5453 is too low!
# Tried the below test case and it failed. (verified with jp code)

"""
\.......................|..../
................./.......-...\
..............................
../.............|......\......
................./.....|......
............................-.
.......................-.|....
........-../...../...........|
\...................\.../.....
..../......\........-.........

Bug was in below line 
if (nr, nc, way) not in vis:
-> Was using "way" instead of "nway"
-> Use more meaningful variables
-> Prefer to run through code instead of generating test cases

"""

if __name__ == "__main__":
  main()
