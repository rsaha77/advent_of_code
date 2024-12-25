import sys

file = "in.txt"
try:
    file = sys.argv[1]
except IndexError:
    pass

inp = open(file).read().strip()
LINES = inp.split("\n\n")


def match (g1, g2, grids, R, C):
  for r in range(R):
    for c in range(C):
      if g1[r][c] == '#' and g2[r][c] == '#':
        return False
  return True


def main():
  grids = []
  for line in LINES:
    grids.append(line.split('\n'))

  R, C = len(grids[0]), len(grids[0][0])

  ans1 = 0
  for g1 in grids:
    for g2 in grids:
      if match(g1,g2,grids, R, C):
        ans1 += 1

  print(ans1 >> 1)


if __name__ == "__main__":
  main()
