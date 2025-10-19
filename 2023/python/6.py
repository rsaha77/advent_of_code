import sys
import re
from collections import defaultdict
D = open("in.txt").read().strip()
LINES = D.split('\n')


def keep_alpnum_spaces(text):
    ret = ''.join(ch if ch.isalnum() or ch.isspace() else '' for ch in text)
    return ret

def remove_chars (text, chs):
	ret = ''.join([ch for ch in text if ch not in chs])
	return ret


mp, mp1, mp2 = defaultdict (int), defaultdict (int), defaultdict (int)

for line in LINES:
	foo, bar = line.split (':')
	mp1 [foo] = [int (x) for x in bar.split()]
	mp2 [foo] = [int("".join(bar.split()))]


def solve (p):
	ans = 1
	mp = mp1 if p == "p1" else mp2
	for i in range(len(mp["Time"])):
		t, d = mp["Time"][i], mp["Distance"][i]
		ctr = 0
		for hold in range(1,  t):
			rem = t - hold
			trav = hold*rem
			if trav > d:
				ctr += 1 
		if ctr > 0:
			ans *= ctr
	return ans

print (solve ("p1"))
print (solve ("p2"))





