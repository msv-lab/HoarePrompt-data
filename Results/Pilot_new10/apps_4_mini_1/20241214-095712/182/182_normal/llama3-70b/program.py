x = int(input())
x = x % 360
if x == 0:
    print(0)
else:
    print((x + 90 - 1) // 90 % 4)
