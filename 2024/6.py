import sys
# import numpy
from graphlib import TopologicalSorter
from itertools import product
from functools import cache
from heapq import heappush as hpush, heappop as hpop
from collections import defaultdict, Counter

# sys.setrecursionlimit(int(1e6))

""" Transposing
tr = list(map(list, zip(*G)))
tr = list(map(list, itertools.zip_longest(*grid, fillvalue=None))) #when one or more lists are empty
"""

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


def show (**kwargs):
    output = ', '.join([f"{key} = {value}" for key, value in kwargs.items()])
    print(output)


def ins(r, c, R, C):
  return 0 <= r < R and 0 <= c < C


# direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
# direction = [[-1, 0], [1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]]

mp = defaultdict(int)
directions = ['up', 'right', 'down', 'left']
dir_map = {
  'up': (-1, 0),
  'right': (0, 1),
  'down': (1, 0),
  'left': (0, -1)
}


def print_grid(mark):
  for g in mark:
    print(g)
  print()


def move_and_turn_90R(r, c, R, C, curr_dir, G):

  dr, dc = dir_map[curr_dir]
  nr, nc = r + dr, c + dc

  if ins(nr, nc, R, C):
    if G[nr][nc] == '#':
      new_dir_idx = (directions.index(curr_dir) + 1) % 4
      new_dir = directions[new_dir_idx]
      dr, dc = dir_map[new_dir]
      r, c = r + dr, c + dc
      # Edge case .. For another # just turn without stepping
      if ins(r,c,R, C) and G[r][c] == '#':
        r, c = r - dr, c - dc
      curr_dir = new_dir
    else:
      r, c = nr, nc

    return r, c, curr_dir

  return -1, -1, -1


def loop_found(gr, gc, R, C, curr_dir, G):
  vis = set()
  mark = [['.' for _ in range(C)] for _ in range (R)]
  for r in range(R):
    for c in range(C):
      mark[r][c] = G[r][c]

  while ins(gr, gc, R, C):
    mark[gr][gc] = '|' if curr_dir in ["up", "down"] else "-"
    if (gr, gc, curr_dir) in vis:
      return True, mark
    vis.add((gr, gc, curr_dir))
    gr, gc, curr_dir = move_and_turn_90R (gr, gc, R, C, curr_dir, G)
  return False, mark


def main():
  ans1, ans2 = 0, 0
  grid = []
  next = defaultdict(list)
  for ln, line in enumerate(LINES):
    grid.append(line)

  R = len(grid)
  C = len(grid[0])
  gr, gc, drc = -1, -1, "up"

  for r in range(R):
    for c in range(C):
      if grid[r][c] == '^':
        gr, gc = r, c

  tgr, tgc, tdrc = gr, gc, drc

  mark = [['_' for _ in range(C)] for _ in range(R)]
  while ins(gr, gc, R, C) and grid[gr][gc] != '#':
    mark [gr][gc] = 'X'
    gr, gc, drc = move_and_turn_90R (gr, gc, R, C, drc, grid)

  ans1 = sum(1 for r in range(R) for c in range(C) if mark[r][c] == 'X' )
  print ("Part 1: ", ans1)

  G = [list(row) for row in grid]
  gr, gc, drc = tgr, tgc, tdrc
  for r in range(R):
    for c in range(C):
      if G[r][c] == '.' and mark[r][c] == 'X':
        G[r][c] = '#'
        is_loop, movements = loop_found (gr, gc, R, C, drc, G)
        if is_loop:
          ans2 += 1
        G[r][c] = '.'

  print("Part 2:", ans2)

  


if __name__ == "__main__":
  main()

