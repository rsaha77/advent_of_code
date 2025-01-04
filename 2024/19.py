import re
import sys
import time
from functools import cache
from collections import defaultdict, Counter

file = "in.txt"
try:
    file = sys.argv[1]
except IndexError:
    pass
inp = open(file).read().strip()
LINES = inp.split("\n")


def solve (idx, s, words, dp):
  if idx == len(s):
    return 1

  if idx in dp:
    return dp[idx]
  
  ret = 0
  for word in words:
    if s[idx:].startswith(word):
      ret = ret + solve(idx + len(word), s, words, dp)

  dp[idx] = ret #ways - starting from index idx
  return dp[idx]


def main():
  ans1, ans2 = 0, 0
  patterns = list(LINES[0].split(', '))
  for idx, line in enumerate(LINES[2:]):
    dp = {}
    tot = solve (0, line, patterns, dp)
    if tot > 0:
      ans1 += 1
      ans2 += tot
  print("p1: ", ans1)
  print("p2: ", ans2)


if __name__ == "__main__":
  st = time.time()
  main()
  en = time.time()
  print("Execution time: ", en-st)

