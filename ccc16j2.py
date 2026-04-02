inp=[]
for i in range(4):
    inp.append(input())

imp=list(map(lambda x: x.split(), inp))

t=[]

for a,b,c,d in imp:
    t.append(int(a)+int(b)+int(c)+int(d))

sidewaysInp=list(map(list, zip(*imp)))

for a,b,c,d in sidewaysInp:
    t.append(int(a)+int(b)+int(c)+int(d))

if len(set(t))==1:
    print("magic")
else:
    print("not magic")