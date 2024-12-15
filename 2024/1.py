import sys

file = "in.txt"
try:
    file = sys.argv[1]
except IndexError:
    pass

inp = open(file).read().strip()
LINES = inp.split("\n")


def main():
  fr, se, ans1, ans2 = [], [], 0, 0
  for ln, line in enumerate(LINES):
    a, b = line.split()
    fr.append(int(a))
    se.append(int(b))
  fr, se = sorted(fr), sorted(se)

  for i, n1 in enumerate(fr):
    ans1 += abs(n1 - se[i])

  for n1 in fr:
    cnt = 0
    for n2 in se:
      if n1==n2:
        cnt += 1
    ans2 += n1 * cnt
    
  print("part1:", ans1)
  print("part2:", ans2)


if __name__ == "__main__":
  main()
