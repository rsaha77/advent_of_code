import sys

data = sys.stdin.read().split('\n\n')
presents, hash_cnt = [], []

for d in data[:-1]:
  grid, cnt = [], 0
  for line in d.splitlines()[1:]:
    grid.append(line)
    cnt += sum(ch=='#' for ch in line)
  presents.append(grid)
  hash_cnt.append(cnt)

total, cannot, can, not_sure = 0, 0, 0, 0
for line in data[-1].splitlines():
  total += 1
  line = line.split(':')
  R, C = tuple(map(int,line[0].split('x')))
  quantities = list(map(int, line[1].split()))

  min_req_slots = sum(cnt * hash_cnt[i] for i, cnt in enumerate(quantities))
  tot_presents = sum(quantities)

  if min_req_slots > R*C:
    cannot += 1
  elif tot_presents <= (R//3) * (C//3):
    # each present can have its own 3x3 block
    can += 1
  else:
    # NP-Complete
    not_sure += 1

# print(f"can: {can}")
# print(f"cannot: {cannot}")
# print(f"NP-Complete: {not_sure}") # 0

assert (not_sure == 0)
print("p1: ", can)


