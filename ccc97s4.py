tmp = int(input())
listin=[]
def tmp233(x:str):return x.strip()
for i in range(tmp):
    tmp2=[]
    while True:
        tmp3=input()
        if tmp3 == "":break
        tmp2.append(tmp3)
    listin.append('/\\/\\/\\'.join(tmp2))
for i in listin:
    out,words,now_count,ttmmpp=[],{},1,[]
    # words: {"word:str":"num:str"}
    for x_x in i.split():
        if '/\\/\\/\\' in x_x:
            tmp1024=x_x.split('/\\/\\/\\')
            for y_y_ in range(len(tmp1024)):
                y_y = tmp1024[y_y_]
                ttmmpp.append(y_y)
                if not(y_y_ == len(tmp1024)-1):ttmmpp.append('/\\/\\/\\')
        else:ttmmpp.append(x_x)
    for word in ttmmpp:
        if word == '/\\/\\/\\':out.append('/\\/\\/\\');continue
        if word not in words.keys():
            words[str(word)] = str(now_count)
            out.append(word)
            now_count+=1
        else:
            out.append( words[word] )
    print('\n'.join(map(tmp233,' '.join(out).split('/\\/\\/\\'))))
    print('')