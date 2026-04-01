_=input()

yesterday = input()
today = input()

occupied = 0

for y,t in zip(yesterday,today):
    if y == "C" and t == "C":
        occupied += 1
print(occupied)