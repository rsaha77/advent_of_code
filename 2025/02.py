import sys
from pathlib import Path

def read_lines(fn):
  f = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(fn)
  return [ln.strip() for ln in f.read_text().splitlines() if ln.strip()]


def ok(s, rep):
  ln = len(s)
  for r in range(rep):
    for nxt in range(r+rep, ln, rep):
      if s[r] != s[nxt]:
        return False
  return True


def main():
  lines = read_lines("in.txt")
  L = lines[0].split(',')
  p1, p2 = 0, 0
  for x in L:
    a,b = map(int,x.split('-'))
    for num in range(a,b+1):
      s = str(num)
      ln = len(s)
      mid = ln//2
      if ln % 2 == 0 and s[:mid] == s[mid:]:
        p1 += num
        p2 += num
        continue
      # check rest of slices for part 2
      for rep in range(1,mid+1):
        if ln % rep != 0:
          continue
        if ok(s, rep):
          p2 += num
          break
  print("p1: ", p1)
  print("p2: ", p2)

if __name__ == "__main__":
  main()
