import sys
from collections import Counter
from itertools import combinations

def diff_one(str1, str2):
  if len(str1) != len(str2):
    return False, None
  comm, diffs = "", 0
  for i in range(len(str1)):
    if str1[i] != str2[i]:
      diffs += 1
      if diffs == 2:
        return False, None
    else:
      comm += str1[i]
  return True, comm


def main():
  data = sys.stdin.read()
  lines = data.splitlines()

  cnt2, cnt3 = 0, 0
  for line in lines:
    freq = Counter(line)
    cnt2 += any(cnt == 2 for cnt in freq.values())
    cnt3 += any(cnt == 3 for cnt in freq.values())

  p2 = None
  for line1, line2 in combinations(lines, 2):
    is_same, common = diff_one(line1, line2)
    if is_same:
      p2 = common
      break

  print("p1:", cnt2 * cnt3)
  print("p2:", p2)


if __name__ == "__main__":
  main()
