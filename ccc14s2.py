# 250 / 500 IR | PY3

tmp___=int(input())
grp1=input().split()
grp2=input().split()
if tmp___%2==1:print("bad",end="");exit()
grps=[]
for i in range(tmp___):
    grps.append((grp1[i], grp2[i]))
for a,b in grps:
    if a==b:print("bad",end="");exit()
print("good")