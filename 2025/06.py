import sys
from pathlib import Path


def read_lines_p1(fname):
  f = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(fname)
  return [ln.strip() for ln in f.read_text().splitlines() if ln.strip()]

def read_lines_p2(fname):
  f = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(fname)
  return [ln for ln in f.read_text().splitlines() if ln.strip()]


def ins(r, c, R, C):
  return 0 <= r < R and 0 <= c < C


def fn(s, opr):
  L = []
  res = ""
  for ch in s:
    if ch != ' ':
      res += ch
    else:
      if len(res):
        L.append(int(res))
      res = ""
  if len(res):
    L.append(int(res))

  ret = L[-1]
  for i in range(len(L)-2, -1, -1):
    if opr == '*':
      ret *= L[i]
    else:
      ret += L[i]
  return ret


def solve_p1():
  lines = read_lines_p1("in.txt")
  p1, G = 0, []
  for line in lines:
    G.append([x for x in line.split()])

  R, C = len(G), len(G[0])
  for c in range(C):
    curr = int(G[0][c])
    for r in range(1, R-1):
      num = int(G[r][c])
      opr = G[R-1][c]
      if opr == '*':
        curr *= num
      else:
        curr += num
    p1 += curr
  print("p1: ", p1)


def solve_p2():
  p2 = 0
  G, opr = [], []
  lines = read_lines_p2("in.txt")
  for line in lines:
    if line != lines[-1]:
      G.append(line)
    else:
      line = [x.strip() for x in line.split()]
      opr = line

  R = len(G)
  C = max(len(G[x]) for x in range(0,R))
  curr, idx = [], 0
  for c in range(C):
    all_space = True
    for r in range(R):
      if c < len(G[r]) and G[r][c] != ' ':
        all_space = False
      if c < len(G[r]):
        curr.append(G[r][c])
    if all_space:
      p2 += fn(curr, opr[idx])
      curr = []
      idx += 1
    else:
      curr.append(' ')

  p2 += fn(curr, opr[idx])
  print("p2: ", p2)


def main():
  solve_p1()
  solve_p2()


if __name__ == "__main__":
  main()
