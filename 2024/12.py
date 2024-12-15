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
DIAG_DIR = [[1, 1], [-1, -1], [-1, 1], [1, -1]]
ALL_DIR = HV_DIR + DIAG_DIR


def print_grid(mark):
  R, C = len(mark), len(mark[0])
  for r in range(R):
    for c in range(C):
      print(mark[r][c],end="")
    print()
  print()


def dfs(ch, r, c, R, C, grid, mark, vis):
  vis.add((r,c))
  mark[r][c] = 'X'
  for dr, dc in HV_DIR:
    nr, nc = r + dr, c + dc
    if ins(nr, nc, R, C) and (nr,nc) not in vis and grid[nr][nc] == ch:
      dfs(ch, nr, nc, R, C, grid, mark, vis)
  return mark


def get_perimeter(mark, R, C):
  cnt = 0
  #down
  for c in range(C):
    for r in range(R):
      if r in [0] and mark[r][c] == 'X':
        cnt += 1
      elif mark[r][c] == 'X' and mark[r-1][c] != 'X':
        cnt += 1
      # print("r, c, cnt: ", r, c, cnt)

  #up
  for c in range(C):
    for r in range(R - 1, -1, -1):
      if r in [R-1] and mark[r][c] == 'X':
        cnt += 1
      elif mark[r][c] == 'X' and mark[r+1][c] != 'X':
        cnt += 1


  #right
  for r in range(R):
    for c in range(C):
      if c in [0] and mark[r][c] == 'X':
        cnt += 1
        continue
      if mark[r][c] == 'X' and mark[r][c-1] != 'X':
        cnt += 1

  #left
  for r in range(R):
    for c in range(C - 1, -1, -1):
      if c in [C-1] and mark[r][c] == 'X':
        cnt += 1
        continue
      if mark[r][c] == 'X' and mark[r][c+1] != 'X':
        cnt += 1

  return cnt


def get_sides(mark, R, C):
  M = []
  R, C = R+2, C+2
  for r in range(R):
    L = []
    for c in range(C):
      if 0 <= r-1 < R-2 and 0 <= c-1 < C-2:
        L.append(mark[r-1][c-1])
      else:
        L.append('O')
    M.append(L)
 
  mark = M

  # Scan horizontal lines
  hor_sides = 0
  for r in range(1, R):
    prev = "00"
    for c in range(1, C):
      add = mark[r][c] + mark[r-1][c]
      if add in ["XO", "OX"] and add != prev:
        hor_sides += 1
      prev = add

  # Scan vertical lines
  ver_sides = 0
  for c in range(1, C):
    prev = "00"
    for r in range(1, R):
      add = mark[r][c] + mark[r][c-1]
      if add in ["XO", "OX"] and add != prev:
        ver_sides += 1
      prev = add


  return hor_sides + ver_sides



def main():
  ans1, ans2 = 0, 0
  grid = []
  for ln, line in enumerate(LINES):
    grid.append(line)
  R, C = len(grid), len(grid[0])
  vis = set()
  for r in range(R):
    for c in range(C):
      mark = [['O' for _ in range(C)] for _ in range(R)]
      if (r,c) not in vis:
        mark = dfs(grid[r][c], r,c,R,C,grid, mark, vis)
        cnt = sum(mark[i][j] == 'X' for i in range(R) for j in range(C))
        ans1 += cnt * get_perimeter(mark, R, C)
        ans2 += cnt * get_sides(mark, R, C)

  print("part 1: ", ans1)
  print("part 2: ", ans2)

  
if __name__ == "__main__":
  main()






















