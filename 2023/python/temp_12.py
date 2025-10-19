import sys
from collections import defaultdict, Counter
from itertools import product

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(10000)

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


# def generate_combinations(pattern, index, res):
#     if index == len(pattern):
#         # print(''.join(pattern))
#         res.append(''.join(pattern))
#         return

#     if pattern[index] == '?':
#         pattern[index] = '.'
#         generate_combinations(pattern, index + 1, res)
#         pattern[index] = '#'
#         generate_combinations(pattern, index + 1, res)
#         pattern[index] = '?'  # Reset for backtracking
#     else:
#         generate_combinations(pattern, index + 1, res)


def valid (r, nums):
  t = []
  cnt = 0
  for ch in r:
    if ch == '#':
      cnt += 1
    elif cnt > 0:
      t.append(cnt)
      cnt = 0

  if cnt:
    t.append(cnt)

  # print(r)
  # print (t)
  # print (nums)
  # print ()

  return True if t == nums else False

def generate_combinations(pattern, nums):
  cnt = 0
  replacements = ['.', '#']
  patterns = pattern.count('?')
  for combo in product(replacements, repeat=patterns):
    index = 0
    result = []
    for char in pattern:
      if char == '?':
        result.append(combo[index])
        index += 1
      else:
        result.append(char)
    cnt += valid (result, nums)
  return cnt


def solve (line):
  # print(line)
  p, n = line.split()
  res = []
  pat, nums = p, n
  for i in range(4):
    pat += '?' + p
    nums += ',' + n

  nums = [int(x.strip()) for x in nums.split(',')]
  # print(pat, nums)

  return generate_combinations(pat, nums)

ans = 0
for ln,line in enumerate(LINES):
  ans += solve (line)

print (ans)

























