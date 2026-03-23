K=input
J=int
I=range
B=list
A=''
D,L,E=B(I(1,J(K())+1)),J(K()),[]
for C in I(L):E.append(J(K()))
for C in E:
	F=[]
	for G in I(1,len(D)+1):
		if G%C==0:F.append(G-1)
	H=B(A+A+A+A+A+A+A+A+A+A+A+A)+B(A+A+A+A+A+A+A+A+A+A+A+A)+B(A+A+A+A+A+A+A+A+A+A+A+A)+B(A+A+A+A+A+A+A+A+A+A+A+A)+B(A+A+A+A+A+A+A+A+A+A+A+A)+B(A+A+A+A+A+A+A+A+A+A+A+A)+B(A+A+A+A+A+A+A+A+A+A+A+A)+B(A+A+A+A+A+A+A+A+A+A+A+A)+B(A+A+A+A+A+A+A+A+A+A+A+A)
	for C in F:H.append(D[C])
	for C in H:D.remove(C)
print('\n'.join(B(map(str,D))))