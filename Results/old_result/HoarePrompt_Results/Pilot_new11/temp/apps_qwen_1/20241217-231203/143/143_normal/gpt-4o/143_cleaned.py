def func_1(n, L, costs):
    max_cost = 10 ** 18
    dp = [max_cost] * 31
    c = costs + [max_cost] * (31 - len(costs))
    for i in range(n):
        dp[i] = min(dp[i], c[i])
    for i in range(1, 31):
        dp[i] = min(dp[i], dp[i - 1] * 2)
    answer = max_cost
    current_cost = 0
    for i in range(30, -1, -1):
        if L >= 1 << i:
            current_cost += dp[i]
            L -= 1 << i
        answer = min(answer, current_cost + (L > 0) * dp[i])
    return answer
if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    L = int(data[1])
    costs = list(map(int, data[2:2 + n]))
    print(func_1(n, L, costs))