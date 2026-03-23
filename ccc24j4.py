in1=input()
in2=input()
tmp=list(in1)
tmp=list(set(tmp))

quiet={0:"-"}
changed=[]

if len(in1)==len(in2):
    pass
else:
    for i in tmp:
        if len(in1.replace(i,""))==len(in2):
            matched=0
            tmp1=in1.replace(i,"")
            for k in range(len(tmp1)):
                if tmp1[k]==in2[k]:
                    matched+=1
            quiet[matched]=i

quiet=quiet[max(quiet.keys())]

in3=in1.replace(quiet,"")
for i in range(len(in3)):
    if in3[i]!=in2[i]:
        changed.append(in3[i])
        changed.append(in2[i])
        break
print(" ".join(changed))
print(quiet)