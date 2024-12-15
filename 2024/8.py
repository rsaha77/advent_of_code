import re
import sys
# import numpy
import math
from graphlib import TopologicalSorter
from itertools import product, combinations
from functools import cache
from heapq import heappush as hpush, heappop as hpop
from collections import defaultdict, Counter

# sys.setrecursionlimit(int(1e6))

file = "in.txt"
try:
    file = sys.argv[1]
except IndexError:
    pass

inp = open(file).read().strip()
LINES = inp.split("\n")


def ins(r, c, R, C):
  return 0 <= r < R and 0 <= c < C


def print_grid(mark):
  R, C = len(mark), len(mark[0])
  for r in range(R):
    for c in range(C):
      print(mark[r][c],end="")
    print()
  print()


def calculate_distance(point1, point2):
  return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def find_antinodes_part1 (pt1, pt2, R, C):
  # print(pt1,pt2)
  x1, y1 = pt1
  x2, y2 = pt2
  dx, dy = x1 - x2, y1 - y2

  # print("Slope: ", dx, dy)

  ant1 = (x1-dx, y1-dy)
  ant2 = (x1+dx, y1+dy)
  ant3 = (x2-dx, y2-dy)
  ant4 = (x2+dx, y2+dy)

  # print("================")
  # print(ant1)
  # print(ant2)
  # print(ant3)
  # print(ant4)
  # print("================")

  points = [ant1, ant2, ant3, ant4]
  max_distance = 0
  point_pair = (None, None)

  for i in range(len(points)):
    for j in range(i + 1, len(points)):
      dist = calculate_distance(points[i], points[j])
      if dist > max_distance:
        max_distance = dist
        point_pair = (points[i], points[j])

  p1, p2 = point_pair
  r1, c1 = p1
  r2, c2 = p2
  ret_pair = []
  if ins(r1,c1,R,C):
    ret_pair.append((r1, c1))
  if ins(r2,c2,R,C):
    ret_pair.append((r2, c2))

  return ret_pair


def find_antinodes_part2 (pt1, pt2, R, C):
  # print(pt1,pt2)
  x1, y1 = pt1
  x2, y2 = pt2
  dx, dy = x1 - x2, y1 - y2

  # print("Slope: ", dx, dy)

  ret_pts = []

  tx, ty = x1, y1
  while ins(tx, ty, R, C):
    ret_pts.append((tx,ty))
    tx += dx
    ty += dy

  tx, ty = x1, y1
  while ins(tx, ty, R, C):
    ret_pts.append((tx,ty))
    tx -= dx
    ty -= dy

  return ret_pts


def main():
  ans1, ans2 = 0, 0
  grid = []
  for ln, line in enumerate(LINES):
    # print(line)
    grid.append(line)

  R, C = len(grid), len(grid[0])

  pts_dict = defaultdict(list)
  for r in range(R):
    for c in range(C):
      ch = grid[r][c]
      if ch != '.':
        pts_dict[ch].append((r,c))

  # print(pts_dict)

  
  for part in ["p1", "p2"]:
    antinodes_plot = [[grid[r][c] for c in range(C)] for r in range(R)]
    antinodes_pts = set()
    for antena, location in pts_dict.items():
      antena_pairs = list(combinations(location, 2))
      # print(antena_pairs)
      # Generate all #
      for pt_pair in antena_pairs:
        pt1, pt2 = pt_pair
        if part == "p1":
          current_antinodes = find_antinodes_part1 (pt1, pt2, R, C)
        else:
          current_antinodes = find_antinodes_part2 (pt1, pt2, R, C)
        for antinodes in current_antinodes:
          antinodes_pts.add(antinodes)
          antinodes_plot[antinodes[0]][antinodes[1]] = '#'
    # print_grid(antinodes_plot)
    print(f"{part} :{len(antinodes_pts)}")


if __name__ == "__main__":
  main()






























