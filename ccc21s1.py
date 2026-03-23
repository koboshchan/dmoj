import sys

n = int(sys.stdin.readline())
heights = list(map(int, sys.stdin.readline().split()))
widths = list(map(int, sys.stdin.readline().split()))

total_area = 0.0

for i in range(n):
    # (h1 + h2) * w / 2
    h_left = heights[i]
    h_right = heights[i+1]
    w = widths[i]
    
    piece_area = (h_left + h_right) * w / 2.0
    total_area += piece_area

print(str(total_area).replace(".0","") if str(total_area).endswith(".0") else str(total_area))
