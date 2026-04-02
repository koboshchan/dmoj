V = lambda r,h: (3.14159 * r ** 2 * h) / 3

r = int(input())
h = int(input())

# round to 2 decimal places
print(round(V(r,h), 2))