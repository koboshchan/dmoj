t = int(input())  # height of tines
s = int(input())  # spacing between tines
h = int(input())  # length of handle

# Draw the tines
for i in range(t):
    print("*" + " " * s + "*" + " " * s + "*")

# Draw the horizontal bar
print("*" * (3 + 2 * s))

# Draw the handle
for i in range(h):
    print(" " * (1 + s) + "*")
