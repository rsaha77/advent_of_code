import re
import sys
import copy
# import numpc
import networkx as nx
import math
# from graphlib import TopologicalSorter
# from itertools import product, combinations
# from functools import cache
# from heapq import heappush as hpush, heappop as hpop
from collections import deque, defaultdict, Counter

# sys.setrecursionlimit(int(1e6))

""" Transposing
tr = list(map(list, zip(*G)))
tr = list(map(list, itertools.zip_longest(*grid, fillvalue=None))) #when one or more lists are empty
"""

import networkx as nx


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


HV_DIR = [[-1, 0], [0, 1], [1, 0], [0, -1]] # ^, >, v, <
DIAG_DIR = [[1, 1], [-1, -1], [-1, 1], [1, -1]]
ALL_DIR = HV_DIR + DIAG_DIR


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


directions = ['^', '>', 'v', '<']
dir_map = {
  '^': (-1, 0),
  '>': (0, 1),
  'v': (1, 0),
  '<': (0, -1)
}

def is_connected(a, b, c, d):
  return a in d[b] and b in d[c] and c in d[a]


def has_t(a,b,c):
  return a.startswith('t') or b.startswith('t') or c.startswith('t')


def get_sorted(a,b,c):
  x = [a,b,c]
  return sorted(x)


def find_max_clique(adj_list):
  G = nx.Graph(adj_list)
  max_clique = max(nx.find_cliques(G), key=len)
  return list(max_clique)


def main():
  ans1, ans2 = 0, 0
  nodes = set()
  g = defaultdict(list)
  d = defaultdict(set)
  for ln, line in enumerate(LINES):
    u, v = line.split('-')
    nodes.add(u)
    nodes.add(v)
    g[u].append(v)
    g[v].append(u)
    d[u].add(v)
    d[v].add(u)

  nodes = [x for x in nodes]

  seen = set()
  for i in range(len(nodes)):
    for j in range(1, len(nodes)):
      for k in range(2, len(nodes)):
        a, b, c = get_sorted(nodes[i], nodes[j], nodes[k])
        if (a,b,c) in seen:
          continue
        seen.add((a,b,c))
        if is_connected (a,b,c,d) and has_t (a,b,c):
          ans1 += 1

  print("p1: ", ans1)

  max_clique = find_max_clique(g)
  print("p2: ", ','.join(sorted(max_clique)))


if __name__ == "__main__":
  main()

