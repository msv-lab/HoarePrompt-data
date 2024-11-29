#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 100, t is a positive integer such that 1 <= t <= 10^5, and for each bus route i (1 <= i <= n), s_i and d_i are positive integers such that 1 <= s_i, d_i <= 10^5.
def func():
    n, t = map(int, input().split())
    buses = []
    for _ in range(n):
        s, d = map(int, input().split())
        
        buses.append((s, d))
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 <= n <= 100, `t` is a positive integer such that 1 <= t <= 10^5, `buses` is a list containing `n` tuples `(s, d)` where each tuple is an integer pair from input.
    min_time = float('inf')
    ans = -1
    for (i, (s, d)) in enumerate(buses):
        time = (t - s) % d
        
        if time < min_time:
            min_time = time
            ans = i + 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer between 1 and 100, `buses` is a list containing `n` tuples, `min_time` is the minimum time calculated from all buses based on the formula `(t - s) % d`, `ans` is the 1-based index of the bus that resulted in `min_time`. If no valid time was found, `min_time` remains float('inf') and `ans` remains -1.
    print(ans)
#Overall this is what the function does:The function accepts input values for the number of bus routes `n` and the current time `t`, along with `n` pairs of integers representing the start time `s` and the duration `d` of each bus route. It calculates the minimum wait time for the next bus based on the formula `(t - s) % d`, and returns the 1-based index of the bus that has the shortest wait time. If no valid bus is found (which is practically not possible with the given constraints), it will return -1. The function does not return any value directly; it only prints the index of the bus.

