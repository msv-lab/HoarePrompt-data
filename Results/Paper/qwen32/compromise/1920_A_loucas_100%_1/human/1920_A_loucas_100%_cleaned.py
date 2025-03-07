loop = int(input())
for iterable in range(loop):
    less = []
    big = []
    no = []
    num = 0
    innerLoop = int(input())
    for iterable2 in range(innerLoop):
        (x, a) = map(int, input().split())
        if x == 1:
            big.append(a)
        elif x == 2:
            less.append(a)
        else:
            no.append(a)
    num = min(less) - max(big) + 1
    if num < 1:
        print(0)
        continue
    for i in no:
        if i <= min(less) and i >= max(big):
            num -= 1
    print(num)