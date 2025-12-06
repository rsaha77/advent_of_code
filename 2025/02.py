import sys

def main():
  line = sys.stdin.read()
  p1, p2 = 0, 0
  for x in line.split(','):
    a,b = map(int,x.split('-'))
    for num in range(a,b+1):
      s = str(num)
      ln = len(s)
      mid = ln//2
      if not ln & 1  and s[:mid] == s[mid:]:
        p1 += num
      if s in (s + s)[1:-1]:
        p2 += num
  print("p1: ", p1)
  print("p2: ", p2)

if __name__ == "__main__":
  main()