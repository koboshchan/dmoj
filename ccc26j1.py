b,t,p = [int(input()) for _ in range(3)]

if t-p-b < 0:
    print("N")
else:
    print("Y", t-p-b)