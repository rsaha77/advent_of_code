import sys
from itertools import chain

def main():
  data = sys.stdin.read()
  N = 1000
  G = [[0] * N for _ in range(N)]
  claims = []

  for idx, line in enumerate(data.splitlines()):
    parts = line.split()
    pos = parts[2].rstrip(':')
    dims = parts[3]

    left, top = map(int, pos.split(','))
    wide, tall = map(int, dims.split('x'))

    r1 = top
    r2 = top + tall
    c1 = left
    c2 = left + wide

    for r in range(r1, r2):
      for c in range(c1, c2):
        G[r][c] += 1

    claims.append((idx, r1, r2, c1, c2))

  overlaps = sum(val > 1 for val in chain.from_iterable(G))

  for idx, r1, r2, c1, c2 in claims:
    if all(G[r][c] == 1 for r in range(r1, r2) for c in range(c1, c2)):
      p2 = idx + 1
      break

  print("p1:", overlaps)
  print("p2:", p2)


if __name__ == "__main__":
  main()
