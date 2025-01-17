def func_1():
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    a = list(map(int, data[1:]))
    if any((ai > 2 * (n - 1) for ai in a)):
        print('NO')
        return
    houses = []
    for i in range(n):
        x = i + 1
        y = i % n + 1
        houses.append((x, y))
    visits = [-1] * n
    for i in range(n):
        for j in range(n):
            if i != j:
                dist = abs(houses[i][0] - houses[j][0]) + abs(houses[i][1] - houses[j][1])
                if dist == a[i]:
                    visits[i] = j + 1
                    break
    if -1 in visits:
        print('NO')
    else:
        print('YES')
        for (x, y) in houses:
            print(x, y)
        print(' '.join(map(str, visits)))