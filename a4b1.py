n=int(input())
dat = [int(input()) for _ in range(n)]
dat.sort()
print("\n".join(map(str, dat)))