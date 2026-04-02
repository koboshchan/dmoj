times=int(input())
ipts,time,friends=[input() for _ in range(times)],0,{}
for ipt in ipts:
    func,name = ipt.split()
    if func=="W":time+=int(name)-1;continue
    if not (name in friends.keys()):friends[name]=[0,time,0]
    if func=="S":friends[name][0]-=1;friends[name][2]+=(time-friends[name][1])
    elif func=="R":friends[name][0]+=1;friends[name][1]=time
    time+=1
smallToBig = list(map(int,friends.keys()))
smallToBig.sort()
for k in smallToBig:
    k=str(k)
    v=friends[k]
    _1,_2,timeToWait = v
    if _1 != 0:print(k+" -1");continue
    print(k+" "+str(timeToWait))