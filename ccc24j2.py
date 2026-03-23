size=int(input())
while True:
    tmp=int(input())
    if tmp<size:
        size+=tmp
    else:
        print(size)
        break