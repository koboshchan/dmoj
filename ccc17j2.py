def shifty_sum(n, k):
    total = 0
    for i in range(k + 1):
        total += n * (10 ** i)
    return total

print(shifty_sum(int(input()), int(input())))