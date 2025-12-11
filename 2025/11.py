import sys
from collections import defaultdict
from functools import cache

@cache
def f(u, dac, fft):
  dac |= u == "dac"
  fft |= u == "fft"
  if u == "out":
    return dac and fft
  return sum (f(v,dac,fft) for v in G[u])

data = sys.stdin.read()
G = defaultdict(list)
for line in data.splitlines():
  u,v = line.split(':')
  G[u] = v.split()

print("p1: ", f("you",True,True))
print("p2: ", f("svr",False,False))  