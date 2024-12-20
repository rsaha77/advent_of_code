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


dp = {}
def is_valid_design_obsolete (pat, line):
  # This function has an issue for part 2, because of repeating checks when checking (line[:i],line[i:])
  if line in pat:
    return True
  if line in dp:
    return dp[line]
  is_valid = False
  for i in range(1, len(line)):
    is_valid = is_valid or is_valid_design(pat, line[:i]) and is_valid_design (pat, line[i:])
  dp[line] = is_valid
  return dp[line]


dp = {}
def total_valid_design (patterns, target):
  if target in dp:
    return dp[target]

  if len(target) == 0:
    return 1

  valid_design_cnt = 0
  for pattern in patterns:
    if target.startswith(pattern):
      valid_design_cnt += total_valid_design(patterns, target[len(pattern):])
  dp[target] = valid_design_cnt

  return dp[target]


def main():
  ans1, ans2 = 0, 0
  patterns = list(LINES[0].split(', '))
  for idx, line in enumerate(LINES[2:]):
    tot = total_valid_design (patterns, line)
    ans1 += 1 if tot > 0 else 0
    ans2 += tot
  print("p1: ", ans1)
  print("p2: ", ans2)


if __name__ == "__main__":
  st = time.time()
  main()
  en = time.time()
  print("Execution time: ", en-st)

