import sys
import numpy
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


def ins(r, c, R, C):
  return 0 <= r < R and 0 <= c < C


direction = [[-1, 0], [1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]]


def good_neighbour (G, R, C, r, c):
  for dr, dc in direction:
    nr = r + dr
    nc = c + dc
    if ins(nr, nc, R, C):
      if (G[nr][nc] != '.' and not G[nr][nc].isdigit()):
        return False
  return True


def generate_gears (G, R, C, r, c):
  for dr, dc in direction:
    nr = r + dr
    nc = c + dc
    if ins(nr, nc, R, C):
      if G[nr][nc] == '*':
        yield (nr, nc)


def main():
  G = []
  for ln, line in enumerate(LINES):
    G.append(line)
  R = len(G)
  C = len(G[0])
  exc = 0
  tot = 0
  p2 = 0
  mp = defaultdict(set)
  for r in range(R):
    s = ""
    ok = True
    gears = []
    for c in range(C):
      ch = G[r][c]
      if ch.isdigit():
        s += ch
        if not good_neighbour (G, R, C, r, c):
          ok = False
        for (gr,gc) in generate_gears(G, R, C, r, c):
          gears.append ((gr, gc))
      else:
        if s:
          tot += int(s)
          for gear in gears:
            mp[gear].add(int(s))
        if ok:
          if s:
            exc += int(s)
        s = ""
        ok = True
        gears = []
    if ok and s:
      exc += int(s)
    if s:
      tot += int(s)
      for gear in gears:
        mp[gear].add(int(s))

  for k,v in mp.items():
    if len(v) == 2:
      p2 += numpy.prod([x for x in v])


  print("p1: ", tot - exc)
  print("p2: ", p2)




if __name__ == "__main__":
  main()























