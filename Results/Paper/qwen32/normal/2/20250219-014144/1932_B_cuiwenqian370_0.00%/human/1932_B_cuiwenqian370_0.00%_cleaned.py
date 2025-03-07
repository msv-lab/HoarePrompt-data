def func_1(path):
    n = len(path)
    if n == 0:
        return 0
    dp = [0] * n
    if path[0] == '@':
        dp[0] = 1
    elif path[0] == '*':
        dp[0] = -float('inf')
    if n > 1:
        if path[1] == '*':
            dp[1] = -float('inf')
        else:
            dp[1] = dp[0] + (1 if path[1] == '@' else 0)
    for i in range(2, n):
        if path[i] == '*':
            dp[i] = -float('inf')
        else:
            dp[i] = max(dp[i - 1], dp[i - 2]) + (1 if path[i] == '@' else 0)
    return max((x for x in dp if x > -float('inf')))

def func_2():
    import sys
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        path = data[index]
        index += 1
        results.append(func_1(path))
    for result in results:
        print(result)