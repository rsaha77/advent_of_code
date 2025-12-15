import sys
from string import ascii_lowercase


def can(c1, c2):
  return c1.upper() == c2.upper() and c1 != c2


def react(L):
  stk = []
  for ch in L:
    if stk and can(stk[-1],ch):
      stk.pop()
    else:
      stk.append(ch)
  return len(stk)


def main():
  L = list(sys.stdin.read())

  print("p1: ", react(L))

  p2 = float('inf')
  for c in ascii_lowercase:
    nL = [ch for ch in L if ch not in [c.upper(), c.lower()]]
    p2 = min(p2, react(nL))
  print("p2: ", p2)


if __name__ == "__main__":
  main()
