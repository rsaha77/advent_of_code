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

"""

px ['a<2006:qkq', 'm>2090:A', 'rfg']
pv ['a>1716:R', 'A']
lnx ['m>1548:A', 'A']
rfg ['s<537:gd', 'x>2440:R', 'A']
qs ['s>3448:A', 'lnx']
qkq ['x<1416:A', 'crn']
crn ['x>2662:A', 'R']
in ['s<1351:px', 'qqz']
qqz ['s>2770:qs', 'm<1801:hdj', 'R']
gd ['a>3333:R', 'R']
hdj ['m>838:A', 'pv']

[['x', '787'], ['m', '2655'], ['a', '1222'], ['s', '2876']]
[['x', '1679'], ['m', '44'], ['a', '2067'], ['s', '496']]
[['x', '2036'], ['m', '264'], ['a', '79'], ['s', '2244']]
[['x', '2461'], ['m', '1339'], ['a', '466'], ['s', '291']]
[['x', '2127'], ['m', '1623'], ['a', '2188'], ['s', '1013']]

"""

def can (l, line):
  # l = s<1351
  sign = l[1]
  ch, num = l.split(sign)
  num = int(num)
  for a, b in line:
    if a == ch:
      b = int(b)
      if (sign == '<'  and b < num) or (sign == '>' and b > num):
        return True
  return False


def getsum (line):
  return sum (int(b) for a,b in line)


def process (line, mp, curr):
  if curr == 'A':
    return getsum (line)
  elif curr == 'R':
    return 0

  for m in mp[curr]:
    # in ['s<1351:px', 'qqz']
    if ':' in m:
      l,r = m.split(':')
    if can(l, line):
      return process (line, mp, r)

  return process(line, mp, mp[curr][-1])


mp = defaultdict (list)
for ln,line in enumerate(LINES):
  l,r = line.split('{')
  r = remove_chars(r, '}')
  r = r.split(',')
  mp[l] = r

























