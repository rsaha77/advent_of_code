import re
import sys
from collections import defaultdict, Counter

file = "in.txt"
try:
    file = sys.argv[1]
except IndexError:
    pass


inp = open(file).read().strip()
LINES = inp.split("\n")


def remove_chars(text, chs):
  ret = "".join([ch for ch in text if ch not in chs])
  return ret


def ins(r, c, R, C):
  return 0 <= r < R and 0 <= c < C


def Cramers(ax, ay, bx, by, px, py):
  den = (ax * by - ay * bx) # determinant

  if den == 0:
    return -1, -1

  m = (px * by - py * bx) // den
  if m * den != (px * by - py * bx):
    return -1, -1
  n = (py - ay * m) // by

  if n * by != (py - ay * m):
    return -1, -1
  return m, n

def main():
  ans1, ans2 = (0,)*2
  button = defaultdict(str)
  TROUBLE = 10000000000000
  for ln, line in enumerate(LINES):
    if len(line) == 0:
      continue
    line = remove_chars(line, ',')
    L = line.split()

    if L[0] == "Button":
      le, ri = L[2].split('+')[1], L[3].split('+')[1]
      button[L[1]] = [int(le), int(ri)]
    else:
      c = int(L[1].split('=')[1])
      f = int(L[2].split('=')[1])
      P, Q = Cramers (button['A:'][0], button['A:'][1], button['B:'][0], button['B:'][1], c, f)
      if P > 0:
        ans1 += P*3 + Q
      c += TROUBLE
      f += TROUBLE
      P, Q = Cramers (button['A:'][0], button['A:'][1], button['B:'][0], button['B:'][1], c, f)
      if P > 0:
        ans2 += P*3 + Q
  print(ans1, ans2)

if __name__ == "__main__":
  main()






















