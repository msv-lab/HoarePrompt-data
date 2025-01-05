#State of the program right berfore the function call: n is a non-negative integer indicating the number of trains included in the timetable. The departure and arrival times of each train are given in the format hh: mm: ss, where hh is the hour, mm is the minute, and ss is the second. The departure time is always before the arrival time.**
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
        
    #State of the program after the loop has been executed: The maximum value in the `dp` list is the sum of all elements in the list. `n` is 0, `m` is 86,400, and all other variables retain their assigned values based on the input.
#Overall this is what the function does:The function processes the timetable information of n trains, where the departure and arrival times are provided in the format hh:mm:ss. It populates a list `dp` with the count of trains at each second of the day based on the input timetable information. After processing all trains, it calculates the maximum number of trains present at any given second and prints that value. The function repeats this process until n is input as 0. Edge cases and missing functionality: The function assumes valid input format for time values and does not handle cases where the input format is incorrect. Additionally, it does not consider overlapping train schedules.

