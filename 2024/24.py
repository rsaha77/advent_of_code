import re
import sys
from copy import deepcopy
from collections import defaultdict

file = "in.txt"
try:
    file = sys.argv[1]
except IndexError:
    pass

inp = open(file).read().strip()
LINES = inp.split("\n")


def remove_chars(text, chs):
  ret = "".join([ch for ch in text if ch not in chs])
  return ret


def get_result(a, oper, b):
  if oper ==  'AND':
    return a&b
  elif oper == 'OR':
    return a|b
  return a^b


def get_decimal_z (vals, equations):

  while True:
    still_got = False
    for i, [a, opr, b, res] in enumerate(equations):
      if type(a) != int and a in vals:
        a = vals[a]
        equations[i][0] = a
      if type(b) != int and b in vals:
        b = vals[b]
        equations[i][2] = b
      if type(a) == int and type(b) == int:
        res_val = get_result (a, opr, b)
        vals[res] = res_val
      else:
        still_got = True

    if not still_got:
      break

  bin_z = []
  for k,v in vals.items():
    if k.startswith('z'):
      bin_z.append([k,v])

  bin_z.sort(key=lambda x: x[0], reverse=True)
  bin_z = ''.join([str(_[1]) for _ in bin_z])
  dec_z = int(bin_z, 2)
  return dec_z


def get_vals_dict(bin_x, bin_y):
  vals = defaultdict(int)
  ln = len(bin_x)
  for i in range(ln-1, -1, -1):
    pos = ln-1-i
    bit_x, bit_y = bin_x[i], bin_y[i]
    key_x, key_y = f'x{str(pos).zfill(2)}', f'y{str(pos).zfill(2)}'
    vals[key_x], vals[key_y] = int(bit_x), int(bit_y)
  return vals

def perform_swap(EQ, SWAPS):
  # print(EQ)
  for i, (a,op,b,res) in enumerate(EQ):
    for p,q in SWAPS:
      if res == p:
        EQ[i][3] = q
      if res == q:
        EQ[i][3] = p


def graph_visualisation(EQ, fname):

  with open('input.dot', 'w') as f:
    f.write('strict digraph {')
    for gate in EQ:
      a,op,b,res = gate
      f.write(f'  {a} -> {res} [label={op}]')
      f.write(f'  {b} -> {res} [label={op}]')
    f.write('}')

  from graphviz import Source
  # Graph visualisation
  Source.from_file('input.dot').render(fname, format='pdf', view=True)


def find_diff_positions(bin1, bin2):
    max_len = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)
    diff_positions = []
    for i in range(max_len):
      if bin1[i] != bin2[i]:
        diff_positions.append(max_len - i)
    return diff_positions


def main():
  ans1, ans2 = 0, 0
  nxt = False
  vals = defaultdict(int)
  equations = []
  for ln, line in enumerate(LINES):
    if len(line) == 0:
      nxt = True
      continue
    if not nxt:
      a,b = line.split(': ')
      vals[a] = int(b)
    else:
      line = remove_chars(line, "->")
      line = line.split(' ')
      a, oper, b, res = line[0], line[1], line[2], line[4]
      equations.append([a,oper,b,res])

  EQ = deepcopy(equations)
  ans1 = get_decimal_z(vals, equations)

  print("p1: ", ans1)

  graph_visualisation(EQ, "output_before_swaps")
  SWAPS = []
  ## Manually filled in after visualising the DAG circuit ##
  SWAPS.append(["djg", "z12"])
  SWAPS.append(["sbg", "z19"])
  SWAPS.append(["dsd", "z37"])
  SWAPS.append(["mcq", "hjm"])
  perform_swap(EQ, SWAPS)
  graph_visualisation(EQ, "output_after_swaps")
  
  success, failure = 0, 0
  for i in range(0,45):
    for j in range(0, 45):
      x, y = 1 << i, 1 << j
      bin_x = bin(x)[2:].zfill(45)
      bin_y = bin(y)[2:].zfill(45)
      vals = get_vals_dict(bin_x, bin_y)
      equations = deepcopy(EQ)
      actual_z = get_decimal_z(vals, equations)
      expected_z = x + y
      if actual_z != expected_z:
        print("actual_z: ", actual_z)
        print("expected_z: ", expected_z)
        print(bin(actual_z)[2:])
        print(bin(expected_z)[2:])
        # Below helps to find affected bits of z. We trace back by visualising the circuit to get affected pairs.
        print(find_diff_positions(bin(actual_z)[2:], bin(expected_z)[2:]))
        print()
        # print("Failed Adder ... ")
        failure += 1
      else:
        success += 1
  print("success: ", success)
  print("failure: ", failure)


  # print("p1: ", ans1)
  swapped_wires = []
  for wire1, wire2 in SWAPS:
    swapped_wires.append(wire1)
    swapped_wires.append(wire2)
  print("p2: ", ','.join(sorted(swapped_wires)))


if __name__ == "__main__":
  main()
