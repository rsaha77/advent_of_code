import sys
from pathlib import Path

def read_lines(fn):
  f = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(fn)
  return [ln.strip() for ln in f.read_text().splitlines() if ln.strip()]

def main():
  lines = read_lines("in.txt")
  curr = 50
  p1, p2 = 0, 0
  for line in lines:
    drc, num = line[0], int(line[1:])
    while num > 0:
      if drc == 'L':
        curr -= 1
      else:
        curr += 1
      curr %= 100
      if not curr:
        p2 += 1
      num -= 1
    if curr == 0:
      p1 += 1
  print(p1, p2)


if __name__ == "__main__":
  main()
