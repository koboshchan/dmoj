"""
R>G
G>B
B>R
"""

def win(first,second):
    if first==second: return None
    if (first == "R" and second == "G"): return True
    if (first == "G" and second == "R"): return False
    if (first == "G" and second == "B"): return True
    if (first == "B" and second == "G"): return False
    if (first == "B" and second == "R"): return True
    if (first == "R" and second == "B"): return False
    return object

from collections import deque

N=deque(list(input()))
M=deque(list(input()))

NScore=0
MScore=0

while (len(N)!=0 and len(M)!=0):
    if win(N[0],M[0]) == None:
        NScore+=1
        MScore+=1
        N.popleft()
        M.popleft()
    elif win(N[0],M[0]) == True:
        NScore+=1
        M.popleft()
    elif win(N[0],M[0]) == False:
        MScore+=1
        N.popleft()

if len(N) == 0:
    MScore += len(M)
elif len(M) == 0:
    NScore += len(N)

print(NScore)
print(MScore)