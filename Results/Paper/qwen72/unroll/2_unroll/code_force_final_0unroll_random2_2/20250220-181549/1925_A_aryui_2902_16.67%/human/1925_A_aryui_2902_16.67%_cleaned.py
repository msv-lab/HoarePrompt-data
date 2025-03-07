def func_1():
    (n, k) = map(int, input().split())
    s = 'abcdefghijklmnopqrstuvw'
    return s[:k] * n
t = int(input())
for i in range(t):
    res = func_1()
    print(res)