def func_1():
    string = raw_input()
    (N, C) = string.split(' ')
    N = int(N)
    C = int(C)
    x = raw_input().split(' ')
    tem = 0
    for i in range(N):
        x[i] = int(x[i])
    for i in range(len(x) - 1):
        if tem <= x[i] - x[i + 1] and x[i] - x[i + 1] - C > 0:
            tem = x[i] - x[i + 1]
    if tem > 0:
        tem = tem - C
    return tem