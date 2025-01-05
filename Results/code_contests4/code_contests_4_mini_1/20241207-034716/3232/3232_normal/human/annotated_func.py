#State of the program right berfore the function call: The input consists of multiple datasets where each dataset begins with a non-negative integer n (0 <= n <= 10,000) followed by n lines each containing two time strings in the format "hh:mm:ss" representing departure and arrival times at Osaki Station. The input terminates with a line containing n = 0, which is not part of the datasets. Each time value follows the constraints: 0 ≤ hh < 24, 0 ≤ mm < 60, 0 ≤ ss < 60.
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
        
    #State of the program after the loop has been executed: `m` is 86400, `n` is 0, `dp` contains cumulative sums of events processed, and the maximum value of `dp` is the highest count of overlapping events based on the inputs provided during the iterations.
#Overall this is what the function does:The function processes multiple datasets containing non-negative integers followed by pairs of departure and arrival times in "hh:mm:ss" format. For each dataset, it calculates the maximum number of overlapping events at any point in time and prints this maximum. The input terminates when a dataset begins with the integer 0. The function does not handle any input errors or invalid time formats explicitly.

