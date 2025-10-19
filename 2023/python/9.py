import sys
from collections import defaultdict, Counter

file = "in.txt"
try:
  file = sys.argv[1]
except IndexError:
  pass

inp = open(file).read().strip()
LINES = inp.split('\n')


def keep_alpnum_spaces(text):
  ret = ''.join(ch if ch.isalnum() or ch.isspace() else '' for ch in text)
  return ret

def remove_chars (text, chs):
  ret = ''.join([ch for ch in text if ch not in chs])
  return ret

p1 = 0
p2 = 0
for ln,line in enumerate(LINES):
  nums = [int (x.strip()) for x in line.split()]
  cnt = 0
  all_nums = []
  all_nums.append(nums)
  while not all (n == 0 for n in nums):
    cnt += nums[-1]
    tnums = []
    for i in range(1, len(nums)):
      tnums.append (nums[i] - nums [i-1])
    nums = tnums
    all_nums.append(nums)

  p1 += cnt
  curr = 0
  for num in all_nums[::-1]:
    curr = num[0]-curr
  p2 += curr

print(p1)
print(p2)

# Note: You can just reverse the initial lists for part 2



















