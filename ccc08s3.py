try:
    from termcolor import colored
    def debug(*args):
        print(*args)
        return
except ImportError:
    def colored(*args, **kwargs):
        return ""
    def debug(*args):
        return


def highlight(data,position):
    data = list(map(list, data))
    data[position[0]][position[1]] = colored(data[position[0]][position[1]], 'red', attrs=['bold'])
    data = "\n".join(list(map(lambda x: ''.join(x), data)))
    debug(data)

n=int(input())

data = []

for _ in range(n):
    n2 = int(input())
    __ = int(input())
    dat=[input() for _ in range(n2)]
    data.append(dat)

debug(data)
from collections import deque

DIRECTIONS = {
    '+': [(-1,0),(1,0),(0,-1),(0,1)],
    '-': [(0,-1),(0,1)],
    '|': [(-1,0),(1,0)],
}

def bfs(grid):
    R, C = len(grid), len(grid[0])
    visited = [[False]*C for _ in range(R)]
    q = deque([(0, 0, 1)])  # (row, col, steps)
    visited[0][0] = True

    while q:
        r, c, steps = q.popleft()
        if r == R-1 and c == C-1:
            return steps
        cell = grid[r][c]
        if cell not in DIRECTIONS:
            continue
        for dr, dc in DIRECTIONS[cell]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and grid[nr][nc] != '*':
                visited[nr][nc] = True
                q.append((nr, nc, steps+1))
    return -1


for i in data:
    debug(i)
    print(bfs(i))
    debug("\n")
    debug("=====================================")
    

"""
Test case #1: 	AC 	[0.031s, 	11.51 MB] 	(3/3)
Test case #2: 	WA 	[0.031s, 	11.57 MB] 	(0/3)
Test case #3: 	TLE 	[>1.000s, 	11.30 MB] 	(0/3)
Test case #4: 	WA 	[0.031s, 	11.49 MB] 	(0/3)
Test case #5: 	AC 	[0.072s, 	11.48 MB] 	(3/3)

Test case #1: 	AC 	[0.043s, 	56.38 MB] 	(3/3)
Test case #2: 	WA 	[0.044s, 	57.01 MB] 	(0/3)
Test case #3: 	TLE 	[>1.000s, 	88.01 MB] 	(0/3)
Test case #4: 	WA 	[0.045s, 	57.02 MB] 	(0/3)
Test case #5: 	AC 	[0.113s, 	59.97 MB] 	(3/3)
"""