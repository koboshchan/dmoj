def printDebug(*k):
    pass


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
