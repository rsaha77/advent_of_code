import re
import sys
from functools import cache
from collections import defaultdict, Counter

# sys.setrecursionlimit(int(1e6))

file = "in.txt"
try:
    file = sys.argv[1]
except IndexError:
    pass


inp = open(file).read().strip()
LINES = inp.split("\n")


@cache
def rec(x, blinks):
  if blinks == 0:
    return 1
  blinks -= 1

  if x == 0:
    return rec(1, blinks)

  str_x = str(x)
  ln = len(str(x))
  if ln % 2 == 0:
    left = int(str_x[:ln//2])
    right= int(str_x[ln//2:])
    return rec(left, blinks) + rec(right, blinks)
  else:
    return rec(x*2024, blinks)


def solve_rec (L, TOTAL_BLINKS):
  ans = 0
  for x in L:
    ans += rec(x, TOTAL_BLINKS)
  return ans


def solve_map(L, TOTAL_BLINKS):
  mp = Counter(L)
  for _ in range (TOTAL_BLINKS):
    new_mp = defaultdict(int)
    for num, freq in mp.items():
      if num == 0:
        new_mp[1] += freq
      elif len(str(num)) % 2 == 0:
        num_str = str(num)
        mid = len(num_str) // 2
        left_half = int(num_str[:mid])
        right_half = int(num_str[mid:])
        new_mp[left_half] += freq
        new_mp[right_half] += freq
      else:
        new_mp[num*2024] += freq
    mp = new_mp
  return sum(mp.values())


def main():
  ans1, ans2 = 0, 0
  for ln, line in enumerate(LINES):
    L = list(map(int, line.split()))
  print("p1: ", solve_rec(L, 25))
  print("p2: ", solve_rec(L, 75))


if __name__ == "__main__":
  main()






























