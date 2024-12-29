import re
import sys
from copy import deepcopy
from heapq import heappush as hpush, heappop as hpop
from collections import deque, defaultdict, Counter

file = "in.txt"
try:
    file = sys.argv[1]
except IndexError:
    pass

inp = open(file).read().strip()
LINES = inp.split("\n")

HV_DIR = [[-1, 0], [0, 1], [1, 0], [0, -1]] # ^, >, v, <
HV_DIR_NXT = [[0, -1], [-1, 0],[0, 1], [1, 0]] # <, v, >, ^


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
  (-1, 0): '^',
  (0, 1): '>',
  (1, 0): 'v',
  (0, -1):'<'
}


def get_move_cost(g):
  move_cost = defaultdict(int)
  R = len(g)
  C = len(g[0])
  for r in range(R):
    for c in range(C):
      for nr in range(R):
        for nc in range(C):
          ch1, ch2 = g[r][c], g[nr][nc]
          dist = abs(nr - r) + abs(nc - c) if '#' not in ch1 and '#' not in ch2 else float('inf')
          # dist = 1 if '#' not in ch1 and '#' not in ch2 else float('inf')
          move_cost[ch1+ch2] = move_cost[ch2+ch1] = dist
  return move_cost


def dijkstra_num_kpad (sr, sc, er, ec, grid, R, C):
  pq = []
  dist = {}
  best_cost = float('inf')
  hpush(pq, (0, sr, sc, None, 'A'))

  vis = set()
  best_paths = []
  while pq:
    cost, r, c, drc, path = hpop(pq)

    # print(cost,r,c,drc,path)
    
    if (r,c,drc) in vis:
      continue
    vis.add((r,c,drc))
    
    if (r, c) not in dist:
        dist[(r,c)] = cost
    
    if (r,c) == (er, ec):
      # print(f'cost: {cost}, path: {path}')
      if cost <= best_cost:
        best_paths.append(path+'A')
        best_cost = cost
      continue
    
    for dr, dc in HV_DIR:
      nr, nc = r + dr, c + dc
      if ins(nr, nc, R, C) and grid[nr][nc] != '#':
        ch2 = grid[nr][nc]
        npath = deepcopy(path)
        new_drc = dir_map[(dr,dc)]
        npath += new_drc
        new_cost = cost + (1 if drc in [None, new_drc] else 2)
        # print(drc, new_drc, new_cost)
        hpush(pq, (new_cost, nr, nc, new_drc, npath))

  return best_paths


def dijkstra2(sr, sc, er, ec, grid, R, C, dir_cost, flag=False):
  print("djk")
  DIR = HV_DIR
  if flag:
    DIR = HV_DIR_NXT
  pq = []
  dist = {}
  best_cost = float('inf')
  hpush(pq, (0, sr, sc, 'A', 'A'))

  vis = set()
  best_paths = []
  while pq:
    cost, r, c, ch1, path = hpop(pq)

    # print(cost,r,c,ch1,path)
    
    if (r,c) in vis:
      continue
    vis.add((r,c))
    
    if (r, c) not in dist:
        dist[(r,c)] = cost
    
    if (r,c) == (er, ec):
      return path+'A'
    
    for dr, dc in DIR:
      nr, nc = r + dr, c + dc
      if ins(nr, nc, R, C) and grid[nr][nc] != '#':
        ch2 = grid[nr][nc]
        npath = deepcopy(path)
        drc = dir_map[(dr,dc)]
        npath += drc
        prev_drc = "" if not len(path) else path[-1]
        # print(prev_drc + drc, " -- ", dir_cost[prev_drc + drc])
        # assert dir_cost[prev_drc + drc] == 1
        hpush(pq, (cost + dir_cost[prev_drc + drc], nr, nc, grid[nr][nc], npath))
        # hpush(pq, (cost + 1, nr, nc, grid[nr][nc], npath))

  assert False


def get_start_end (source, target, g, R, C):
  sr,sc,er,ec = (-1,)*4
  for r in range(R):
    for c in range(C):
      if g[r][c] == source:
        sr,sc = r,c
      if g[r][c] == target:
        er, ec = r,c
  assert -1 not in [sr,sc,er,ec]
  return sr,sc,er,ec


from_to = {}

def get_move1(ch1, ch2, num_kpad):
  R, C = len(num_kpad), len(num_kpad[0])
  sr, sc, er, ec = get_start_end (ch1, ch2, num_kpad, R, C)
  curr_best_paths = dijkstra_num_kpad(sr, sc, er, ec, num_kpad, R, C)
  return [path[1:] for path in curr_best_paths]


D = {}
def get_move2(dir_kpad, dir_cost, nums):

  """
  #^A
  <v>
  """

  moves2 = []
  R, C = len(dir_kpad), len(dir_kpad[0])
  for i in range(len(nums) - 1):
    ch1, ch2 = nums[i], nums[i+1]
    if (ch1,ch2) in D:
      moves2.append(D[(ch1,ch2)])
      continue
    sr, sc, er, ec = get_start_end (ch1, ch2, dir_kpad, R, C)
    # print(f'{ch1} -> {ch2}')
    djk = dijkstra2(sr, sc, er, ec, dir_kpad, R, C, dir_cost, True)[1:]
    moves2.append(djk)
    # print(moves2)
    D[(ch1,ch2)] = djk

  moves2 = ''.join(moves2)

  return moves2


def numerical(n):
  return int(''.join(ch for ch in n if ch.isdigit()))


def main():
  ans1, ans2 = 0, 0

  num_kpad = [['7','8','9'], ['4','5','6'], ['1','2','3'], ['#','0','A']]
  dir_kpad = [['#', '^', 'A'], ['<', 'v', '>']]
  num_pad_cost = get_move_cost(num_kpad)
  dir_cost = get_move_cost(dir_kpad)

  print_grid(num_kpad)
  print_grid(dir_kpad)

  print(num_pad_cost)
  print(dir_cost)

  
  for ln, line in enumerate(LINES):
    # print("line: ", line)
    line = 'A' + line
    S = ''
    len_S = 0
    for ch1,ch2 in list(zip(line, line[1:])):
      if (ch1, ch2) in from_to:
        len_S += from_to[(ch1,ch2)]
        continue
      # print()
      print(ch1 + " -> " + ch2)
      move1 = get_move1 (ch1, ch2, num_kpad)
      # print("------------- First Moves: ", move1, ' ------------------')

      s, len_s = '', float('inf')
      for m1 in move1:

        tm = m1
        for robots in range(2):
          tm = get_move2(dir_kpad, dir_cost, 'A' + tm)
          print(robots, len(tm))

        ts = ''.join(tm)

        if len(ts) < len_s:
          s = ts
          len_s = len(ts)

      from_to[(ch1,ch2)] = len_s
      len_S += len(s)
    # print(S, len(S))
    print("********************", numerical (line), len_S, "********************")
    ans1 += numerical (line) * len_S
  print("p1: ", ans1)

if __name__ == "__main__":
  main()





