def func_1(a, b):
    while b:
        (a, b) = (b, a % b)
    return a

def func_2(n, m):
    cnt = 0
    for i in range(1, m):
        x = n - (i * i - i)
        y = i * i
        cnt = cnt + x // y + (i > 1)
    if cnt == 0:
        return 1
    return cnt
t = int(input())
for _ in range(t):
    (n, m) = map(int, input().split())
    result = func_2(n, m)
    print(result)