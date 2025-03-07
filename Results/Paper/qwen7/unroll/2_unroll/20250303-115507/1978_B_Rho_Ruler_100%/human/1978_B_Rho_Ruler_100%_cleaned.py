def func_1(k, n, a, b):
    return k * b - k * (k - 1) // 2 + (n - k) * a

def func_2(n, a, b):
    (low, high) = (0, min(n, b))
    max_profit = 0
    while low <= high:
        mid = (low + high) // 2
        profit_mid = func_1(mid, n, a, b)
        profit_next = func_1(mid + 1, n, a, b)
        max_profit = max(max_profit, profit_mid)
        if profit_next > profit_mid:
            low = mid + 1
        else:
            high = mid - 1
    return max_profit
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        (n, a, b) = map(int, input().split())
        print(func_2(n, a, b))