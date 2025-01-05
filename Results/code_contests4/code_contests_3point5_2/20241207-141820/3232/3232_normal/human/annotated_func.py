#State of the program right berfore the function call: n is a non-negative integer indicating the number of trains in the timetable. Each train's departure and arrival times are given in the format hh:mm:ss hh:mm:ss on separate lines, where hh is the hour, mm is the minute, and ss is the second. The departure time is always before the arrival time.**
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
        
    #State of the program after the loop has been executed: `n` is 0, `m` is greater than 0, `dp` is a list where each element is the sum of all elements before it, `a, b, c, d, e, f` have final values assigned after the final iteration of the loop, `i` is equal to `m-1`, maximum value in `dp` is printed
#Overall this is what the function does:The function `func` reads the number of trains `n` as a non-negative integer. Each train's departure and arrival times are provided in the format hh:mm:ss hh:mm:ss on separate lines, where hh is the hour, mm is the minute, and ss is the second. The departure time is always before the arrival time. The function then calculates the maximum number of trains present at any given time and prints that value.

