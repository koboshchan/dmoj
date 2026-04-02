"I, O, S, H, Z, X, N"

inp  = input()

for i in inp:
    if i not in "IOSHZXN":
        print("NO")
        break
else:
    print("YES")