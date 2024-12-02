#State of the program right berfore the function call: n and t are positive integers such that 1 <= n <= 100 and 1 <= t <= 10^5. Each bus route has a positive arrival time and interval between buses such that 1 <= s_i, d_i <= 10^5 for 1 <= i <= n.**
def func():
    n, t = map(int, input().split())
    buses = []
    for _ in range(n):
        s, d = map(int, input().split())
        
        buses.append((s, d))
        
    #State of the program after the  for loop has been executed: `n` is a positive integer between 1 and 100, `t` is a positive integer between 1 and 10^5, `buses` is a list that contains `n` elements with the tuples `(s, d)` where each `s` and `d` are positive integers between 1 and 10^5 extracted from the input and appended to the existing list of buses
    min_time = float('inf')
    ans = -1
    for (i, (s, d)) in enumerate(buses):
        time = (t - s) % d
        
        if time < min_time:
            min_time = time
            ans = i + 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer between 1 and 100, `t` is a positive integer between 1 and 10^5, `buses` is a list that contains `n` elements with the tuples `(s, d)`, `min_time` is the minimum time calculated from the loop, `ans` is the index of the tuple in `buses` with the minimum time
    print(ans)
#Overall this is what the function does:The function `func` reads two positive integers `n` and `t`, then reads `n` pairs of positive integers representing bus arrival times and intervals. It calculates the minimum time difference between `t` and bus arrival times, and prints the index of the bus with the minimum time difference. The function does not have a specific return value.

