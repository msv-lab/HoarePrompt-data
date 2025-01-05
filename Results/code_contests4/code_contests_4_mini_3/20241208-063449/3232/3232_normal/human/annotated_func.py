#State of the program right berfore the function call: The input consists of multiple datasets, where each dataset starts with an integer n (1 <= n <= 10,000) representing the number of trains, followed by n lines of departure and arrival times in the format "hh:mm:ss hh:mm:ss", with 0 ≤ hh < 24, 0 ≤ mm < 60, and 0 ≤ ss < 60. The last dataset is indicated by n = 0, which should not be processed.
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
        
    #State of the program after the loop has been executed: `m` is 86400, `dp` contains cumulative sums of occurrences up to each index, `dp[0]` remains unchanged, and the maximum value in `dp` is the highest occurrence recorded during the iterations. The loop continues to accept input until `n` is 0, at which point it exits.
#Overall this is what the function does:The function processes multiple datasets of train departure and arrival times, calculating the maximum number of trains present at the station at any given time. Each dataset starts with an integer `n` indicating the number of trains, followed by `n` lines of arrival and departure times in the format "hh:mm:ss hh:mm:ss". The processing stops when `n` is 0, which indicates the end of input. The function returns the maximum count of overlapping trains for each dataset.

