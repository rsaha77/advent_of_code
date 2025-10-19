import sys
from collections import defaultdict, Counter, deque
from functools import cache

# print(sys.getrecursionlimit())
sys.setrecursionlimit(100000)

file = "in.txt"
try:
  file = sys.argv[1]
except IndexError:
  pass

inp = open(file).read().strip()
LINES = inp.split('\n')



def is_valid (pat, grp):
  chk = []
  streak = 0
  for ch in pat:
    if ch == '#':
      streak += 1
    else:
      if streak:
        chk.append(streak)
      streak = 0
  if streak:
    chk.append(streak)
  return tuple(chk) == grp


# O(2^len(s))
def solve_brute_force (s, grp, i):
  if i == len(s):
    return is_valid(s, grp)
  if s[i] == '?':
    return (solve (s[:i] + '#' + s[i+1:], grp, i + 1) +
            solve (s[:i] + '.' + s[i+1:], grp, i + 1))
  else:
    return solve(s, grp, i + 1)


# O(len(s) * len(grp) * MAX_BLOCK_SIZE)
def solve_dp (dp, s, grp, s_idx, grp_idx, curr_grp):

  if s_idx == len(s):
    if ((grp_idx == len(grp) and curr_grp == 0) or
         grp_idx == len(grp) - 1 and grp[grp_idx] == curr_grp):
        return 1
    return 0

  if dp[s_idx][grp_idx][curr_grp] >= 0:
    return dp [s_idx][grp_idx][curr_grp]

  ch = s[s_idx]
  ans = 0
  if ch in ['#', '?']:
    if grp_idx <= len(grp) - 1 and curr_grp < grp[grp_idx]:
      ans += solve_dp(dp, s, grp, s_idx + 1, grp_idx, curr_grp + 1)
  if ch in ['.', '?']:
    if curr_grp == 0:
      ans += solve_dp(dp, s, grp, s_idx + 1, grp_idx, 0)
    elif curr_grp == grp[grp_idx]:
      ans += solve_dp(dp, s, grp, s_idx + 1, grp_idx + 1, 0)

  dp [s_idx][grp_idx][curr_grp] = ans
  return ans


def solve_dfa ():
  # TODO
  pass
    

def hot_springs (p2):
  ans = 0
  for ln,line in enumerate(LINES):
    # print(ln)
    pat, grp = line.split()
    grp = [int(x) for x in grp.split(',')]
    if p2:
      factor = 5
      pat = (pat + '?') * (factor - 1) + pat
      grp *= factor
    dp = [[[-1 for _ in range(max(grp) + 1)] for _ in range(len(grp) + 1)] for _ in range(len(pat))]
    ans += solve_dp (dp, pat, tuple(grp), 0, 0, 0)
  return ans


def main():
  print ("Part 1:", hot_springs (p2=False))
  print ("Part 2:", hot_springs (p2=True))


if __name__ == "__main__":
  main()

