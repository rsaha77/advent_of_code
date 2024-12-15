import sys
# import numpy
from graphlib import TopologicalSorter
from collections import defaultdict, Counter

# sys.setrecursionlimit(int(1e6))


file = "in.txt"
try:
    file = sys.argv[1]
except IndexError:
    pass


inp = open(file).read().strip()
LINES = inp.split("\n")


def get_middle(lst):
  return lst[len(lst) // 2]


def arrange_nums(rules, update):
  ts = TopologicalSorter()
  
  for x, y in rules:
    if x in update and y in update:
      ts.add(x, y)
  
  sorted_update = list(ts.static_order())
  return sorted_update


def main():
  ans1, ans2 = (0,)*2
  next = defaultdict(list)
  rules = []
  for ln, line in enumerate(LINES):
    if '|' in line:
      a,b = list(map(int, line.split('|')))
      next[a].append(b)
      rules.append([a,b])
    elif ',' in line:
      nums = list(map(int, line.split(',')))
      valid = True
      for i, num in enumerate(nums[1:]):
        if num not in next[nums[i]]:
          valid = False
      if valid:
        ans1 += get_middle(nums)
      else:
        nums = arrange_nums(rules, nums)
        ans2 += get_middle(nums)
  print("p1: ", ans1)
  print("p2: ", ans2)


if __name__ == "__main__":
  main()
