from collections import deque
from rich import print


def sum_(dat):
    out = []
    for i in dat:
        out += i
    return out

def splitList(l, index):
    l = list(l.copy())
    return l[:index], l[index:]

def checkRank(rank, taller, shorter, index):
    rank=rank.copy()
    tallerCheck,shorterCheck = splitList(rank,index)
    tallerCheck,shorterCheck,taller,shorter
    breakpoint
    for i in taller:
        # if not i in rank:
        #     continue
        if (not (i in tallerCheck)):
            # breakpoint
            return False
    for i in shorter:
        # if not i in rank:
        #     continue
        if (not (i in shorterCheck)):
            return False
    breakpoint
    return True
n, m = list(map(int, input().split(" ")))
adj = [input().split(" ") for _ in range(m)]
p, q = input().split(" ")

queue = deque(adj.copy())
peoples = list(set(sum_(adj)))

# for i in range(n):
#     adj.append([i+1])
# print(bfsDisconnected(adj))

rank = deque(queue.popleft())
unknown = [i + 1 for i in range(n)]

unknown
queue

for person in peoples:
    rankBefore = rank.copy()
    if person in rank: continue
    taller = []
    shorter = []
    for x, y in adj:
        if x == person:
            breakpoint
            taller.append(y)
        elif y == person:
            breakpoint
            shorter.append(x)
    for i in range(len(rank)):
        r = checkRank(rankBefore,taller,shorter,i)
        rankBefore,taller,shorter,i
        breakpoint
        if checkRank(rankBefore,taller,shorter,i):
            rank.insert(i,person)
            breakpoint
        # breakpoint
    adj
    [p, q]
    rank
    breakpoint


adj
[p, q]
rank
breakpoint
# stdin
"""
10 3
1 2
2 3
3 4
1 4
"""
