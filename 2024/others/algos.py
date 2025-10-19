def dijkstra (grid, part1=False):
  part2 = not part1
  R, C = len(grid), len(grid[0])
  pq = [(0, 0, 0, "ri", 0)] #shortest dist at 0,0 while it's heading right with steps, path

  seen = set()
  ans = float('inf')

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
      # Missing this was the reason for timeout / too slow for part1
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


# ==========================================================
# ==========================================================


  class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        a = self.parent[a]
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def merge(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb: return False
        self.parent[pb] = pa
        return True








        