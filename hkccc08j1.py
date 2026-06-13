def product(x,y):
    return x*y

c = int(input())
c_fih = [product(*map(int, input().split())) for _ in range(c)]
n = int(input())
n_fih = [product(*map(int, input().split())) for _ in range(n)]
c_max = max(c_fih)
n_max = max(n_fih)
if c_max > n_max:
    print("Casper")
elif n_max > c_max:
    print("Natalie")
else:
    print("Tie")