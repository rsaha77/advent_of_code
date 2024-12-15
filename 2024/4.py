import re
import sys

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
direction_diag = [[1, 1], [-1, -1], [-1, 1], [1, -1]]


def print_grid(mark):
  for g in mark:
    print(g)
  print()


def get_xmas_cnt(r, c, R, C, grid):
  cnt = 0
  for dr, dc in direction:
    curr_str = ""
    steps = 0
    nr, nc = r, c
    while ins(nr, nc, R, C) and steps < 4:
      curr_str += grid[nr][nc]
      if curr_str == "XMAS":
        cnt += 1
        break
      nr, nc = nr + dr, nc + dc
      steps += 1
  return cnt


def get_x_mas_cnt(r, c, R, C, grid):
  cnt = 0
  ar, ac = r + 1, c + 1
  br, bc = r - 1, c - 1

  cr, cc = r + 1, c - 1
  dr, dc = r - 1, c + 1

  if ins (ar, ac, R , C) and ins (br, bc, R , C) and ins (cr, cc, R , C) and ins (dr, dc, R , C):
    if grid[ar][ac] + grid [br][bc] in ["MS", "SM"] and grid[cr][cc] + grid [dr][dc] in ["MS", "SM"]:
      return True

  return False


def main():
  ans1, ans2 = 0, 0
  grid = []
  for ln, line in enumerate(LINES):
    grid.append(line)

  R, C = len(grid), len(grid[0])

  for r in range(R):
    for c in range(C):
      if grid[r][c] == 'X':
        ans1 += get_xmas_cnt (r, c, R, C, grid)
      if grid[r][c] == 'A':
        ans2 += get_x_mas_cnt (r, c, R, C, grid)

  print("p1: ", ans1)
  print("p2: ", ans2)

if __name__ == "__main__":
  main()
