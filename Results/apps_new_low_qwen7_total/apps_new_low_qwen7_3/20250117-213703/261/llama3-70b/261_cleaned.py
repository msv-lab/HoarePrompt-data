(m, k) = map(int, input().split())

def func_1(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def func_2(m, k):
    n = 1
    while True:
        count = sum((1 for i in range(n + 1, 2 * n + 1) if func_1(i) == k))
        if count == m:
            return n
        n += 1
print(func_2(m, k))