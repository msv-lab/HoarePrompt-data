#State of the program right berfore the function call: n is an integer between 1 and 100, t is a positive integer between 1 and 100000, and for each bus route i (1 <= i <= n), s_i and d_i are positive integers between 1 and 100000.
def func():
    n, t = map(int, input().split())
    buses = []
    for _ in range(n):
        s, d = map(int, input().split())
        
        buses.append((s, d))
        
    #State of the program after the  for loop has been executed: `n` is between 1 and 100, `t` is a positive integer between 1 and 100000, `s_i` is a positive integer between 1 and 100000, `d_i` is a positive integer between 1 and 100000, `buses` is a list containing `n` tuples of the form `(s, d)`, where each `s` is a positive integer (user input), and each `d` is a positive integer (user input).
    min_time = float('inf')
    ans = -1
    for (i, (s, d)) in enumerate(buses):
        time = (t - s) % d
        
        if time < min_time:
            min_time = time
            ans = i + 1
        
    #State of the program after the  for loop has been executed: `n` is between 1 and 100, `buses` is a list containing `n` tuples of the form (s, d); `min_time` is the minimum time observed across all buses; `ans` is the 1-based index of the bus that has the minimum time.
    print(ans)
#Overall this is what the function does:The function accepts two integers, `n` (between 1 and 100) and `t` (a positive integer between 1 and 100,000), and processes `n` bus routes, each characterized by two integers `s` (the start time) and `d` (the duration). It calculates the minimum time until the next bus departs based on the current time `t`, and returns the 1-based index of the bus route that has the minimum wait time. If no buses are available, it will still return the index of the first bus (1), as it assumes there is always at least one bus.

