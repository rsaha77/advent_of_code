import re
import sys
import random
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
        hpush(pq, (new_cost, nr, nc, new_drc, npath))

  return best_paths


def get_move1(ch1, ch2, num_kpad):
  R, C = len(num_kpad), len(num_kpad[0])
  sr, sc, er, ec = get_start_end (ch1, ch2, num_kpad, R, C)
  curr_best_paths = dijkstra_num_kpad(sr, sc, er, ec, num_kpad, R, C)
  curr_best_paths = [path[1:] for path in curr_best_paths]
  return curr_best_paths


def dijkstra_dir_kpad(sr, sc, er, ec, grid, R, C, dir_cost):
  # print("djk")
  pq = []
  dist = {}
  best_cost = float('inf')
  hpush(pq, (0, sr, sc, 'A', 'A'))

  vis = set()
  best_path = None
  while pq:
    cost, r, c, drc, path = hpop(pq)

    # print("--------------", cost,r,c,drc,path)
    
    if (r,c,drc) in vis:
      continue
    vis.add((r,c,drc))
    
    if (r, c) not in dist:
        dist[(r,c)] = cost
    
    if (r,c) == (er, ec):
      # return path + 'A'
      path += 'A'
      cost += dir_cost[drc+'A']
      if cost < best_cost:
        best_path = path
        best_cost = cost

      if cost == best_cost:
        random_number = random.randint(1, 20)
        if random_number & 1: # Funny part
          best_path = path
      continue
    
    for dr, dc in HV_DIR_NXT:
      nr, nc = r + dr, c + dc
      if ins(nr, nc, R, C) and grid[nr][nc] != '#':
        ch2 = grid[nr][nc]
        npath = deepcopy(path)
        new_drc = dir_map[(dr,dc)]
        npath += new_drc
        hpush(pq, (cost + dir_cost[drc + new_drc], nr, nc, new_drc, npath))

  return best_path


# nxt = {} # next set of moves after ch1->ch2
nxt = {'A^': '<A', '^^': 'A', '^<': 'v<A', '<A': '>>^A', 'A<': 'v<<A', 'AA': 'A', 'Av': '<vA', 'v<': '<A', 'A>': 'vA', '>>': 'A', '>^': '<^A', '^A': '>A', '<^': '>^A', '<<': 'A', '>A': '^A', 'v>': '>A', '<v': '>A', 'vA': '^>A', '>v': '<A', '^>': 'v>A', 'vv': 'A'}
#The hardcoded value of nxt via dijkstra works for all inputs and is faster than DP with dijkstra
#Ran it multiple times to get min for p1 and p2, and hence optimal nxt

"""
Below is the best nxt found after getting the best_ans / correct_ans
nxt = {'A^': '<A', '^^': 'A', '^<': 'v<A', '<A': '>>^A', 'A<': 'v<<A', 'AA': 'A', 'Av': '<vA', 'v<': '<A', 'A>': 'vA', '>>': 'A', '>^': '<^A', '^A': '>A', '<^': '>^A', '<<': 'A', '>A': '^A', 'v>': '>A', '<v': '>A', 'vA': '^>A', '>v': '<A', '^>': 'v>A', 'vv': 'A'}

The following moves of cost:3 are the tricky ones
'<A': '>>^A'
'A<': 'v<<A'

"""

def move_it (dir_kpad, dir_cost, N, D):
  R, C = len(dir_kpad), len(dir_kpad[0])
  for rbt_num in range(N):
    nD = defaultdict(int)
    for k,v in D.items():
      ch1, ch2 = k[0],k[1]
      if ch1+ch2 not in nxt:
        sr, sc, er, ec = get_start_end (ch1, ch2, dir_kpad, R, C)
        djk = dijkstra_dir_kpad (sr, sc, er, ec, dir_kpad, R, C, dir_cost)
        djk = djk[1:]
        nxt[ch1+ch2] = djk
      prev_ch = 'A'
      for ch in nxt[ch1+ch2]:
        nD[prev_ch + ch] += D[ch1+ch2]
        prev_ch = ch
    D = nD
    ret = 0
    for k,v in D.items():
      ret += v
  return ret



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


def numerical(n):
  return int(''.join(ch for ch in n if ch.isdigit()))


def main():

  num_kpad = [['7','8','9'], ['4','5','6'], ['1','2','3'], ['#','0','A']]
  dir_kpad = [['#', '^', 'A'], ['<', 'v', '>']]
  num_pad_cost = get_move_cost(num_kpad)
  dir_cost = get_move_cost(dir_kpad)

  # print_grid(num_kpad)
  # print_grid(dir_kpad)

  best_ans1, best_ans2 = float('inf'), float('inf')
  ans1, ans2 = 0, 0

  REPS = 1 # Need to increase it if we do not have the optimal value of nxt
  for _ in range(REPS):
    for part in ['p1', 'p2']:
      for ln, line in enumerate(LINES):
        line = 'A' + line
        tot = 0
        for ch1,ch2 in list(zip(line, line[1:])):
          move1 = get_move1 (ch1, ch2, num_kpad)
          mn = float('inf')

          for i,mv1 in enumerate(move1):
            # print("mv1: ", mv1)
            D = defaultdict(int)
            prev = 'A'
            for ch in mv1:
              D[prev+ch] += 1
              prev = ch

            NUM_ROBOTS = 2 if part == "p1" else 25
            mn = min (mn, move_it(dir_kpad, dir_cost, NUM_ROBOTS, D))

          tot += mn

        # print("=======================", numerical (line), tot, "==========================")
        if part == "p1":
          ans1 += numerical (line) * tot
        else:
          ans2 += numerical (line) * tot

    best_ans1 = min(best_ans1, ans1)
    best_ans2 = min(best_ans2, ans2)

  # print("===========================================================")
  # sorted_nxt = sorted(nxt.items(), key=lambda item: len(item[1]), reverse=True)
  # for k, v in sorted_nxt:
  #   print(f"{k}: {v}")

  print("p1: ", best_ans1)
  print("p2: ", best_ans2)

if __name__ == "__main__":
  main()


# Before we know optimal nxt ... needed to run below ..
# 156412136415172 is too low (tried with N = 24)
# 191139369248202 (AC!)
# 216789225827842 ??
# 217914284523602 (WA)
# 218917999117732 cannot
# 224157261790290 cannot
# 351815457990646 cannot
# 359631515231422 (WA)
# 361978551477642 (WA)
# 376870341498810 is too high (It got better by choosing best path for dijkstra_dir_kpad)
# 401684331740594 is too high for N = 25

