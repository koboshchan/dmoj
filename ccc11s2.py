import sys

input = sys.stdin.readline

n = int(input())

answer = [input().strip() for _ in range(n)]
correct = [input().strip() for _ in range(n)]

score = 0

for a, c in zip(answer, correct):
    if a == c:
        score += 1

print(score)