import sys
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


def hash(op):
    val = 0
    for ch in op:
        val = ((val + ord(ch)) * 17) % 256
    return val


def solve_p2(opers):
    boxes = [[] for b in range(256)]
    ans = 0
    for op in opers:
        todo = "add" if "=" in op else "rmv"
        label = op[:-1] if op.endswith('-') else op[:-2]
        hash_val = hash(label)
        focal_length = int(op[-1]) if "=" in op else 0

        if todo == "rmv":
            boxes [hash_val] = [[LB, FL] for LB, FL in boxes[hash_val] if label != LB]
        if todo == "add":
            if label in [LB for LB,FL in boxes[hash_val]]:
                boxes[hash_val] = [[LB, focal_length if LB == label else FL] for LB,FL in boxes[hash_val]]
            else:
                boxes[hash_val].append([label, focal_length])

    ans=0
    for box_num, hash_val in enumerate(boxes):
      for slot, LB_FL in enumerate(hash_val):
        ans += (box_num + 1) * (slot + 1) * LB_FL[1]

    return ans



def main():
    opers = inp.split(',')
    p1=0
    for op in opers:
        p1 += hash(op)
    print("p1:", p1)
    print("p2:", solve_p2(opers)) # preferred as dict only has one item, so we use list


if __name__ == "__main__":
    main()


















