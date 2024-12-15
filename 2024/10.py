import re
import sys
from collections import defaultdict, Counter

# sys.setrecursionlimit(int(1e6))


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


def dfs (r, c, R, C, grid, vis, p2=False):
  vis.add((r,c))
  count = 1 if grid[r][c] == 9 else 0
  for dr,dc in HV_DIR:
    nr = r + dr
    nc = c + dc
    if ins(nr, nc, R, C):
      if p2 == False and (nr,nc) in vis:
        continue
      if grid[nr][nc] == grid[r][c] + 1:
        count += dfs (nr, nc, R, C, grid, vis, p2)
  return count


def main():
  ans1, ans2 = 0, 0
  grid = []
  for ln, line in enumerate(LINES):
    grid.append([int (x) for x in line])
  R, C = len(grid), len(grid[0])

  for r in range(R):
    for c in range(C):
      if grid[r][c] == 0:
        vis = set()
        ans1 += dfs(r, c, R, C, grid, vis)
        ans2 += dfs(r, c, R, C, grid, vis, p2=True)

  print(ans1, ans2)

if __name__ == "__main__":
  main()

