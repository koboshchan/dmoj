inp = int(input())
for i in range(inp // 2):
    print(
        "*" * ((i * 2) + 1),
        " " * ((inp * 2) - ((i * 2) * 2) - 4),
        "*" * ((i * 2) + 1),
    )
print("*" * ((inp * 2)))


for i in range(inp // 2 - 1, -1, -1):
    print(
        "*" * ((i * 2) + 1),
        " " * ((inp * 2) - ((i * 2) * 2) -4),
        "*" * ((i * 2) + 1),
    )
