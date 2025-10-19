import sys
import re
from collections import defaultdict, Counter
D = open("in.txt").read().strip()
LINES = D.split('\n')


def get_rank_1(hand):
    counts = Counter(hand)
    unique_counts = len(counts)

    if unique_counts == 1:
        # Five of a kind
        return 1
    elif unique_counts == 2:
        # Four of a kind or Full house
        if 4 in counts.values():
            return 2
        else:
            return 3
    elif unique_counts == 3:
        # Three of a kind or Two pair
        if 3 in counts.values():
            return 4
        else:
            return 5
    elif unique_counts == 4:
        # One pair
        return 6
    else:
        # High card
        return 7


all_cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10,
               '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}


def get_rank_2(hand):
    ranks = [-card_values[card] for card in hand]
    return ranks


cards = []

for i, line in enumerate(LINES):
    card, num = line.split()
    cards.append([card, num, 0, 0])


def solve(cards, part):
    if part == "p2":
        card_values['J'] = 1
    for i, card in enumerate(cards):
        winning_score = get_rank_1(card[0])
        if part == "p2":
            for ch in all_cards:
                changed_hand = list(card[0])
                for i, c in enumerate(changed_hand):
                    if c == 'J':
                        changed_hand[i] = ch
                winning_score = min(
                    winning_score, get_rank_1(''.join(changed_hand)))
        card[2] = winning_score
        card[3] = get_rank_2(card[0])

    cards = sorted(cards, key=lambda x: (x[2], x[3]))

    idx, ans = len(cards), 0
    for card in cards:
        ans += int(card[1]) * idx
        idx -= 1
    return ans


print("part 1: ", solve(cards, "p1"))
print("part 2: ", solve(cards, "p2"))
