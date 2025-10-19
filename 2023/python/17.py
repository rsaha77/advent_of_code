import sys
from heapq import heappush as hpush, heappop as hpop
from collections import defaultdict, Counter

# sys.setrecursionlimit(int(1e6))

""" Transposing
tr = list(map(list, zip(*G)))
tr = list(map(list, itertools.zip_longest(*grid, fillvalue=None))) #when one or more lists are empty
"""

file = "in.txt"
try:
    file = sys.argv[1]
except IndexError:
    pass


inp = open(file).read().strip()
LINES = inp.split("\n")


def keep_alpnum_spaces(text):
  ret = "".join(ch if ch.isalnum() or ch.isspace() else "" for ch in text)
  return ret


def remove_chars(text, chs):
  ret = "".join([ch for ch in text if ch not in chs])
  return ret

def show (**kwargs):
    output = ', '.join([f"{key} = {value}" for key, value in kwargs.items()])
    print(output)

def ins(r, c, R, C):
  return 0 <= r < R and 0 <= c < C


mp = defaultdict(int)

dTurn = {
  ("ri", "st"): (0, 1, "ri"),
  ("ri", "le"): (-1, 0, "up"),
  ("ri", "ri"): (1, 0, "do"),

  ("le", "st"): (0, -1, "le"),
  ("le", "le"): (1, 0, "do"),
  ("le", "ri"): (-1, 0, "up"),

  ("up", "st"): (-1, 0, "up"),
  ("up", "le"): (0, -1, "le"),
  ("up", "ri"): (0, 1, "ri"),

  ("do", "st"): (1, 0, "do"),
  ("do", "le"): (0, 1, "ri"),
  ("do", "ri"): (0, -1, "le")
}


def invalid (steps, turn, part1, part2):

  if part1:
    if steps == 3 and turn == "st":
      return True

  if part2:
    if steps < 4 and turn in ["le", "ri"]:
      return True
    if steps == 10 and turn in ["st"]:
      return True

  return False


def solve(grid, part1=False):
  part2 = not part1
  R, C = len(grid), len(grid[0])
  pq = [(0, 0, 0, "ri", 0)] #shortest dist at 0,0 while it's heading right with steps, path

  seen = set()
  ans = float('inf')

  """
  if not doing dist[u] + dist < dist[v]
  then need to include the set to track the seen states

  In this question (dist[u] + dist) < dist[v] would fail because there are multiple distances involved in a node.
  Hence the trick/modification is to track them via the set seen and use all those distances to calulate the shortest path.
  """

  while pq:
    dist_rc, r, c, way, steps = hpop(pq)

    if (r, c) == (R-1, C-1):
      if part1:
        return dist_rc
      if part2:
        if steps >= 4:
          # print(steps, dist_rc)
          ans = min (ans, dist_rc)

    if (r, c, way, steps) in seen:
      # Missed this for part1
      # Was checking inside the for loop which is wrong + slow. Can only check once popped.
      continue

    seen.add((r, c, way, steps))

    for turn in ["st", "le", "ri"]:
      if invalid (steps, turn, part1, part2):
        continue

      new_steps = (steps + 1) if turn == "st" else 1
      dr, dc, new_way = dTurn[(way, turn)]
      nr, nc = r + dr, c + dc

      if ins (nr, nc, R, C) and (nr, nc, new_way, new_steps) not in seen:
        new_dist = dist_rc + grid[nr][nc]
        hpush(pq, (new_dist, nr, nc, new_way, new_steps))

  return ans



def main():
  grid = []
  for ln, line in enumerate(LINES):
    grid.append([int(ch) for ch in line])
  print("part1:", solve(grid, part1=True))
  print("part2:", solve(grid))


# Time: 26 + many!
if __name__ == "__main__":
  main()
