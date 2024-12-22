import sys
from collections import defaultdict


file = "in.txt"
try:
    file = sys.argv[1]
except IndexError:
    pass


inp = open(file).read().strip()
LINES = inp.split("\n")


def mix (secret, val):
  return secret ^ val


def prune (secret):
  return secret % 16777216


def find_secret(secret, LIMIT):
  secret_list = [secret]
  for _ in range(LIMIT):
    secret = prune(mix(secret, secret * 64))
    secret = prune(mix(secret, secret // 32))
    secret = prune(mix(secret, secret * 2048))
    secret_list.append(secret)
  return secret_list


def get_seq_maxbanana_dict(secrets):
  bananas = [secret % 10 for secret in secrets]

  changes = [None]
  for i in range(1, len(secrets)):
    changes.append(bananas[i] - bananas[i-1])

  mp = {}
  for i in range(4,len(changes)):
    a,b,c,d = changes[i-3], changes[i-2], changes[i-1], changes[i]
    if (a,b,c,d) not in mp:
      mp[(a,b,c,d)] = bananas[i]

  return mp


def main():
  ans1, ans2 = 0, 0
  D = defaultdict(int)
  LIMIT = 2000

  for ln, line in enumerate(LINES):
    secret_list = find_secret (int(line), LIMIT)
    ans1 +=  secret_list[LIMIT]
    seq_maxbanana_dict = get_seq_maxbanana_dict(secret_list)
    for seq, max_banana in seq_maxbanana_dict.items():
      D[seq] += max_banana

  ans2 = max(D.values())

  
  print("p1: ", ans1)
  print("p2: ", ans2)

if __name__ == "__main__":
  main()


