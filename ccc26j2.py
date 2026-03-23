first5 = [int(input()) for _ in range(5)]
d = int(input())
first5.remove(min(first5))
first5.remove(max(first5))
print(sum(first5)*d)