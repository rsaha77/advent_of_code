import sys
import numpy
from itertools import product
from functools import cache
from heapq import heappush as hpush, heappop as hpop
from collections import defaultdict, Counter, deque

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


# direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
# direction = [[-1, 0], [1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]]


class module:
  def __init__(self, type=None, status=None):
    self.type = type
    self.status = status


broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a

button -low-> broadcaster
broadcaster -low-> a
broadcaster -low-> b
broadcaster -low-> c
a -high-> b
b -high-> c
c -high-> inv
inv -low-> a
a -low-> b
b -low-> c
c -low-> inv
inv -high-> a


def solve (modules, nxt):
  cnt = 1000
  while cnt > 0:
    qq = deque(["broadcaster", "low"])
    while not qq.empty():
      u, pulse = qq.pop()
      for v in nxt(u):
        typ, status = modules[v].type, modules[v].status
        if pulse == "low":
          if typ == "Flip-flop":
            new_status = "ON" if status == "OFF" else "OFF"
            modules[v].status = new_status
            new_pulse = "high" if new_status == "ON" else "low"
            

    cnt -= 1


def main():
  modules = defaultdict(lambda: module())
  nxt = defaultdict(list)
  for ln, line in enumerate(LINES):
    l,r = line.split("->")
    l = l.strip()
    r = [x.strip() for x in r.split(',')]
    if l != "broadcaster":
      tp = l[0]
      l = l[1:]
      modules[l].type = "Flip-flop" if tp == "%" else "Conjunction"
      modules[l].status = "OFF"
    nxt [l] = r

  for k,v in nxt.items():
    print(k, v)
  return (solve (modules, nxt))


if __name__ == "__main__":
  main()










