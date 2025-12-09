import os
import sys
import matplotlib as mpl
from matplotlib import font_manager
import matplotlib.pyplot as plt
import mplcursors
from itertools import combinations, pairwise
from shapely import Polygon, box


if not os.environ.get('MPLBACKEND'):
  mpl.use('MacOSX')


def _init_matplotlib():
  try:
    font_manager._load_fontmanager(try_read_cache=False)
  except Exception:
    pass


def visualise_pts(pts, n):
  if not pts:
    print('no points to visualise')
    return None, None

  _init_matplotlib()
  xs = [x for x, y in pts]
  ys = [y for x, y in pts]
  fig, ax = plt.subplots(figsize=(6, 6))
  sc = ax.scatter(xs, ys, s=30, c='blue', label='points', picker=True)
  sc._poly_pts = pts  # store original input tuples

  cursor = mplcursors.cursor(sc, hover=True)
  @cursor.connect('add')
  def on_add(sel):
    i = sel.index
    x, y = sc._poly_pts[i]
    sel.annotation.set_text(f'({x}, {y})')
    sel.annotation.get_bbox_patch().set(fc='white', alpha=0.8)

  if n >= 3:
    poly = Polygon(pts)
    if not poly.is_valid:
      poly = poly.buffer(0)
    xpoly, ypoly = poly.exterior.xy
    line, = ax.plot(xpoly, ypoly, color='orange', linewidth=2, label='polygon')
    line.set_picker(False)  # ignore edges in hover

  ax.set_aspect('equal', adjustable='box')
  ax.grid(True, linestyle='--', alpha=0.4)
  ax.legend()
  ax.set_title('Input points')
  ax.set_xlabel('x')
  ax.set_ylabel('y')
  plt.tight_layout()
  plt.show()
  return fig, ax


def sort_point(pairs):
  return [((min(x1, x2), min(y1, y2)), (max(x1, x2), max(y1, y2))) for (x1, y1), (x2, y2) in pairs]


def solve_with_shapely(pts):
  poly = Polygon(pts)
  n = len(pts)
  p1 = p2 = 0
  for i in range(n):
    for j in range(i+1, n):
      c1, r1 = pts[i]
      c2, r2 = pts[j]
      area = (abs(r2-r1)+1) * (abs(c2-c1)+1)
      p1 = max (p1, area)
      if p2 < area:
        rectangle = box(min (c1, c2), min (r1, r2), max(c1, c2), max(r1, r2))
        if poly.covers(rectangle):
          p2 = area
  print("p1: ", p1)
  print("p2: ", p2)


def solve(poly_pts):
  poly_edges = sort_point(pairwise(poly_pts + [poly_pts[0]]))
  p1 = p2 = 0
  for (x1, y1), (x2, y2) in sort_point(combinations(poly_pts, 2)):  # diagonals, sorted to makes sure x1<x2 and y1<y2
    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    p1 = max(p1, area)
    if area > p2:
      for (ex1, ey1), (ex2, ey2) in poly_edges:
        # Either p1==p2 (ver edge) or q1==q2 (hor edge)
        if (((ex1 == ex2 and x1 < ex1 < x2) and (ey2 > y1 and ey1 < y2)) or
            ((ey1 == ey2 and y1 < ey1 < y2) and (ex2 > x1 and ex1 < x2))):
          break
      else:
        p2 = area

  print("p1: ", p1)
  print("p2: ", p2)


def main():
  lines = sys.stdin.read().splitlines()
  poly_pts = list(tuple(map(int, line.split(','))) for line in lines)
  visualise_pts(poly_pts, len(poly_pts)) # Uncomment to visualise input
  # solve_with_shapely(poly_pts) # Solved using shapely library
  solve(poly_pts) # Faster by 0.4sec on the input data


if __name__ == '__main__':
  main()
