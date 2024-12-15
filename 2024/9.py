import re
import sys
# import numpy
from copy import deepcopy
import math
from graphlib import TopologicalSorter
from itertools import product, combinations
from functools import cache
from heapq import heappush as hpush, heappop as hpop
from collections import defaultdict, Counter

# sys.setrecursionlimit(int(1e6))

""" Transposing
tr = list(map(list, zip(*G)))
tr = list(map(list, itertools.zip_longest(*grid, fillvalue=None))) #when one or more lists are empty
"""

file = "in.txt"
try:
    file = sys.argv[1]
except IndexError:
    pass


inp = open(file).read().strip()
LINES = inp.split("\n")


def keep_alpnum_spaces(text):
  ret = "".join(ch if ch.isalnum() or ch.isspace() else "" for ch in text)
  return ret


def remove_chars(text, chs):
  ret = "".join([ch for ch in text if ch not in chs])
  return ret


def show (**kwargs):
    output = ', '.join([f"{key} = {value}" for key, value in kwargs.items()])
    print(output)


def ins(r, c, R, C):
  return 0 <= r < R and 0 <= c < C


HV_DIR = [[-1, 0], [1, 0], [0, 1], [0, -1]]
DIAG_DIR = [[1, 1], [-1, -1], [-1, 1], [1, -1]]
ALL_DIR = HV_DIR + DIAG_DIR


# mp = defaultdict(int)
# directions = ['up', 'right', 'down', 'left']
# dir_map = {
#   'up': (-1, 0),
#   'right': (0, 1),
#   'down': (1, 0),
#   'left': (0, -1)
# }


def print_grid(mark):
  R, C = len(mark), len(mark[0])
  for r in range(R):
    for c in range(C):
      print(mark[r][c],end="")
    print()
  print()


def get_last_num_info (s, beg, end):
  while beg >= 0 and s[beg] == '.':
    beg -= 1
  
  end = beg
  while beg >= 0 and s[beg] == s[end]:
    beg -= 1
  beg += 1

  target_num_from_end = s[beg]
  return target_num_from_end, beg, end


def check_block_move_possible(s, end, block_size):
  cnt = 0
  beg = -1
  for i,ch in enumerate(s):
    if i == end:
      break
    if ch == '.':
      cnt += 1
      if beg == -1:
        beg = i
    else:
      cnt = 0
      beg = -1
    if cnt == block_size:
      return True, beg, i

  return False, -1, -1


def solve1(s):
  n = len(s)
  st, en = 0, n-1
  while True:
    while s[st] != '.':
      st += 1
    while s[en] == '.':
      en -= 1
    if st >= en:
      break
    s[st], s[en] = s[en], s[st]
    st += 1
    en -= 1

  mul = 0
  ans = 0
  for ch in s:
    if ch != '.':
      ans += mul * int(ch)
    mul += 1

  return ans


def solve2(s):
  last_num_beg = len(s) - 1
  while True:
    last_num_end = last_num_beg
    last_num, last_num_beg, last_num_end = get_last_num_info(s, last_num_beg, last_num_end)
    if last_num_beg == 0:
      break
    can, dots_beg, dots_end = check_block_move_possible(s, last_num_beg, last_num_end - last_num_beg + 1)
    if can:
      tmp = last_num_beg
      for i in range(dots_beg, dots_end+1):
        s[i] = last_num
        s[tmp] = '.'
        tmp += 1
    last_num_beg -= 1

  # print(s)

  mul = 0
  ans = 0
  for ch in s:
    if ch != '.':
      ans += mul * int(ch)
    mul += 1

  return ans

def main():
  ans1, ans2 = 0, 0
  for ln, line in enumerate(LINES):

    idx = 0
    ID = 0
    s = []
    while idx < len(line):
      num = int(line[idx])
      idx += 1
      if idx%2 == 1:
        for i in range(num):
          s.append(ID)
        ID += 1
      else:
        for i in range(num):
          s.append('.')

    Ts = deepcopy(s)
    print("p1: ", solve1(s))
    s = Ts
    print("p2: ", solve2(s))

if __name__ == "__main__":
  main()






























