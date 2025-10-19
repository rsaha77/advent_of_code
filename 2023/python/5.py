import sys
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
curr_map, mappings = [], []
fl = False
for ln,line in enumerate(LINES):
  if ln == 0:
    _, seeds = line.split(':')
    seeds = [int(x.strip()) for x in seeds.split()]

  elif ln == 1:
    continue

  elif len(line) == 0:
    mappings.append(curr_map)
    continue

  elif line.endswith(':'):
    curr_map = []

  elif line[0].isdigit():
    line = [int(x.strip()) for x in line.split()]
    curr_map.append (line)

  if ln == len(LINES) - 1:
    mappings.append(curr_map)

# print (mappings)


def getlocation (seed, mappings):
  # print ("Init seed:", seed)
  for maps in mappings:
    for c in maps:
      dest, source, cnt = c[0], c[1], c[2]
      # print (dest, source, cnt)
      if seed >= source and (seed - source) < cnt:
        seed = dest + seed - source
        # print(seed)
        break
    # print ("SEED: ", seed)
    # print()
  # print ("Done seed: ", seed)
  return seed

mn = 999999999999999
for i in range (1, len(seeds), 2):
  seed, freq = seeds [i-1], seeds [i]
  # print (seed, freq)
  for j in range(freq):
    mn = min (mn, getlocation(seed + j, mappings))

print (mn)



































