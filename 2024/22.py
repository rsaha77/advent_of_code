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


def find_secrets (secret, LIMIT):
  secrets = [secret]
  for _ in range(LIMIT):
    secret = prune(mix(secret, secret * 64))
    secret = prune(mix(secret, secret // 32))
    secret = prune(mix(secret, secret * 2048))
    secrets.append(secret)
  return secrets


def get_seq_banana_dict (secrets):
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
  LIMIT = 2000
  seq_tot_banana = defaultdict(int)

  for ln, line in enumerate(LINES):
    secrets = find_secrets (int(line), LIMIT)
    ans1 +=  secrets[LIMIT]
    seq_banana = get_seq_banana_dict (secrets)
    for seq, banana in seq_banana.items():
      seq_tot_banana[seq] += banana

  ans2 = max(seq_tot_banana.values())

  
  print("p1: ", ans1)
  print("p2: ", ans2)

if __name__ == "__main__":
  main()


