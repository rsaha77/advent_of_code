import re
import sys
import copy

file = "in.txt"
try:
    file = sys.argv[1]
except IndexError:
    pass


inp = open(file).read().strip()
LINES = inp.split("\n")


def ins(r, c, R, C):
  return 0 <= r < R and 0 <= c < C

def print_grid(mark):
  R, C = len(mark), len(mark[0])
  for r in range(R):
    for c in range(C):
      print(mark[r][c], end="")
    print()
  print()


directions = ['^', '>', 'v', '<']
dir_map = {
  '^': (-1, 0),
  '>': (0, 1),
  'v': (1, 0),
  '<': (0, -1)
}


def move_small_boxes (r, c, grid, movement, R, C):
  for drc in movement:
    dr, dc = dir_map[drc]
    nr, nc = r + dr, c + dc
    if not ins(nr, nc, R, C) or grid[nr][nc] == '#':
      pass
    elif grid[nr][nc] == '.':
      grid[nr][nc] = '@'
      grid[r][c] = '.'
      r, c = nr, nc
    elif grid[nr][nc] == 'O':
      while grid[nr][nc] == 'O':
        nr, nc = nr+dr, nc+dc
      if grid[nr][nc] == '.':
        while True:
          grid[nr][nc] = grid[nr-dr][nc-dc]
          grid[nr-dr][nc-dc] = '.'
          nr,nc = nr-dr, nc-dc
          if (nr,nc) == (r,c):
            break
        r,c = r+dr, c+dc
    # print_grid(grid)
    # input("Press Enter to continue..")
  return grid


def expand_grid(grid, R, C):
  nC = C*2
  nGrid = [['-' for _ in range(nC)] for _ in range(R)]
  for r in range(R):
    for c in range(C):
      ch = grid[r][c]
      ch1, ch2 = '-', '-'
      if ch in ['#', '.']:
        ch1, ch2 = ch, ch
      elif ch == 'O':
        ch1, ch2 = '[', ']'
      elif ch == '@':
        ch1, ch2 = '@', '.'
      nGrid[r][c*2] = ch1
      nGrid[r] [c*2 + 1] = ch2
  return nGrid, R, nC


def dfs(r, c, dr, dc, grid, vis):
  ret = True
  vis.add((r,c))
  nr, nc = r+dr, c+dc
  if grid[nr][nc] == '#':
    return False
  if (nr,nc) not in vis:
    if grid[nr][nc] == '[':
      return ret and dfs(nr, nc, dr, dc, grid, vis) and dfs (nr, nc+1, dr, dc, grid, vis)
    elif grid[nr][nc] == ']':
      return ret and dfs(nr, nc, dr, dc, grid, vis) and dfs(nr, nc-1, dr, dc, grid, vis)
  return ret


def move_big_boxes(r, c, grid, movement, R, C):
  for drc in movement:
    dr, dc = dir_map[drc]
    nr, nc = r + dr, c + dc
    assert(ins(nr, nc, R, C))
    if grid[nr][nc] == '#':
      continue
    elif grid[nr][nc] == '.':
      grid[nr][nc] = '@'
      grid[r][c] = '.'
      r, c = nr, nc
    elif grid[nr][nc] in ['[', ']']:
      vis = set()
      can_move = dfs(r, c, dr, dc, grid, vis)
      if can_move:
        vis = sorted(vis)
        if drc in  ['v', '>']:
          vis = reversed(vis)
        for rr,cc in vis:
          nr, nc = rr+dr, cc+dc
          grid[nr][nc] = grid[rr][cc]
          grid[rr][cc] = '.'
          r,c = nr,nc
    # print_grid(grid)
    # input("Press Enter to continue..")
  return grid


def get_robot_pos (grid, R, C):
  for r in range(R):
    for c in range(C):
      if grid[r][c] == '@':
        return (r, c)
  raise Exception("No Robot Found")


def gps_sum(grid, R, C, target):
  cnt = 0
  for r in range(R):
    for c in range(C):
      if grid[r][c] == target:
        cnt += 100*r + c
  return cnt


def solve1(grid, movement, R, C):
  pr, pc = get_robot_pos(grid, R, C)
  grid = move_small_boxes(pr, pc, grid, movement, R, C)
  return gps_sum(grid, R, C, 'O')


def solve2(grid, movement, R, C):
  grid, R, C = expand_grid (grid, R, C)
  pr, pc = get_robot_pos(grid, R, C)
  grid = move_big_boxes(pr, pc, grid, movement, R, C)
  return gps_sum(grid, R, C, '[')
  

def main():
  ans1, ans2 = 0, 0
  nxt = False
  grid = []
  movement = ""
  for ln, line in enumerate(LINES):
    if len(line) == 0:
      nxt = True
      continue
    if not nxt:
      grid.append([x for x in line])
    else:
      movement += line

  print_grid(grid)
  print(line)

  R, C = len(grid), len(grid[0])
  Tgrid = copy.deepcopy(grid)

  print("p1: ", solve1(grid, movement, R, C))
  grid = Tgrid
  print("p2: ", solve2(grid, movement, R, C))


if __name__ == "__main__":
  main()










