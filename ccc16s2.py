"""
Question 1: what is the minimum total speed, out of all possible assignments into pairs?
Question 2: what is the maximum total speed, out of all possible assignments into pairs?

The first line will contain the type of question you are to solve, which is either 1 or 2 .
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

type_of_question = input()

n = int(input())

dmojistan = list(map(int, input().split()))
pegland = list(map(int, input().split()))

if type_of_question == "1":
    dmojistan.sort()
    pegland.sort()

    total_speed = 0

    for i in range(n):
        total_speed += max(dmojistan[i], pegland[i])

    print(total_speed)
else:
    dmojistan.sort()
    pegland.sort()

    total_speed = 0

    for i in range(n):
        total_speed += max(dmojistan[i], pegland[n - 1 - i])

    print(total_speed)