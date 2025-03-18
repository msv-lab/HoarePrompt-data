#State of the program right berfore the function call: n and t are positive integers such that 1 <= n <= 100 and 1 <= t <= 10^5. Each bus route has a time si for the first bus arrival and an interval di between two buses, where 1 <= si, di <= 10^5.**
def func():
    n, t = map(int, input().split())
    buses = []
    for _ in range(n):
        s, d = map(int, input().split())
        
        buses.append((s, d))
        
    #State of the program after the  for loop has been executed: `n` is at least 1, `t` is a positive integer such that 1 <= t <= 10^5, `buses` contains `n` tuples `(s, d)` that were appended, `_` is `n-1`, `s` and `d` are integers obtained from the input split
    min_time = float('inf')
    ans = -1
    for (i, (s, d)) in enumerate(buses):
        time = (t - s) % d
        
        if time < min_time:
            min_time = time
            ans = i + 1
        
    #State of the program after the  for loop has been executed: After the loop finishes executing, the variables will have the following values: `n` remains at least 1, `t` remains a positive integer such that 1 <= t <= 10^5, `buses` contains all `n` tuples, `_` remains `n-1`, `s` and `d` are integers obtained from the last tuple in the `buses` list, `min_time` contains the minimum value of `(t - s) % d` across all tuples in `buses`, `ans` is the index of the tuple in `buses` that resulted in the minimum `time`. If there are multiple tuples that result in the same minimum `time`, `ans` will hold the index of the first occurrence.
    print(ans)
#Overall this is what the function does:The function `func` reads input data regarding bus routes, calculates the next bus arrival time for each route based on a given time, and prints the index of the bus route with the minimum waiting time for the next bus arrival. The function takes into account the constraints on input values and handles multiple buses potentially having the same minimum waiting time.

