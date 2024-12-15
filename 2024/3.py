import re
import sys

file = "in.txt"
try:
    file = sys.argv[1]
except IndexError:
    pass


inp = open(file).read().strip()
LINES = inp.split("\n")


def print_grid(mark):
  for g in mark:
    print(g)
  print()


def extract_mul_with_indexes(input_string):
  mul_pattern = r'mul\((\d+),\s*(\d+)\)'
  result = []
  index = 0
  while index < len(input_string):
    mul_match = re.search(mul_pattern, input_string[index:])
    if mul_match:
      x, y = mul_match.groups()
      start_index = index + mul_match.start()
      result.append((start_index, (int(x), int(y))))  # Append index first
      index += mul_match.end()  # Move index past the current match
      continue
    index += 1

  return result



def extract_do_with_indexes(input_string):
  do_pattern = r'do\(\)'
  result = []
  index = 0
  while index < len(input_string):
    do_match = re.search(do_pattern, input_string[index:])
    if do_match:
      start_index = index + do_match.start()
      result.append((start_index, 'do'))
      index += do_match.end()
      continue
    index += 1
    return result


def extract_dont_with_indexes(input_string):
  dont_pattern = r"don't\(\)"
  result = []
  index = 0
  while index < len(input_string):
    dont_match = re.search(dont_pattern, input_string[index:])
    if dont_match:
      start_index = index + dont_match.start()
      result.append((start_index, 'dont')) 
      index += dont_match.end()
      continue
    index += 1
  return result


def merge_and_sort_lists(list1, list2, list3):
    merged_list = list1 + list2 + list3
    sorted_list = sorted(merged_list, key=lambda x: x[0])
    return sorted_list


def main():
  ans1, ans2 = 0, 0
  can = True
  for ln, line in enumerate(LINES):
    L1 = extract_mul_with_indexes(line)
    L2 = extract_do_with_indexes(line)
    L3= extract_dont_with_indexes(line)
    L= merge_and_sort_lists(L1, L2, L3)
    
    for _,x in L:
      if x not in ['dont', 'do']:
        a, b = x
        ans1 += a*b
      if x == 'dont':
        can = False
      elif x == 'do':
        can = True
      elif can:
        a, b = x
        ans2 += a*b
        
  print("p1: ", ans1)
  print("p2: ", ans2)


if __name__ == "__main__":
  main()







