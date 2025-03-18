t = int(input())

def func_1(n):
    if n == 0:
        return -1
    position = 0
    while n != 0:
        n >>= 1
        position += 1
    return position - 1
for _ in range(t):
    (n, k) = [int(x) for x in input().split()]
    arr = []
    if n > 1:
        counter = func_1(k)
        arr.append(2 ** counter - 1)
        arr.append(k - arr[-1])
        for _ in range(n - 2):
            arr.append(0)
        print(*arr)
    else:
        print(k)