import sys
# import numpy
from itertools import product
from collections import defaultdict, Counter

# sys.setrecursionlimit(int(1e6))

file = "in.txt"
try:
    file = sys.argv[1]
except IndexError:
    pass


inp = open(file).read().strip()
LINES = inp.split("\n")


def generate_combinations(n, lst):
  return [list(combination) for combination in product(lst, repeat=n)]


def concatenate_numbers(num1, num2):
  concatenated = str(num1) + str(num2)
  return int(concatenated)


def check (target, nums, lst):
  ln = len(nums)
  all_combs = generate_combinations(ln-1, lst)
  for combs in all_combs:
    actual = nums[0]
    for i in range(1, ln):
      if combs[i-1] == 0:
        actual += nums[i]
      elif combs[i-1] == 1:
        actual *= nums[i]
      else: actual = concatenate_numbers(actual, nums[i])
    if actual == target:
      return True
  return False


def main():
  ans1, extra, ans2 = (0,)*3
  for ln, line in enumerate(LINES):
    target, R = line.split(':')
    target = int(target)
    nums = [int(x) for x in R.split()]
    # print(target, nums)
    if check(target, nums, [0,1]):
      ans1 += target
    elif check (target, nums, [0,1,2]):
      extra += target
  ans2 = ans1 + extra
  print("p1: ", ans1)
  print("p2: ", ans2)


if __name__ == "__main__":
  main()
