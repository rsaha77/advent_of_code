import sys
from scipy.optimize import linprog


def solve1(buttons, light):
  curr_min = float('inf')
  for comb in range(2**len(buttons)):
    my_light = ['.'] * len(light)
    tot = 0
    for idx in range(len(buttons)):
      if (comb >> idx) & 1:
        tot += 1
        curr_btn = buttons[idx]
        for btn in curr_btn:
          current_state = my_light[btn]
          my_light[btn] = '#' if current_state == '.' else '.'
    my_light = ''.join(my_light)
    if light == my_light:
      curr_min = min(curr_min, tot)
  return curr_min


def solve2(buttons, joltage):
    cost = [1 for _ in buttons]
    constraint_matrix = [[i in b for b in buttons] for i in range(len(joltage))]
    return linprog(c=cost, A_eq=constraint_matrix, b_eq=joltage, integrality=1).fun


def main():
  p1 = p2 = 0
  data = sys.stdin.read()
  for line in data.splitlines():
    light, buttons, joltage = [], [], []
    line = line.split()
    light = line[0][1:-1]
    for button in line[1:-1]:
      buttons.append(tuple(map(int, button[1:-1].split(','))))
    for jlt in line[-1][1:-1].split(','):
      joltage.append(int(jlt))

    p1 += solve1(buttons, light)
    p2 += solve2(buttons, joltage)

  print("p1: ", p1)
  print("p2: ", int(p2))


if __name__ == "__main__":
  main()