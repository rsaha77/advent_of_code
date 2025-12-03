import sys
from pathlib import Path

def read_lines(fn):
  f = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(fn)
  return [ln.strip() for ln in f.read_text().splitlines() if ln.strip()]


def solve(s, k):
  stk = []
  for i,ch in enumerate(s):
    # print(f'{stk=} ---- {len(s[i:])+len(stk)=} ---- {s[i:]=}')
    num = int(ch)
    while stk and num > stk[-1] and len(s[i:])+len(stk) > k:
      stk.pop()
    if len(stk) < k:
      stk.append(num)
  return int("".join(map(str, stk)))


def main():
  lines = read_lines("in.txt")
  p1 = p2 = 0
  for s in lines:
    p1 += solve(s,k=2)
    p2 += solve(s,k=12)
  print("p1: ", p1)
  print("p2: ", p2)


if __name__ == "__main__":
  main()
