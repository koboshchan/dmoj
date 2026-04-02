inp=[]
for i in range(6):
    inp.append(input())

inp=("".join(inp)).upper()

if inp.count("W") in [5,6]:
    print(1)
elif inp.count("W") in [3,4]:
    print(2)
elif inp.count("W") in [1,2]:
    print(3)
else:
    print(-1)