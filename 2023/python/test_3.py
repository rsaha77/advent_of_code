import sys
import numpy
from itertools import product
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


def ins(r, c, R, C):
  return 0 <= r < R and 0 <= c < C


direction = [[-1, 0], [1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]]

def main():
  print ("h")
  




if __name__ == "__main__":  main()
























