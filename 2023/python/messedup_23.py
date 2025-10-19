import sys
import heapq
from collections import defaultdict, Counter

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(10000)

#tr = list(map(list, zip(*G)))
#tr = list(map(list, itertools.zip_longest(*grid, fillvalue=None))) #when one or more lists are empty, the above won't work

file = "in.txt"
try:
  file = sys.argv[1]
except IndexError:
  pass

inp = open(file).read().strip()
LINES = inp.split('\n')


def keep_alpnum_spaces(text):
  ret = ''.join(ch if ch.isalnum() or ch.isspace() else '' for ch in text)
  return ret

def remove_chars (text, chs):
  ret = ''.join([ch for ch in text if ch not in chs])
  return ret

def ins (r, c, R, C):
  return 0 <= r < R and 0 <= c < C

direction = [[-1,0], [1,0], [0,1], [0,-1]]

def valid (ch, r, c, nch, nr, nc):
  if ch == '.':
    return True
  elif ch == '>' and nr == r and nc == c + 1:
    return True
  elif ch == '<' and nr == r and nc == c - 1:
    return True
  elif ch == '^' and nr == r - 1 and nc == c:
    return True
  elif ch == 'v' and nr == r + 1 and nc == c:
    return True
  return False


def solve (G, R, C, st, en):
  DG = [[G[r][c]+" " for c in range(C)] for r in range(R)]
  li = [(0, st)]
  heapq.heapify(li)
  vis = set()
  while li:
    dist, (r, c) = heapq.heappop(li)
    vis.add((r,c))
    print ("..", dist, r, c)
    ch = G[r][c]
    new_dist = -dist + 1
    for dr, dc in direction:
      nr = r + dr
      nc = c + dc
      if 0 <= nr < R and 0 <= nc < C and G[nr][nc] != '#' and (nr,nc) not in vis:
        print(",,", nr, nc)
        if valid (ch, r, c, G[nr][nc], nr, nc):
          heapq.heappush(li, (-new_dist, (nr, nc)))
          foo = str(new_dist) + (" " if new_dist//10 == 0 else "")
          DG[nr][nc] = foo
          print("new dist:", new_dist, nr, nc)
          if (nr,nc) == en:
            for g in DG:
              print(g)
            return new_dist
  assert(False)


G = []
for ln,line in enumerate(LINES):
  G.append(line)

R = len(G)
C = len(G[0])

st, en = [(0,c) for c in range(C) if G[0][c] == '.'][0], [(R-1,c) for c in range(C) if G[R-1][c] == '.'][0]

print("st:",st)
print("en:",en)

print (solve(G, R, C, st, en))

# 2415 is too high (used dijkstra BUGGY longest path)
# 1462 is too low (used dijkstra shortest path)



















