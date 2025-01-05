#State of the program right berfore the function call: The input consists of multiple datasets, where each dataset begins with an integer n (1 <= n <= 10000) followed by n lines containing two timestamps (hh:mm:ss) representing the departure and arrival times of each train. Each timestamp is in the format hh:mm:ss with 0 ≤ hh < 24, 0 ≤ mm < 60, and 0 ≤ ss < 60. The dataset ends with n = 0, which is not included in the datasets.
def func():
    m = 24 * 60 * 60
    while True:
        n = int(raw_input())
        
        if n == 0:
            break
        
        dp = [0] * (m + 1)
        
        for _ in range(n):
            a, d = raw_input().split()
            a, b, c = map(int, a.split(':'))
            d, e, f = map(int, d.split(':'))
            dp[a * 3600 + b * 60 + c] += 1
            dp[d * 3600 + e * 60 + f] -= 1
        
        for i in range(m):
            dp[i + 1] += dp[i]
        
        print(max(dp))
        
    #State of the program after the loop has been executed: `m` is 86400, `n` is 0, `dp` is a list of size 86401 with all elements set to 0; the maximum value of `dp` is the highest count of overlapping events recorded during all iterations, with `dp` reflecting cumulative totals over the day.
#Overall this is what the function does:The function accepts multiple datasets of train departure and arrival timestamps, counting the maximum number of overlapping trains at any given time during the day. It processes each dataset until it encounters a dataset starting with `n = 0`, which indicates the end of input. For each dataset, it calculates and prints the maximum number of overlapping trains based on the provided timestamps. The function handles timestamps correctly and ensures that the maximum overlap is calculated accurately, but it does not return any values; it only prints the results.

