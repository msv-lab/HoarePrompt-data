def func_1():
    c = [0] * 5
    for i in range(1, 5):
        c[i] = int(input())
    s = input()
    res = 0
    for ch in s:
        res += c[int(ch)]
    print(res)
    return