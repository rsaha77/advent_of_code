import sys
import re
from collections import defaultdict

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

seeds = []
mp = defaultdict (int)
for ln,line in enumerate(LINES):
  if ln == 0:
    _, seeds = line.split(':')
    seeds = [int(x) for x in seeds.split()]
    for seed in seeds:
      mp [seed] = seed

  if ln == 1:
    continue

  if len (line) == 0:
    new_seeds = []
    for seed in seeds:
      new_seeds.append(mp[seed])
    seeds = new_seeds
    mp.clear()
    for seed in seeds:
      mp[seed] = seed;
    continue

  if len (line) and line[0].isdigit():
    dest, source, cnt = [int(x) for x in line.split()]
    for seed in seeds:
      if seed >= source and (seed - source) <= cnt:
        mp[seed] = dest + seed - source 

mn = 999999999999999
for v in mp.values():
  mn = min (mn, v)

print (mn)

    





