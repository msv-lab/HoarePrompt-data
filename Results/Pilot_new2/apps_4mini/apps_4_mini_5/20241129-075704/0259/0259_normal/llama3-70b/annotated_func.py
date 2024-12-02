#State of the program right berfore the function call: n is a positive integer (1 <= n <= 100), t is a positive integer (1 <= t <= 100000), and for each bus route i, s_i and d_i are positive integers (1 <= s_i, d_i <= 100000).
def func():
    n, t = map(int, input().split())
    buses = []
    for _ in range(n):
        s, d = map(int, input().split())
        
        buses.append((s, d))
        
    #State of the program after the  for loop has been executed: `n` is an integer within the range 1 to 100, `t` is an integer within the range 1 to 100000, `buses` is a list containing `n` tuples of the form (s, d) where each tuple corresponds to user input values for `s` and `d`.
    min_time = float('inf')
    ans = -1
    for (i, (s, d)) in enumerate(buses):
        time = (t - s) % d
        
        if time < min_time:
            min_time = time
            ans = i + 1
        
    #State of the program after the  for loop has been executed: `n` is an integer within the range 1 to 100; `t` is an integer within the range 1 to 100000; `buses` is a list containing `n` tuples of the form (s, d); `min_time` is the minimum time calculated from all buses, `ans` is the index (1-based) of the bus that results in the minimum time, `i` is `n - 1`, `s` is the first element of the last tuple in `buses`, `d` is the second element of the last tuple in `buses`. If the loop does not execute (if `n` is 0), then `min_time` remains as positive infinity, and `ans` remains -1.
    print(ans)
#Overall this is what the function does:The function accepts two positive integers `n` (number of bus routes) and `t` (current time), collects `n` tuples of bus route parameters `(s_i, d_i)`, calculates the minimum wait time for the buses, and prints the 1-based index of the bus that results in the minimum wait time. If there are no bus routes, it would print -1.

