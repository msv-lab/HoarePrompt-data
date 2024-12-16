def func_1(n, a, b):
    (low, high) = (1, min(a, b) + 1)

    def can_distribute(x):
        return a // x + b // x >= n
    while low < high:
        mid = (low + high) // 2
        if can_distribute(mid):
            low = mid + 1
        else:
            high = mid
    return low - 1
(n, a, b) = map(int, input().split())
print(func_1(n, a, b))