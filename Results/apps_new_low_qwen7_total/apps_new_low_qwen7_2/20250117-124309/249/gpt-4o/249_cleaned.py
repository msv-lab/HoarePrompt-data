MOD = 10 ** 9 + 7

def func_1(a, b, k, t):
    max_diff = 2 * k * t
    dp_prev = [0] * (2 * max_diff + 1)
    dp_curr = [0] * (2 * max_diff + 1)
    dp_prev[max_diff + (a - b)] = 1
    for _ in range(t):
        prefix_sum = [0] * (2 * max_diff + 3)
        for i in range(2 * max_diff + 1):
            prefix_sum[i + 1] = (prefix_sum[i] + dp_prev[i]) % MOD
        for i in range(2 * max_diff + 1):
            left = max(0, i - 2 * k)
            right = min(2 * max_diff, i + 2 * k) + 1
            dp_curr[i] = (prefix_sum[right] - prefix_sum[left]) % MOD
        (dp_prev, dp_curr) = (dp_curr, dp_prev)
    result = 0
    for i in range(max_diff + 1, 2 * max_diff + 1):
        result = (result + dp_prev[i]) % MOD
    print(result)
(a, b, k, t) = map(int, input().split())
func_1(a, b, k, t)