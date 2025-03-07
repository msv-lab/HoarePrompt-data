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
    for i in range(max(big), min(less)):
        if i not in no:
            num = i
            break
    print(num)