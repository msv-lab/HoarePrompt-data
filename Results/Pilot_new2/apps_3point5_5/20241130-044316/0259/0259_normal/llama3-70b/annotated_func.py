#State of the program right berfore the function call: n and t are positive integers such that 1 <= n <= 100 and 1 <= t <= 10^5. Each bus route has a first bus arrival time si and time interval di, where 1 <= si, di <= 10^5.**
def func():
    n, t = map(int, input().split())
    buses = []
    for _ in range(n):
        s, d = map(int, input().split())
        
        buses.append((s, d))
        
    #State of the program after the  for loop has been executed: Output State: n is a positive integer between 1 and 100, t is a positive integer, buses contains n tuples (s, d) where s and d are integers obtained from splitting the input.
    min_time = float('inf')
    ans = -1
    for (i, (s, d)) in enumerate(buses):
        time = (t - s) % d
        
        if time < min_time:
            min_time = time
            ans = i + 1
        
    #State of the program after the  for loop has been executed: n is a positive integer between 1 and 100, t is a positive integer, buses contains n tuples, min_time is the minimum time value calculated during the loop execution, ans is the index of the tuple that resulted in the minimum time value, i is equal to n-1 after the loop finishes, s and d correspond to the values of the last tuple in the list, and time is the result of the calculation (t - s) % d.
    print(ans)
#Overall this is what the function does:The function reads two positive integers n and t from input. It then reads n pairs of integers representing bus arrival times and intervals. The function calculates the minimum time value based on the input parameters and prints the index of the tuple that resulted in the minimum time value.

