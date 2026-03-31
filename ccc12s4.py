from collections import deque


def read_cases():
    """Read test cases interactively until a line with single 0."""
    cases = []
    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        if not line:
            continue
        n = int(line)
        if n == 0:
            break
        nums = []
        while len(nums) < n:
            part = input().strip()
            if not part:
                continue
            nums.extend(map(int, part.split()))
        cases.append(nums[:n])
    return cases


def goal_state(n):
    return tuple((i,) for i in range(1, n + 1))


def initial_state(arr):
    return tuple((x,) for x in arr)


def can_place(coin, dest_stack):
    return (not dest_stack) or (coin <= dest_stack[-1])


def neighbors(state):
    m = len(state)
    for i in range(m):
        if state[i]:
            coin = state[i][-1]
            # move left
            if i - 1 >= 0 and can_place(coin, state[i - 1]):
                new_state = list(state)
                new_state[i] = state[i][:-1]
                new_state[i - 1] = state[i - 1] + (coin,)
                yield tuple(new_state)
            # move right
            if i + 1 < m and can_place(coin, state[i + 1]):
                new_state = list(state)
                new_state[i] = state[i][:-1]
                new_state[i + 1] = state[i + 1] + (coin,)
                yield tuple(new_state)


def bfs_min_moves(initial, goal):
    if initial == goal:
        return 0
    q = deque([initial])
    dist = {initial: 0}
    while q:
        s = q.popleft()
        d = dist[s]
        for t in neighbors(s):
            if t not in dist:
                nd = d + 1
                if t == goal:
                    return nd
                dist[t] = nd
                q.append(t)
    return None


def solve_case(arr):
    n = len(arr)
    res = bfs_min_moves(initial_state(arr), goal_state(n))
    return str(res) if res is not None else "IMPOSSIBLE"


def main():
    cases = read_cases()
    for arr in cases:
        print(solve_case(arr))


if __name__ == "__main__":
    main()