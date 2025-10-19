
# Ugly code, no time to refactor :(
# Was very hard to debug part2 because of a minor and stupid bug
# Was returning when found previous mirror but I just had to continue

"""
Corner case for my bug of part2:

##.#....#
...##...#
...##..##
##.......
.....##..
..#..##..
..##....#
..#..##..
####....#

"""

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


def check_row_reflections (G, vertical, store, mirror_hor=0, mirror_ver=0):
  R = len(G)
  C = len(G[0])

  ret = 0
  for r in range(R):
    GL = G[:r]
    GR = G[r:]
    nl = len(GL)
    nr = len(GR)
    if 0 in [nl, nr]:
      continue
    dx = 0
    cnt = 0
    for j in range (min(nl, nr)):
      if GL[nl - 1 - dx] == GR[dx]:
        dx += 1
        cnt += 1
    if cnt in [nl, nr]:
      # Perfect Mirror Found
      if (vertical and mirror_ver == nl) or (not vertical and mirror_hor == nl):
        # Mirror positioning is exactly same as before
        # Bug which wasted time in p2 = returning instead of continuing
        continue
      ret = nl
      break

  ret *= 1 if vertical else 100
  return ret


def solve (G, vertical=False, p1=False):

  mirror_hor = check_row_reflections(G, vertical=False, store=True)
  TG = list(map(list, zip(*G)))
  mirror_ver = check_row_reflections(TG, vertical=True, store=True)

  if p1:
    return max(mirror_hor, mirror_ver)

  if mirror_hor:
    mirror_hor //= 100

  ret = -1
  for r, g in enumerate(G):
    for c, ch in enumerate(g):
      G[r][c] = '.' if ch == '#' else '#'

      ret = check_row_reflections(G, vertical=False, store=False, mirror_hor=mirror_hor, mirror_ver=-1)
      TG = list(map(list, zip(*G)))
      ret = max (ret, check_row_reflections(TG, vertical=True, store=False, mirror_hor=-1, mirror_ver=mirror_ver))

      if ret > 0:
        return ret

      G[r][c] = ch
  return ret


G = []
ans_p1 = 0
ans_p2 = 0
for ln,line in enumerate(LINES):
  # print (line)
  if len(line) == 0:
    ans_p1 += solve(G, p1=True)
    ans_p2 += solve(G)
    G = []
  else:
    G.append(list(line))

ans_p1 += solve(G, p1=True)
ans_p2 += solve(G)
print (ans_p1)
print (ans_p2)

# 24961 is too low
# 41939 is too high
# 32069 can




























  


