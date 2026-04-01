dat = [int(input()) for _ in range(4)]

if  (dat[0] == 8 or dat[0] == 9) and \
    (dat[3] == 8 or dat[3] == 9) and \
    (dat[1] == dat[2]):
    print("ignore")
else:
    print("answer")