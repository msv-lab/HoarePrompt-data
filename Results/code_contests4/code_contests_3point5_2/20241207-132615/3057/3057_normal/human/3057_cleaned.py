steps = 0
index = 0
(steps, index) = raw_input().split()
steps = int(steps)
index = int(index)
left = 1
right = int(math.pow(2, steps) - 1)
if index % 2 == 1:
    print(1)
else:
    while (right + left) / 2 != index:
        steps -= 1
        if index < (right + left) / 2:
            right = (right + left) / 2 - 1
        elif index > (right + left) / 2:
            left = right = (right + left) / 2 + 1
    print(steps)