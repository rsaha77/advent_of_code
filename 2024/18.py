import re
import sys
import time
from heapq import heappush as hpush, heappop as hpop
from collections import deque

file = "in.txt"
try:
    file = sys.argv[1]
except IndexError:
    pass


inp = open(file).read().strip()
LINES = inp.split("\n")


def ins(r, c, R, C):
  return 0 <= r < R and 0 <= c < C


HV_DIR = [[-1, 0], [1, 0], [0, 1], [0, -1]]


def bfs(sr, sc, er, ec, grid, R, C):
  q = deque([(0, sr, sc)])
  best_cost = float('inf')

  vis = set()
  while q:
    cost, r, c = q.popleft ()
    
    if (r,c) in vis:
      continue
    vis.add((r,c))
    
    if (r,c) == (er, ec):
      best_cost = cost
      break

    for dr, dc in HV_DIR:
      nr, nc = r + dr, c + dc
      if ins(nr, nc, R, C) and grid[nr][nc] != '#':
       q.append((cost+1, nr, nc))

  return best_cost


def solve1(sr,sc,er,ec,R,C,cors,FALLS):
  grid = [['.' for _ in range(C)] for _ in range(R)]
  for idx in range(FALLS):
    r, c = cors[idx]
    grid[r][c] = '#'
  best_cost = bfs(sr, sc, er, ec, grid, R, C)
  return best_cost


def solve2(sr,sc,er,ec,R,C,cors,FALLS):
  grid = [['.' for _ in range(C)] for _ in range(R)]
  for fall,(r,c) in enumerate(cors):
    grid[r][c] = '#'
    if fall < FALLS:
      continue
    best_cost = bfs(sr, sc, er, ec, grid, R, C)
    if best_cost == float('inf'):
      return (c,r)
  assert(False)


def is_blocked(mid, cors, sr, sc, er, ec, R, C):
  grid = [['.' for _ in range(C)] for _ in range(R)]
  for i in range(mid + 1):
    grid[cors[i][0]][cors[i][1]] = '#'
  if bfs(sr, sc, er, ec, grid, R, C) == float('inf'):
    return True
  return False


def solve2_binary_search(sr,sc,er,ec,R,C,cors,FALLS):
  beg, end = FALLS, len(cors) - 1
  while beg <= end:
    mid = (end + beg) // 2
    if is_blocked(mid, cors, sr, sc, er, ec, R, C):
      end = mid - 1
    else:
      beg = mid + 1
  return cors[beg][1], cors[beg][0]


def main():
  R, C = 71, 71
  sr, sc = 0, 0
  er, ec = 70, 70
  FALLS = 1024

  #---- SAMPLE ----#
  # R, C = 7, 7
  # er, ec = 6, 6
  # FALLS = 12
  #----------------#

  cors = []

  for ln, line in enumerate(LINES):
    c, r = [int(x) for x in line.split(',')]
    cors.append((r,c))

  print("p1: ", solve1(sr,sc,er,ec,R,C,cors,FALLS))
  # print("p2: ", solve2(sr,sc,er,ec,R,C,cors,FALLS)) # ~1.18 secs
  print("p2: ", solve2_binary_search(sr,sc,er,ec,R,C,cors,FALLS)) # ~0.017 secs


if __name__ == "__main__":
  start = time.time()
  main()
  end = time.time()
  print(f"Execution Time: {end - start:.6f} seconds")

"""
Initially used dijkstra from day 16 and got correct answer for p1 and p2
Refactored to bfs (p1) and binary_search + bfs (p2) to optimise
"""

