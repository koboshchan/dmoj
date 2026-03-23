# Problem S1: Baby Hop, Giant Hop

"""
Problem Description
Samantha the Frog is hopping between lily pads arranged in a straight line, evenly spaced.
There are an infinite number of lily pads. The lily pads are numbered, in order, using integers.
For every integer, there is also a lily pad.
Samantha starts on a lily pad numbered A and would like to hop onto a lily pad numbered
B. She can take a giant hop of length K, or a baby hop of length 1. Each hop can be either
forwards or backwards.
Samantha would like to know the fewest number of hops needed to get from A to B. But
sometimes, she would like to know the second fewest number of hops needed.
Input Specification
The first line of input contains a single integer, A, the starting lily pad (−1018 ≤ A ≤ 1018).
The second line of input contains a single integer, B, the ending lily pad (−1018 ≤ B ≤ 1018).
The third line of input contains a single integer, K, the distance of a giant hop (2 ≤ K ≤
1018).
The fourth line of input contains the integer, T , which is either 1 or 2, indicating if the fewest
(when T = 1) or second fewest (when T = 2) number of steps should be found.
"""

import os

debug = os.environ.get("QODANA_TOKEN", False)


def printDebug(*k):
    if debug:
        print(*k)


def fin(*k):
    print(*k)
    exit()


a, b, k, t = [int(input()) for _ in range(4)]

if a == b:
    fin(0 if t == 1 else 2)

diff = abs(a - b)
rest = diff % k
base = diff // k

printDebug(diff, rest, base)

if t == 1:
    fin(min((abs(rest - k) + 1 + base), (base + rest)))
elif t == 2:
    if (abs(rest - k) + 1 + base) == (base + rest):
        printDebug("same 2", (abs(rest - k) + 1 + base), (base + rest))
        fin(max((abs(rest - k) + 1 + base), (base + rest)) + 2)
    else:
        fin(max((abs(rest - k) + 1 + base), (base + rest)))
