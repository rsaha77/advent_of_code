import sys
import re
import math
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
start_nodes = []

for i,line in enumerate(LINES):
  if i == 0:
    instruction = line
    continue
  if i == 1:
    continue

  line = keep_alpnum_spaces(line)
  L, RL, RR = [x.strip() for x in line.split()]
  mp[L] = [RL, RR]

  if L.endswith('A'):
    start_nodes.append (L)

all_iters = []
for st in start_nodes:
  idx = 0
  iters = 0
  node = st
  while True:
    direction = instruction [idx % len(instruction)]
    node = mp[node][0 if direction == 'L' else 1]
    iters += 1
    idx += 1
    if node.endswith('Z'):
      break
  print (st, node, iters)
  all_iters.append (iters)

print(math.lcm(*all_iters))


