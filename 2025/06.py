import sys
from math import prod


def solve_p1(lines):
  G = [line.split() for line in lines.splitlines()]
  R, C = len(G), len(G[0])
  p1 = 0
  for c in range(C):
    col_nums = [int(G[r][c]) for r in range(R-1)]
    p1 += prod(col_nums) if G[R-1][c] == '*' else sum(col_nums)
  return p1


def solve_p2(lines):
  lines = lines.splitlines()
  G = lines[:-1]
  opr = list(lines[-1].split())
  R, C = len(G), len(G[0])
  p2, idx, seg = 0, 0, []
  for c in range(C):
    curr_col = ''.join(G[r][c].strip() for r in range(R))
    if curr_col:
      seg.append(int(curr_col))
    if not curr_col or c == C - 1:
      assert(seg and idx < len(opr))
      p2 += prod(seg) if opr[idx] == '*' else sum(seg)
      seg = []
      idx += 1
  return p2


def main():
  lines = sys.stdin.read()
  print ("p1: ", solve_p1(lines))
  print ("p2: ", solve_p2(lines))


if __name__ == "__main__":
  main()
