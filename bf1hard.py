n = int(input())
inp = [int(input()) for _ in range(n)]
inp.sort()
print("\n".join(map(str, inp)))