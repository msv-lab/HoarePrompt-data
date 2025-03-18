#State of the program right berfore the function call: n is an integer such that 1 <= n <= 100, t is an integer such that 1 <= t <= 100000, and for each bus route i (1 <= i <= n), s_i and d_i are integers such that 1 <= s_i, d_i <= 100000.
def func():
    n, t = map(int, input().split())
    buses = []
    for _ in range(n):
        s, d = map(int, input().split())
        
        buses.append((s, d))
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 <= `n` <= 100, `t` is an integer such that 1 <= `t` <= 100000, `buses` contains `n` tuples of the form `(s, d)` where each `s` and `d` are integers obtained from user input.
    min_time = float('inf')
    ans = -1
    for (i, (s, d)) in enumerate(buses):
        time = (t - s) % d
        
        if time < min_time:
            min_time = time
            ans = i + 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 <= `n` <= 100, `min_time` is the minimum time from all buses calculated as `(t - s) % d` for each bus where `time` was less than the previous `min_time`, `ans` is the index (1-based) of the bus corresponding to the minimum time, and `buses` contains `n` tuples of the form `(s, d)`. If the loop does not execute, `min_time` remains positive infinity and `ans` remains -1.
    print(ans)
#Overall this is what the function does:The function accepts input for the number of bus routes `n` and a time `t`, then reads `n` pairs of integers representing the start time `s` and the duration `d` for each bus route. It calculates the minimum time until the next bus departure from time `t` for all bus routes and returns the 1-based index of the bus with the minimum time. If no buses are available (though the code guarantees at least one bus route), it would return -1. The function does not return any value but prints the bus index.

