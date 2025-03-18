MOD = 998244353

def func_1(n, k):
    return len(set(str(n))) <= k

def func_2(l, r, k):
    total_sum = 0
    for num in range(l, r + 1):
        if func_1(num, k):
            total_sum = (total_sum + num) % MOD
    return total_sum
(l, r, k) = map(int, input().split())
print(func_2(l, r, k))