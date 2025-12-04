import sys
from pathlib import Path

DIRS = [(-1,0), (1,0), (0,1), (0,-1),(-1,1),(-1,-1),(1,-1),(1,1)]


def read_lines(fn):
  f = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(fn)
  return [ln.strip() for ln in f.read_text().splitlines() if ln.strip()]


def ins(r, c, R, C):
  return 0 <= r < R and 0 <= c < C


def main():
  lines = read_lines("in.txt")
  G = [list(line) for line in lines]
  R, C = len(G), len(G[0])
  p1 = p2 = 0
  done_p1 = False

  while True:
    can = False
    nG = [row[:] for row in G]
    for r in range(R):
      for c in range(C):
        if G[r][c] == '@':
          cnt = 0
          for dr,dc in DIRS:
            nr,nc=r+dr,c+dc
            if ins(nr,nc,R,C) and G[nr][nc] == '@':
              cnt += 1
              if cnt > 3:
                break
          if cnt <= 3:
            nG[r][c] = '.'
            can = True
            if not done_p1:
              p1 += 1
            p2 += 1
    done_p1 = True
    G = nG
    if not can:
      break

  print("p1: ", p1)
  print("p2: ", p2)


if __name__ == "__main__":
  main()
