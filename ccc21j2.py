tmp = int(input())
list_ = [(input(),int(input())) for _ in range(tmp)]
winnerName,winnerPoint="",0
for n,p in list_:
    if p>winnerPoint:winnerPoint,winnerName=p,n
print(winnerName)