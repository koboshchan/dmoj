import sys
sys.setrecursionlimit(100000)
R=int(input())
C=int(input())
total=0
map_=[]
price={"S":1,"M":5,"L":10,"*":-1}
for i in range(R):
    map_.append(input())
x_,y_=int(input()),int(input())
betterMap=[list(map(lambda x: price[x],i)) for i in map_]
def noOutOfRange(x,y):
    x=x[0]
    y=y[0]
    if x>=R or y>=C or x<0 or y<0:
        return -1
    else:
        return betterMap[x][y]
def check(x,y):
    # print(x,y)
    global total
    if x>=R or y>=C or x<0 or y<0:
        return
    if betterMap[x][y] == -1 or betterMap[x][y] == 0:
        return
    total+=betterMap[x][y]
    betterMap[x][y]=0
    check(x+1,y)
    check(x-1,y)
    check(x,y+1)
    check(x,y-1)
    if not ((noOutOfRange([x],[y-1]) == -1) and(noOutOfRange([x-1],[y]) == -1)):
        check(x-1,y-1)
    if not ((noOutOfRange([x],[y+1]) == -1) and(noOutOfRange([x-1],[y]) == -1)):
        check(x-1,y+1)
    if not ((noOutOfRange([x],[y-1]) == -1) and(noOutOfRange([x+1],[y]) == -1)):
        check(x+1,y-1)
    if not ((noOutOfRange([x],[y+1]) == -1) and(noOutOfRange([x+1],[y]) == -1)):
        check(x+1,y+1)
check(x_,y_)
print(total)