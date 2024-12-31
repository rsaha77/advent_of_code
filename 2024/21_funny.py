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
        # print(drc, new_drc, new_cost)
        hpush(pq, (new_cost, nr, nc, new_drc, npath))

  return best_paths


def dijkstra2(sr, sc, er, ec, grid, R, C, dir_cost):
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
      # print("check: ", cost, dir_cost[drc+'A'])
      cost += dir_cost[drc+'A']
      # print(path)
      # print(cost, best_cost)
      if cost < best_cost:
        best_path = path
        best_cost = cost

      if cost == best_cost:
        # if dir_cost [path[0]+path[1]] + dir_cost[path[-2]+path[-1]] < dir_cost [best_path[0]+best_path[1]] + dir_cost[best_path[-2]+best_path[-1]]:
        # if dir_cost [path[-2]+path[-1]] < dir_cost [best_path[-2]+best_path[-1]]:
        random_number = random.randint(243, 4612)
        if random_number & 1:
          best_path = path
      continue
    
    for dr, dc in HV_DIR_NXT:
      nr, nc = r + dr, c + dc
      if ins(nr, nc, R, C) and grid[nr][nc] != '#':
        ch2 = grid[nr][nc]
        npath = deepcopy(path)
        new_drc = dir_map[(dr,dc)]
        npath += new_drc
        # print("drc-new_drc: ", drc, new_drc)
        # print(drc + new_drc, " -- ", dir_cost[drc + new_drc])
        # assert dir_cost[drc + new_drc] == 1
        hpush(pq, (cost + dir_cost[drc + new_drc], nr, nc, new_drc, npath))

  return best_path



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


def get_move1(ch1, ch2, num_kpad):
  R, C = len(num_kpad), len(num_kpad[0])
  sr, sc, er, ec = get_start_end (ch1, ch2, num_kpad, R, C)
  curr_best_paths = dijkstra_num_kpad(sr, sc, er, ec, num_kpad, R, C)
  curr_best_paths = [path[1:] for path in curr_best_paths]
  # print("curr_best_paths")
  # print(curr_best_paths)
  return curr_best_paths


"""
D = {
  "A<": 432,
  "<^": 511211,
  .
  .
}


    +---+---+
  # | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+

nxt = {
  "A<": {'<': 2, 'v': 1, 'A':1}, # "<v<A" .. we should be able to reach from each pair to each other 
  "Av": {},
  "A>": {},
  "A^": {},
  "<^": {'>'': 1, '^'':1 'A': 1} # ">^A"
  .
  .
  .
  "":
}

"""
nxt = defaultdict(str) # next set of moves after ch1->ch2
def move_it (dir_kpad, dir_cost, N, D):
  # print("\nstart move_it fn ---------------------------------------------------")
  # print("Total Moves: ", N)
  # print("D: ", D)
  # print("nxt: ", nxt)
  R, C = len(dir_kpad), len(dir_kpad[0])
  for rbt_num in range(N):
    # print()
    # print("Robot Number: ", rbt_num+2)
    nD = defaultdict(int)
    for k,v in D.items():
      # print("k,v: ", k,v)
      ch1, ch2 = k[0],k[1]
      # we already know what are the next set of moves for ch1->ch2
      if len(nxt[ch1+ch2]) > 0: 
        # print("already have nxt: ", nxt)
        prev_ch = 'A'
        for ch in nxt[ch1+ch2]: # example: ch1+ch2 (note A< is just one character (from -> to)ie; < ... = A< (next move: "<v<A") and nk,nv = {'<': 2, 'v': 1, 'A':2} .. < = A to ^ .. < = v to <
          nD[prev_ch + ch] += D[ch1+ch2]
          prev_ch = ch
      else:
        sr, sc, er, ec = get_start_end (ch1, ch2, dir_kpad, R, C)
        # print(f'{ch1} -> {ch2}')
        djk = dijkstra2(sr, sc, er, ec, dir_kpad, R, C, dir_cost)
        djk = djk[1:]
        # print("djk: ", djk)
        prev_ch = 'A'
        for ch in djk:
          nD[prev_ch + ch] += D[ch1+ch2]
          prev_ch = ch
        nxt[ch1+ch2] = djk
        # print("nxt: ", nxt)
      # print("nD: ", nD)
    D = nD
    # print("robot: ", rbt_num+2)
    # print("Whats in D?")
    # print(D)
    ret = 0
    for k,v in D.items():
      # print (k, v)
      ret += v
    # print(rbt_num+2, ret)
    # print('---------------')

  return ret


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

  # print(num_pad_cost)
  # print(dir_cost)

  
  for ln, line in enumerate(LINES):
    # print("line: ", line)
    line = 'A' + line
    tot = 0
    for ch1,ch2 in list(zip(line, line[1:])):
      # print()
      # print(ch1 + " -> " + ch2)
      move1 = get_move1 (ch1, ch2, num_kpad)
      # print("move1: ", move1)
      mn = float('inf')

      # move1=['vA']

      for i,mv1 in enumerate(move1):
        # print("mv1: ", mv1)
        D = defaultdict(int) # total number of moves of type ch1->ch2 for all combs
        prev = 'A'
        for ch in mv1:
          D[prev+ch] += 1
          prev = ch

        # print("robot: 1")
        # print("initial D: ", D)
        NUM_ROBOTS = 25
        ##################### SAMPLE ###################
        # NUM_ROBOTS = 2
        ################################################
        mn = min (mn, move_it(dir_kpad, dir_cost, NUM_ROBOTS, D))

      tot += mn

    # print("=======================", numerical (line), tot, "==========================")
    ans1 += numerical (line) * tot
  print("p1: ", ans1)

if __name__ == "__main__":
  main()

# 156412136415172 is too low (N = 24)
# 191139369248202 (AC!)
# 216789225827842 ??
# 217914284523602 (WA)
# 218917999117732 cannot
# 224157261790290 cannot
# 351815457990646 cannot
# 359631515231422 (WA)
# 361978551477642 (WA)
# 376870341498810 is too high (It got better by choosing best path for dijkstra 2)
# 401684331740594 is too high (N = 25)

