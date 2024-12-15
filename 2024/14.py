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


HV_DIR = [[-1, 0], [1, 0], [0, 1], [0, -1]]

def print_grid(mark):
  R, C = len(mark), len(mark[0])
  for r in range(R):
    for c in range(C):
      if mark[r][c] == 0:
        print('.',end="")
        continue
      print(mark[r][c],end="")
    print()
  print()


def solve (pr, pc, vr, vc, R, C):
  TOTAL_SIMULATIONS = 100
  npr, npc = (pr + (vr * TOTAL_SIMULATIONS)) % R, (pc + (vc * TOTAL_SIMULATIONS)) % C
  return npr, npc


def get_quad_prods(grid, R, C):
  mdr = R // 2
  mdc = C // 2
  q1, q2, q3, q4 = 0, 0, 0, 0

  for r in range(R):
    for c in range(C):
      cnt = grid[r][c]
      if 0 <= r < mdr and 0 <= c < mdc:
        q1 += cnt
      elif 0 <= r < mdr and mdc < c < C:
        q2 += cnt
      elif mdr < r < R and 0 <= c < mdc:
        q3 += cnt
      elif mdr < r < R and mdc < c < C:
        q4 += cnt

  return q1*q2*q3*q4

def dfs(r, c, R, C, grid, vis):
  vis.add((r,c))
  for dr, dc in HV_DIR:
    nr, nc = r + dr, c + dc
    if ins(nr, nc, R, C) and grid[nr][nc] == '*' and (nr,nc) not in vis:
      dfs(nr,nc,R,C,grid,vis)


def connected_components(grid, R, C):
  cnt = 0
  vis = set()
  for r in range(R):
    for c in range(C):
      if grid[r][c] == '*' and (r,c) not in vis:
        dfs(r,c,R,C,grid,vis)
        cnt += 1
  return cnt

  
def main():
  ans1, ans2 = 0, 0
  R, C = 103, 101
  # R, C = 7, 11
  grid = [[0 for _ in range (C)] for _ in range(R)]
  L = []

  for ln, line in enumerate(LINES):
    p,v = line.split()
    pc, pr = p.split('=')[1].split(',')
    vc, vr = v.split('=')[1].split(',')
    pr, pc, vr, vc = int(pr), int(pc), int(vr), int(vc)
    L.append((pr, pc, vr, vc))
    npr, npc = solve (pr, pc, vr, vc, R, C)
    grid[npr][npc] += 1

  ans1 = get_quad_prods(grid, R, C)
  print(ans1)

  sim = 0
  while True:
    sim += 1
    grid = [['.' for _ in range (C)] for _ in range(R)]
    for i, (pr, pc, vr, vc) in enumerate(L):
      npr, npc = (pr + vr) % R, (pc + vc) % C
      grid[npr][npc] = '*'
      L[i] = (npr, npc, vr, vc)
    if connected_components(grid, R, C) <= len(L)//2:
      print_grid(grid)
      break

  print("p2:", sim)


if __name__ == "__main__":
  main()


