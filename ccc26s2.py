n, l, q = [int(input()) for _ in range(3)]

diff = [0] * (n + 2)

for _ in range(l):
    pi, si = map(int, input().split())
    left = max(1, pi - si)
    right = min(n, pi + si)
    diff[left] += 1
    diff[right + 1] -= 1

illuminated = [False] * (n + 1)
count = 0
for i in range(1, n + 1):
    count += diff[i]
    illuminated[i] = count > 0

for _ in range(q):
    spot = int(input())
    print("Y" if illuminated[spot] else "N")
