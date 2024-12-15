import sys
# import numpy
from itertools import product
from functools import cache
from heapq import heappush as hpush, heappop as hpop
from collections import defaultdict, Counter

# sys.setrecursionlimit(int(1e6))

file = "in.txt"
try:
    file = sys.argv[1]
except IndexError:
    pass

inp = open(file).read().strip()
LINES = inp.split("\n")

def inc_or_dec_by_one_three (L):
  return all (L[i] - L[i+1] in [1,2,3] for i in range(len(L) - 1)) or \
         all (L[i] - L[i+1] in [-1,-2,-3] for i in range (len(L) - 1))

def inc_or_dec (L):
  return all (L[i] < L[i+1] for i in range(len(L) - 1)) or \
         all (L[i] > L[i+1] for i in range (len(L) - 1))


def main():
  ans1, ans2 = 0, 0
  for line in LINES:
    t_levels = list(map(int, line.split()))
    if inc_or_dec_by_one_three (t_levels):
      ans1 += 1
    safe = 0
    for skip_idx in range(len(t_levels)):
      levels = t_levels[:skip_idx] + t_levels[skip_idx + 1:]
      if inc_or_dec(levels) and all (1 <= abs (levels[i] - levels[i+1]) <= 3 for i in range(len(levels) - 1)):
        safe = 1
    ans2 += safe
  print("p1:", ans1)
  print("p2:", ans2)


if __name__ == "__main__":
  main()
