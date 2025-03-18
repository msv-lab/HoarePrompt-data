#State of the program right berfore the function call: n and t are integers such that 1 <= n <= 100 and 1 <= t <= 10^5. Each bus route has an arrival time and interval between buses represented by s_i and d_i, both integers such that 1 <= s_i, d_i <= 10^5.**
def func():
    n, t = map(int, input().split())
    buses = []
    for _ in range(n):
        s, d = map(int, input().split())
        
        buses.append((s, d))
        
    #State of the program after the  for loop has been executed: `n` is at least 1, `buses` list contains bus routes with arrival time `s_i` and interval `d_i` for each route, `s` and `d` are assigned the integer values obtained from splitting the input for the last iteration of the loop.
    min_time = float('inf')
    ans = -1
    for (i, (s, d)) in enumerate(buses):
        time = (t - s) % d
        
        if time < min_time:
            min_time = time
            ans = i + 1
        
    #State of the program after the  for loop has been executed: Output State: `time` will be the result of the last (t - s) % d calculation, `min_time` will be the minimum value of `time` throughout all iterations, `ans` will be the index of the bus route with the smallest `time` value, `n` is at least 1, `buses` list contains bus routes with arrival time `s_i` and interval `d_i` for each route.
    print(ans)
#Overall this is what the function does:The function `func` reads input for the number of bus routes and a specific time, then reads the arrival times and intervals for each bus route. It calculates the time until the next bus arrives based on the input time and bus schedules, and prints the index of the bus route with the shortest waiting time.

