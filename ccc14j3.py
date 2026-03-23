an,da,ins,in1=100,100,[],int(input())
for i in range(in1):ins.append(list(map(int,input().split(' '))))
for i in ins:
    if i[0]==i[1]:continue
    elif i[0]<i[1]:an-=i[1]
    elif i[1]<i[0]:da-=i[0]
print(an);print(da)