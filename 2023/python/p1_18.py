import sys
from collections import defaultdict, Counter

# sys.setrecursionlimit(int(1e6))

# tr = list(map(list, zip(*G)))
# tr = list(map(list, itertools.zip_longest(*grid, fillvalue=None))) #when one or more lists are empty, the above won't work

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


def ins(r, c, R, C):
    return 0 <= r < R and 0 <= c < C


MXN = 700
st = 100

# MXN = 20
# st = 0

direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
mp = defaultdict(int)


def valid (G, r, c):
    """
    This is wrong and wont work for this question
    """
    tot = 0
    for dr,dc in direction:
        nr,nc = r,c
        fl = False
        while nr >= 0 and nr < MXN and nc >= 0 and nc < MXN:
            if G[nr][nc] == '#':
                fl = True
                break
            nr += dr
            nc += dc
        if not fl:
            return False
        tot += 1
    return True if tot == 4 else False


G = [['.' for c in range(MXN)] for r in range(MXN)]
r,c = st, st
plots = []
for ln, line in enumerate(LINES):
    drc, cnt, foo = line.split()
    cnt = int(cnt)
    print(drc, cnt)
    print(r,c)

    if drc == 'R':
        tot = c + cnt
        while c < tot:
            G[r][c] = '#'
            plots.append((r,c))
            c += 1


    elif drc == 'L':
        tot = c - cnt
        while c > tot:
            G[r][c] = '#'
            plots.append((r,c))
            c -= 1

    elif drc == 'D':
        tot = r + cnt
        while r < tot:
            print(drc, cnt)
            G[r][c] = '#'
            plots.append((r,c))
            r += 1
        

    elif drc == 'U':
        tot = r - cnt
        while r > tot:
            G[r][c] = '#'
            plots.append((r,c))
            r -= 1

for g in G:
    for ch in g:
        print(ch,end="")
    print()

# ans = 0
# for r in range(MXN):
#     for c in range(MXN):
#         if G[r][c] == '#' or valid (G, r, c):
#             ans += 1


# 35983 is too high
# 29725 is too low
"""

Found out coner case

 ###
 .
#.#
####

Ans is 0 for this case
Lets use matplotlib

TODO: Without matplotlib later

"""

from matplotlib.path import Path
ans = 0
path = Path(plots)
for r in range(MXN):
  for c in range(MXN):
    if G[r][c] == '#' or path.contains_point((r, c)):
      ans += 1

print(ans)



































