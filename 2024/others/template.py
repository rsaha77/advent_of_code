import re
import sys
import copy
# import numpc
import math
# from graphlib import TopologicalSorter
# from itertools import product, combinations
# from functools import cache
# from heapq import heappush as hpush, heappop as hpop
from collections import deque, defaultdict, Counter

# sys.setrecursionlimit(int(1e6))

file = "in.txt"
try:
    file = sys.argv[1]
except IndexError:
    pass

inp = open(file).read().strip()
LINES = inp.split("\n")

HV_DIR = [[-1, 0], [0, 1], [1, 0], [0, -1]] # ^, >, v, <
DIAG_DIR = [[1, 1], [-1, -1], [-1, 1], [1, -1]]
ALL_DIR = HV_DIR + DIAG_DIR

directions = ['^', '>', 'v', '<']
dir_map = {
  '^': (-1, 0),
  '>': (0, 1),
  'v': (1, 0),
  '<': (0, -1)
}


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


def print_grid(mark):
  R, C = len(mark), len(mark[0])
  for r in range(R):
    for c in range(C):
      print(mark[r][c], end="")
    print()
  print()


def generate_combinations(n, lst):
  return [list(combination) for combination in product(lst, repeat=n)]


def merge_and_sort_lists(list1, list2, list3):
    merged_list = list1 + list2 + list3
    sorted_list = sorted(merged_list, key=lambda x: x[0])
    return sorted_list


def calculate_distance(point1, point2):
  return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def main():
  ans1, ans2 = 0, 0
  grid = []
  for ln, line in enumerate(LINES):
    pass

  R, C = len(grid), len(grid[0])
  grid = [[grid[r][c] for c in range(C)] for r in range(R)]

if __name__ == "__main__":
  main()










