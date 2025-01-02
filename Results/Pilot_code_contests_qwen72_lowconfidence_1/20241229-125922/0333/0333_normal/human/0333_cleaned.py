def func_1(n, p):
    l = [1] * (n + 1)
    for i in range(n):
        l[i + 1] = l[i] * (n - i) * pow(i + 1, p - 2, p) % p
    return l

def func_2(n, p):
    l = []
    if n % 4 == 0:
        for e in func_1(n // 2 - 1, p):
            l += [e, -e]
        return l
    if n % 4 == 1:
        for e in func_1(n // 2, p):
            l += [e, 0]
        l.pop(-1)
        return l
    if n % 4 == 2:
        for e in func_1(n // 2 - 1, p):
            l += [e, e]
        return l
    pre_l = []
    for e in func_1(n // 2 - 1, p):
        pre_l += [e, e]
    l.append(pre_l[0])
    for i in range(1, n - 1):
        l.append(pre_l[i] + pre_l[i - 1] * (-1) ** (i + 1))
    l.append(pre_l[n - 2] * (-1) ** n)
    return l
if __name__ == '__main__':
    n = int(raw_input())
    s = func_2(n, 10 ** 9 + 7)
    t = 0
    l = map(lambda x: int(x), raw_input().split(' '))
    for i in range(n):
        t += s[i] * l[i]
        t %= 10 ** 9 + 7
    print(str(t))