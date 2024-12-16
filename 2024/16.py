import sys
from heapq import heappush as hpush, heappop as hpop
from collections import defaultdict, Counter

file = "in.txt"
try:
    file = sys.argv[1]
except IndexError:
    pass


inp = open(file).read().strip()
LINES = inp.split("\n")


def ins(r, c, R, C):
  return 0 <= r < R and 0 <= c < C


HV_DIR = [[-1, 0], [0, 1], [1, 0], [0, -1]]


directions = ['^', '>', 'v', '<']
dir_map = {
  '^': (-1, 0),
  '>': (0, 1),
  'v': (1, 0),
  '<': (0, -1)
}


def dfs(r, c, drc, grid, R, C, curr_cost, best_cost, mark, trace_path, vis):
  # was only used for debugging.. Doesn't work for larger grid ..
  vis.add((r,c))
  if curr_cost > best_cost:
    return
  if grid[r][c] == 'E':
    if curr_cost == best_cost:
      cost[r][c] == cost
      for pr, pc in trace_path:
        mark[pr][pc] = 1
    return
  for dr, dc in HV_DIR:
    nr, nc = r + dr, c + dc
    if (nr, nc) not in vis and ins(nr,nc,R,C) and grid[nr][nc] in ['.','E']:
      new_cost, new_drc = get_cost_dir (r,c,nr,nc,drc)
      cost = curr_cost + new_cost
      trace_path.append((nr,nc))
      vis.add((nr,nc))
      dfs(nr, nc, new_drc, grid, R, C, cost, best_cost, mark, trace_path, vis)
      vis.remove((nr,nc))
      trace_path.pop()
  vis.remove((r,c))


def reverse_direction(drc):
  return directions[(directions.index(drc) + 2) % 4]


def dijkstra(sr, sc, er, ec, grid, R, C, p2=False):
  pq = []
  dist = {}
  best_cost = float('inf')
  if not p2:
    hpush(pq, (0, sr, sc, '>'))
  else:
    for drc in directions:
      hpush(pq, (0, er, ec, drc))

  vis = set()
  while pq:
    cost, r, c, drc = hpop(pq)
    
    if (r,c,drc) in vis:
      continue
    vis.add((r,c,drc))
    
    if (r, c, drc) not in dist:
        dist[(r,c,drc)] = cost
    
    if not p2 and (r,c) == (er, ec):
      best_cost = min(best_cost, cost)
    elif p2 and (r, c) == (sr, sc):
      best_cost = min(best_cost, cost)

    dr, dc = dir_map[drc]
    nr, nc = r + dr, c + dc
    if ins(nr, nc, R, C) and grid[nr][nc] != '#':
      hpush(pq, (cost+1, nr, nc, drc))
    idx = directions.index(drc)
    hpush(pq, (cost+1000, r, c, directions[(idx+1) % 4]))
    hpush(pq, (cost+1000, r, c, directions[(idx-1) % 4]))

  return best_cost, dist


def main():
  grid = []
  for ln, line in enumerate(LINES):
    grid.append(line)

  R, C = len(grid), len(grid[0])

  sr,sc,er,ec = (-1,)*4
  for r in range (R):
    for c in range(C):
      if grid[r][c] == 'S':
        sr,sc = r,c
      if grid[r][c] == 'E':
        er,ec = r,c

  assert(sr != -1 and sc != -1 and er != -1 and ec != -1)
        

  best_cost, costs_from_start = dijkstra(sr, sc, er, ec, grid, R, C)
  print("p1: ", best_cost)

  foo, costs_from_end = dijkstra (sr, sc, er, ec, grid, R, C, True)
  valid_tiles = 0
  for r in range(R):
    for c in range(C):
      is_valid_tile = False
      for drc in directions:
        if (r,c,drc) in costs_from_start and (r,c,drc) in costs_from_end:
          c1 = costs_from_start[(r,c,drc)]
          c2 = costs_from_end[(r,c,reverse_direction(drc))]
          if c1 + c2 == best_cost:
            is_valid_tile = True
      if is_valid_tile:
        valid_tiles += 1

  print("p2: ", valid_tiles)


if __name__ == "__main__":
  main()
