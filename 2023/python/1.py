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

mp = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def isnewdig (line, idx, rev=False):
	n = len(line)
	s = ""
	if not rev:
		for i in range (idx, n):
			l = line [i]
			s += l
			num = mp.get(s, None)
			if num != None:
				return num
	else:
		for i in range (idx, n):
			l = line [i]
			s += l
			num = mp.get(s, None)
			if num != None:
				return num

	return -1

ans = 0
for idx,line in enumerate(lines):

	for i,l in enumerate(line):
		if l.isdigit():
			f = int(l)
			break
		ft = isnewdig(line, i)
		if ft > -1:
			f = ft
			break

	n = len (line)
	for i in reversed(range(n)):
		l = line[i]
		if l.isdigit():
			s = int(l)
			break
		st = isnewdig(line, i, True)
		if st > -1:
			s = st
			break

	print (f, s)
	ans += f*10 + s


print (ans)


