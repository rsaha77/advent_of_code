import sys
from collections import defaultdict

"""
It's a DAG
dp[state] = Starting from this state, how many valid paths lead to the target?
"""

def solve(source, G, p1):
  DP = {}
  def dfs (u, seen_dac, seen_fft):
    state = u if p1 else (u, seen_dac, seen_fft)
    if state in DP:
        return DP[state]

    seen_dac |= (u == "dac")
    seen_fft |= (u == "fft")

    if u == "out":
      return 1 if (p1 or (seen_dac and seen_fft)) else 0
    
    tot = 0
    for v in G[u]:
      tot += dfs (v, seen_dac, seen_fft)
    DP[state] = tot
    return tot
  return dfs(source, False, False)


def main():
  data = sys.stdin.read()
  G = defaultdict(list)
  for line in data.splitlines():
    line = line.split(':')
    G[line[0]] = line[1].split()

  print("p1: ", solve("you", G, p1=True))
  print("p2: ", solve("svr", G, p1=False))


if __name__ == "__main__":
  main()
