import sys

inp = list(sys.stdin.readline().strip())

dat = [["1", "2"], ["3", "4"]]

for i in inp:
    if i == "H":
        dat = dat[::-1]
    if i == "V":
        dat[0] = dat[0][::-1]
        dat[1] = dat[1][::-1]

print(" ".join(dat[0]))
print(" ".join(dat[1]))
