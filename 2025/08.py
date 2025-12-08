import sys
import math

class DSU:
  def __init__(self, n):
    self.par = list(range(n))
    self.siz = [1] * n

  def get_par(self, x):
    if self.par[x] != x:
      self.par[x] = self.get_par(self.par[x])
    return self.par[x]

  def join(self, a, b):
    a, b = self.get_par(a), self.get_par(b)
    if a == b:
      return False
    if self.siz[a] < self.siz[b]:
      a, b = b, a
    self.siz[a] += self.siz[b]
    self.par[b] = a
    return True

  def get_comp_size(self, x):
    return self.siz[self.get_par(x)]


def main():
  lines = sys.stdin.read()
  pts = []
  for line in lines.splitlines():
    x,y,z = (int(n) for n in line.split(','))
    pts.append((x,y,z))
  N = len(pts)

  def dist(i, j):
    x1, y1, z1 = pts[i]
    x2, y2, z2 = pts[j]
    dx, dy, dz = x2 - x1, y2 - y1, z2 - z1
    return math.sqrt(dx*dx + dy*dy + dz*dz)

  dist_pts = []
  for i in range(N):
    for j in range(i+1, N):
      dist_pts.append((dist(i, j), (i,j)))

  dist_pts = sorted(dist_pts)

  dsu = DSU(N)
  p1, p2 = None, None
  for idx, (_, (u, v)) in enumerate(dist_pts):
    can_join = dsu.join(u,v)

    if idx == 999:
      par_size = {}
      for u in range(N):
        par_u = dsu.get_par(u)
        if par_u not in par_size:
          par_size[par_u] = dsu.get_comp_size(par_u)
      comp_sizes = sorted(par_size.values())
      p1 = math.prod(comp_sizes[-3:])

    if can_join:
      curr_sz = dsu.get_comp_size(u)
      if curr_sz == N:
        p2 = pts[u][0] * pts[v][0]
        break

  print("p1: ", p1)
  print("p2: ", p2)


if __name__ == "__main__":
  main()

