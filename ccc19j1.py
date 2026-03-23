in1 = [int(input()) for _ in range(6)]

a = sum([in1[0] * 3, in1[1] * 2, in1[2] * 1])
b = sum([in1[3] * 3, in1[4] * 2, in1[5] * 1])

print("T" if a==b else ("A" if a>b else "B"))