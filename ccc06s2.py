in1=input()
in2=input()
in3=input()

dic=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")

cypher = {}

for x,y in zip(in2,in1):
    if x in cypher.keys():
        continue
    cypher[x] = y

if len(cypher.keys()) == 26:
    for i in dic:
        if i not in cypher.keys():
            x = i
            break
    for i in dic:
        if i not in cypher.values():
            y = i
            break
    cypher[x] = y

for l in in3:
    print(cypher.get(l,"."),end="")
print()