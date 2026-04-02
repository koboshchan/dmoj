M, N = int(input()), int(input())
canvas = [[0 for _ in range(N)] for _ in range(M)]
tmp = int(input())
tmp2 = [input() for _ in range(tmp)]
rulls={}
for i in tmp2:
    if i in rulls:del rulls[i]
    else:rulls[i]=None

for tmp3123 in rulls:
    rc, num = tmp3123.split()
    num = int(num)
    if rc == "R":
        for i in range(N):canvas[num-1][i]+=1
    elif rc == "C":
        for i in range(M):canvas[i][num-1]+=1
canvasGold=0
for i in canvas:
    for j in i:
        if j%2==1:
            canvasGold +=1
print(canvasGold)