#State of the program right berfore the function call: n is an integer representing the number of passengers (1 ≤ n ≤ 100), s is an integer representing the number of the top floor (1 ≤ s ≤ 1000), and each passenger is represented by a pair of integers (fi, ti) where fi is the floor number (1 ≤ fi ≤ s) and ti is the time of arrival in seconds (1 ≤ ti ≤ 1000).
def func():
    n, s = map(int, raw_input().split())
    p = []
    for i in range(n):
        fi, ti = map(int, raw_input().split())
        
        p.append((fi, ti))
        
    #State of the program after the  for loop has been executed: `n` is an integer (1 ≤ n ≤ 100), `i` is equal to `n`, `p` is a list containing `n` tuples of the form `(fi, ti)` where each tuple corresponds to the inputs provided during each iteration of the loop.
    p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
    p.append((0, 0))
    time_passed = 0
    for i in range(n + 1):
        time_passed += s - p[i][0]
        
        s = p[i][0]
        
        if time_passed < p[i][1]:
            time_passed += p[i][1] - time_passed
        
    #State of the program after the  for loop has been executed: `n` is an integer (1 ≤ n ≤ 100), `i` is `n + 1`, `s` is `p[n][0]`, `time_passed` is the cumulative time calculated through all iterations.
    print(time_passed)
#Overall this is what the function does:The function accepts an integer `n`, representing the number of passengers, and an integer `s`, representing the number of the top floor. It reads the floor numbers and arrival times of each passenger, calculates the total time taken to reach each passenger's floor starting from the top floor, and adjusts the total time based on the arrival time of each passenger. It then prints the total time passed, which includes the time taken to travel between floors and any necessary waiting time for passengers.

