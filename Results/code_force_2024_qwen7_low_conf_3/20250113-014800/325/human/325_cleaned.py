def func_1():
    import sys
    input = sys.stdin.read
    data = input().split()
    index = 0
    num_cases = int(data[index])
    index += 1
    results = []
    for _ in range(num_cases):
        n = int(data[index])
        index += 1
        s = data[index]
        index += 1
        dp = [0] * (n + 1)
        result = 0
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                dp[i] = n - i + dp[i + 1]
            else:
                dp[i] = dp[i + 1]
        result = sum(dp[:n])
        results.append(result)
    for res in results:
        print(res)
if __name__ == '__main__':
    func_1()