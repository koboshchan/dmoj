inp="""AABbCcddEe
AaBBccddee
5
ABCdE
aBcdE
ABcdE
ABCde
ABcDe"""


parent1 = input()
parent2 = input()
N = int(input())
babys = []
for i in range(N):
    babys.append(input())

dominant = []

for i in range(5):
    parent1_allele = parent1[i*2]
    parent2_allele = parent2[i*2]
    if parent1_allele.isupper() and parent2_allele.isupper():
        dominant.append(parent1_allele)
    elif parent1_allele.islower() and parent2_allele.islower():
        dominant.append(parent1_allele)
    else:
        dominant.append(parent1_allele.upper())
    parent1_allele = parent1[i*2+1]
    parent2_allele = parent2[i*2+1]
    if parent1_allele.isupper() and parent2_allele.isupper():
        dominant.append(parent1_allele)
    elif parent1_allele.islower() and parent2_allele.islower():
        dominant.append(parent1_allele)
    else:
        dominant.append(parent1_allele.upper())
dominant = list(set(dominant))

for baby in babys:
    possible = True
    for letter in baby:
        if letter not in dominant:
            print("Not their baby!")
            possible = False
            break
    if possible:
        print("Possible baby.")