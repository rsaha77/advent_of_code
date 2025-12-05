import sys

def main():
  p1 = p2 = 0
  lines = sys.stdin.read()
  ranges, nums = lines.split('\n\n')

  ranges = list(tuple(map(int, rng.split('-'))) for rng in ranges.splitlines())
  nums = list(map(int,nums.splitlines()))

  for num in nums:
    for (a,b) in ranges:
      if a <= num <= b:
        p1 += 1
        break

  ranges = sorted(ranges)
  ptr = 0
  for (a,b) in ranges:
    if b < ptr:
      continue
    ptr = max(ptr, a)
    p2 += b - ptr + 1
    ptr = b + 1

  print("p1: ", p1)
  print("p2: ", p2)


if __name__ == "__main__":
  main()
