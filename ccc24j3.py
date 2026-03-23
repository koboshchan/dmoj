tmp=int(input())
pars=[]
for _ in range(tmp):
    pars.append(int(input()))
pars.sort()
pars.reverse()
pars2=list(set(pars))
pars2.sort()
pars2.reverse()
print(pars2[2],pars.count(pars2[2]))
