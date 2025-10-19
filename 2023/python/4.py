import sys
import re
from collections import defaultdict
D = open("in.txt").read().strip()
LINES = D.split('\n')

mp = defaultdict (int)
ans = 0
for idx,line in enumerate(LINES):
	curr_card = idx + 1
	mp [curr_card] += 1
	l,tot = line.split('|')
	cardnum, cards = l.split(':')
	cards = [int (x) for x in cards.split()]
	tot = [int (x) for x in tot.split()]
	matches = len(set(tot) & set(cards))

	for nxt_card in range (curr_card + 1, curr_card + matches + 1):
		mp [nxt_card] += mp [curr_card];
	ans += mp [curr_card]
print (ans)
