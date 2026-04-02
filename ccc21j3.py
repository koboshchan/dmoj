encodedCodes,p=[],""
while True:
    tmp = input()
    if tmp == "99999":break
    encodedCodes.append(tmp)
for encodedCode in encodedCodes:
    der,num=encodedCode[:2],encodedCode[2:]
    if der=="00":print(p+" "+num)
    elif sum(list(map(int,der)))%2==0:print("right "+num);p="right"
    elif sum(list(map(int,der)))%2==1:print("left "+num);p="left"