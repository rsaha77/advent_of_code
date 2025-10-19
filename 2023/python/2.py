import sys
import re
from collections import defaultdict
D = open("in.txt").read().strip()
lines = D.split('\n')


def keep_alphanumeric_spaces(text):
    ret = ''.join(ch if ch.isalnum() or ch.isspace() else '' for ch in text)
    return ret

def remove_chs (text, chs):
	ret = ''.join([ch for ch in text if ch not in chs])
	return ret

ans = 0
mp = defaultdict(int)
for idx,line in enumerate(lines):
	line = remove_chs (line, ";,:")
	tot = [x for x in line.split()]
	prev = "foo"
	mxr, mxb, mxg = 0,0,0
	for x in tot:
		if x == "red":
			mxr = max (mxr, int(prev))
		if x == "blue":
			mxb = max (mxb, int(prev))
		if x == "green":
			mxg = max (mxg, int(prev))
		prev = x;
	ans += (mxr * mxb * mxg)
	mp [ans] = ans + 5
print (ans)

