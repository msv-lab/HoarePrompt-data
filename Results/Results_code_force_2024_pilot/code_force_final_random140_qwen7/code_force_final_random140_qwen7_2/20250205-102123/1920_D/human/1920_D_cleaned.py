def func_1(x):
    x = int(x)
    if x in b:
        return b[x]
    for i in a:
        x = (x - 1) % i + 1
        if x in b:
            return b[x]
for _ in range(int(input())):
    a = [0]
    b = {}
    (c, d) = map(int, input().split())
    for i in range(c):
        (d, e) = map(int, input().split())
        if a[-1] > 10 ** 19:
            continue
        if d & 1:
            a[-1] += 1
            b[a[-1]] = e
        else:
            a.append(a[-1] * (e + 1))
    a = a[::-1]
    print(str(list(map(resolve_query, input().split())))[1:-1].replace(',', ''))