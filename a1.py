n = int(input())
for i in range(n):
    inp = input().split(" ")
    tmp = list(inp[1])
    del tmp[int(inp[0])-1]
    tmp = "".join(tmp)
    print("%d %s" % (i+1, tmp))