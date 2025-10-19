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
tot_cnt = 0
mxso = 0
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
    tot_cnt += line[2]
    mxso = max (mxso, line [0] + line[2])
    curr_map.append (line)

  if ln == len(LINES) - 1:
    mappings.append(curr_map)

# print (mappings)


def solve (mappings, seeds):
  mappings.reverse()
  for maps in mappings:
    for c in maps:
      dest, source, cnt = c[0], c[1], c[2]


  return 1111


print ("(len(seeds)/2)): ", (len(seeds)/2))
print ("tot_cnt: ", tot_cnt)
print ("max_possible_ans: ", mxso)
print (solve (mappings, seeds))
  

mn = 999999999999999
tf = 0
for i in range (1, len(seeds), 2):
  seed, freq = seeds [i-1], seeds [i]
  tf += freq
#   print (seed, freq)
#   for j in range(freq):
#     mn = min (mn, getlocation(seed + j, mappings))

in_mins = pow(10,8) * 60;
print ("process seeds in O(1): ", tf/in_mins, " mins")
print ("current naive solution", tf*215/in_mins, " mins")
print ("Preprocess maps: ", ((tot_cnt * (len(seeds)/2))/in_mins), " mins, will be out of MEMORY + TIME if you store it")
print ("Binary Search: ", tf*(7)/in_mins, "mins")
print ("min to max ans chk: ", mxso*10/in_mins, "mins")

# print(mn)


































