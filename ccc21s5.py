import sys

sys.setrecursionlimit(20000)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    if a == 0 or b == 0: return 0
    return abs(a * b) // gcd(a, b)

input = sys.stdin.read().split()

if not input:
    exit()

N = int(input[0])
M = int(input[1])

queries = []
idx = 2
for _ in range(M):
    queries.append((int(input[idx]), int(input[idx+1]), int(input[idx+2])))
    idx += 3

del input

diff_arrays = [[0] * (N + 2) for _ in range(17)]

for x, y, z in queries:
    diff_arrays[z][x] += 1
    diff_arrays[z][y+1] -= 1
    
A = [1] * (N + 1)
for z in range(1, 17):
    current_count = 0
    for i in range(1, N + 1):
        current_count += diff_arrays[z][i]
        if current_count > 0:
            A[i] = lcm(A[i], z)

tree_size = 1
while tree_size < N:
    tree_size *= 2
tree = [0] * (2 * tree_size)

for i in range(1, N + 1):
    tree[tree_size + i - 1] = A[i]
    
for i in range(tree_size - 1, 0, -1):
    tree[i] = gcd(tree[2 * i], tree[2 * i + 1])
    
def query_gcd(l, r):
    l += tree_size - 1
    r += tree_size - 1
    res = 0
    while l <= r:
        if l % 2 == 1:
            res = gcd(res, tree[l])
            l += 1
        if r % 2 == 0:
            res = gcd(res, tree[r])
            r -= 1
        l //= 2
        r //= 2
    return res

for x, y, z in queries:
    if query_gcd(x, y) != z:
        print("Impossible")
        exit()

print(*(A[1:]))
