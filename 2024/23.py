import sys
import networkx as nx
from collections import deque, defaultdict, Counter


file = "in.txt"
try:
    file = sys.argv[1]
except IndexError:
    pass


inp = open(file).read().strip()
LINES = inp.split("\n")


def ins(r, c, R, C):
  return 0 <= r < R and 0 <= c < C


HV_DIR = [[-1, 0], [0, 1], [1, 0], [0, -1]] # ^, >, v, <
DIAG_DIR = [[1, 1], [-1, -1], [-1, 1], [1, -1]]
ALL_DIR = HV_DIR + DIAG_DIR


def is_connected(a, b, c, d):
  return a in d[b] and b in d[c] and c in d[a]


def startswith_t(a,b,c):
  return a.startswith('t') or b.startswith('t') or c.startswith('t')


def get_sorted(a,b,c):
  x = [a,b,c]
  return sorted(x)


def find_max_clique(adj_set):
  G = nx.Graph(adj_set)
  max_clique = max(nx.find_cliques(G), key=len)
  return list(max_clique)


def main():
  ans1, ans2 = 0, 0
  g = defaultdict(set)
  for ln, line in enumerate(LINES):
    u, v = line.split('-')
    g[u].add(v)
    g[v].add(u)

  nodes = sorted(g.keys())

  for i in range(len(nodes)):
    for j in range(i+1, len(nodes)):
      for k in range(j+1, len(nodes)):
        a,b,c = nodes[i], nodes[j], nodes[k]
        if is_connected(a,b,c,g) and startswith_t(a,b,c):
          ans1 += 1

  print("p1: ", ans1)

  max_clique = find_max_clique(g)
  print("p2: ", ','.join(sorted(max_clique)))


if __name__ == "__main__":
  main()
