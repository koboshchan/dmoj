happiness = lambda s,m,l:  1 * s + 2 * m + 3 * l
s, m, l = [int(input()) for _ in range(3)]
print("happy" if happiness(s, m, l) >= 10 else "sad")