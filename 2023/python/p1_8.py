import sys
import re
from collections import defaultdict, Counter
D = open("in.txt").read().strip()
LINES = D.split('\n')


def keep_alpnum_spaces(text):
  ret = ''.join(ch if ch.isalnum() or ch.isspace() else '' for ch in text)
  return ret

def remove_chars (text, chs):
  ret = ''.join([ch for ch in text if ch not in chs])
  return ret


mp = defaultdict (list)

for i,line in enumerate(LINES):
  if i == 0:
    instruction = line
    continue
  if i == 1:
    continue

  line = keep_alpnum_spaces(line)
  L, RL, RR = [x.strip() for x in line.split()]
  mp[L] = [RL, RR]


ans = 0
idx = 0;
node = "AAA"
while True:
  direction = instruction [idx % len(instruction)]
  node = mp[node][0 if direction == 'L' else 1]
  ans += 1
  idx += 1
  if node == 'ZZZ':
    break

print(ans)


