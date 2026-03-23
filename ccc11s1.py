n = int(input())
dat = [input().strip() for _ in range(n)]
fin = ""

for i in dat:
    fin += i

fin = fin.lower()
count_s = fin.count("s")
count_t = fin.count("t")

if count_t > count_s:
    print("English")
else:
    print("French")
