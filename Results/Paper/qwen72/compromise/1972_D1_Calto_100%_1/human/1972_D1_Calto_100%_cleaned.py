def func_1(a, b):
    while b:
        (a, b) = (b, a % b)
    return a

def func_2(n, m):
    cnt = -1
    for i in range(1, m + 1):
        x = n - (i * i - i)
        y = i * i
        cnt = cnt + math.ceil(x / y) + (x % y == 0)
    return cnt
t = int(input())
for _ in range(t):
    (n, m) = map(int, input().split())
    result = func_2(n, m)
    print(result)