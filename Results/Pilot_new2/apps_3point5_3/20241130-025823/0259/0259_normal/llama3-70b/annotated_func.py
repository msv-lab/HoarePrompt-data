#State of the program right berfore the function call: **Precondition**: **n and t are positive integers such that 1 <= n <= 100 and 1 <= t <= 10^5. Each bus route has a start time s_i and interval time d_i, where 1 <= s_i, d_i <= 10^5.**
def func():
    n, t = map(int, input().split())
    buses = []
    for _ in range(n):
        s, d = map(int, input().split())
        
        buses.append((s, d))
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `t` is a positive integer, `buses` contains `n` tuples `(s, d)`, `_` is incremented by `n`, `s` and `d` for each tuple are assigned the values of integers obtained from splitting the input by spaces.
    min_time = float('inf')
    ans = -1
    for (i, (s, d)) in enumerate(buses):
        time = (t - s) % d
        
        if time < min_time:
            min_time = time
            ans = i + 1
        
    #State of the program after the  for loop has been executed: n is greater than 0, t is a positive integer, buses contains at least n tuples, _ is incremented by n, s and d are assigned values from the tuple that results in the minimum time, min_time is the minimum time obtained from all tuples, ans is the index of the tuple that results in the minimum time plus 1, i is the index of the last tuple in the list, time is equal to the minimum time obtained from all tuples.
    print(ans)
#Overall this is what the function does:Functionality: The function `func` reads input consisting of positive integers `n` and `t`, followed by `n` tuples each representing bus routes with start times and intervals. It then calculates the minimum time difference for each bus route based on the current time `t` and prints the index of the bus route with the smallest time difference. The function does not return any value. Edge cases and missing functionalities: The function does not handle invalid inputs, negative integers, or edge cases where multiple bus routes have the same minimum time difference.

