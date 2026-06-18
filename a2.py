r="Ready"
mp="Mirrored pair"
op="Ordinary pair"

print(r)
while True:
    inp = input()
    if inp == "  ":break
    if inp in ["qp","pq","db","bd"] : print(mp)
    else: print(op)