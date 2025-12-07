import sys
from collections import defaultdict

def main():
  data = sys.stdin.read()
  G = data.splitlines()
  R, C = len(G), len(G[0])

  sr = sc = -1
  for r, row in enumerate(G):
    c = row.find('S')
    if c != -1:
      sr, sc = r, c
      break
  assert(sr != -1)

  cnt_col = [0] * C
  splits, cnt_col[sc] = 0, 1
  for r in range(sr+1, R):
    for c in range(C):
      if G[r][c] == '^' and cnt_col[c] > 0:
        splits += 1
        cnt = cnt_col[c]
        cnt_col[c] = 0
        if c - 1 >= 0:
          cnt_col[c - 1] += cnt
        if c + 1 < C:
          cnt_col[c + 1] += cnt

  print("p1: ", splits)
  print("p2: ", sum(cnt_col))


if __name__ == "__main__":
  main()
