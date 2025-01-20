n = int(input())
x = int(input())
position = x
for i in range(n, 0, -1):
    if i % 2 == 1:
        if position == 0:
            position = 1
        elif position == 1:
            position = 0
    elif position == 1:
        position = 2
    elif position == 2:
        position = 1
print(position)