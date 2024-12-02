#State of the program right berfore the function call: n is an integer such that 1 <= n <= 100, t is a positive integer such that 1 <= t <= 100000, and for each bus route i (1 <= i <= n), s_i and d_i are integers such that 1 <= s_i, d_i <= 100000.
def func():
    n, t = map(int, input().split())
    buses = []
    for _ in range(n):
        s, d = map(int, input().split())
        
        buses.append((s, d))
        
    #State of the program after the  for loop has been executed: `n` is an integer such that `1 <= n <= 100`, `t` is a positive integer such that `1 <= t <= 100000`, `buses` now contains `n` tuples of the form `(s, d)` where each `s` and `d` are input integers provided during each iteration of the loop.
    min_time = float('inf')
    ans = -1
    for (i, (s, d)) in enumerate(buses):
        time = (t - s) % d
        
        if time < min_time:
            min_time = time
            ans = i + 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that `1 <= n <= 100`, `t` is a positive integer such that `1 <= t <= 100000`, `buses` contains `n` tuples of the form `(s, d)`, `min_time` is the minimum time calculated as `(t - s) % d` for the buses that provided the minimum value, `ans` is the index (1-based) of the bus that resulted in `min_time`, or remains -1 if no update occurred.
    print(ans)
#Overall this is what the function does:The function accepts an integer `n` (representing the number of bus routes) and a positive integer `t` (representing a time). It collects `n` pairs of integers `(s, d)` representing the start time and duration of each bus route. The function calculates the minimum wait time for the next bus based on the provided times and durations, and it prints the 1-based index of the bus with the shortest wait time. If no bus results in a wait time (which is impossible given the constraints), it would print `-1`. However, since inputs are constrained, the function will always return a valid bus index.

