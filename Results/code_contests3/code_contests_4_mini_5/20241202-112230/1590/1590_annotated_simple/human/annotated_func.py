#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 100) representing the number of passengers, s is a positive integer (1 ≤ s ≤ 1000) representing the top floor number, and each passenger's details consist of a floor number fi and an arrival time ti, where each fi is a positive integer (1 ≤ fi ≤ s) and each ti is a positive integer (1 ≤ ti ≤ 1000).
def func():
    n, s = map(int, raw_input().split())
    p = []
    for i in range(n):
        fi, ti = map(int, raw_input().split())
        
        p.append((fi, ti))
        
    #State of the program after the  for loop has been executed: `n` is a positive integer between 1 and 100, `p` is a list containing `n` tuples of integers, each tuple `(fi, ti)` being input values from user input.
    p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
    p.append((0, 0))
    time_passed = 0
    for i in range(n + 1):
        time_passed += s - p[i][0]
        
        s = p[i][0]
        
        if time_passed < p[i][1]:
            time_passed += p[i][1] - time_passed
        
    #State of the program after the  for loop has been executed: `n` is a positive integer between 1 and 100, `i` is `n`, `s` is `p[n][0]`, `time_passed` is the total time calculated based on the elements of `p`.
    print(time_passed)
#Overall this is what the function does:The function accepts a positive integer `n` representing the number of passengers and a positive integer `s` representing the top floor number. It reads `n` pairs of integers representing each passenger's floor number and arrival time, sorts the passengers by their floor number in descending order, and calculates the total time taken to reach all passengers, considering their respective arrival times. Finally, it prints the total time passed, which includes waiting for passengers if the elevator arrives before them. If there are no passengers or if the inputs do not meet the specified constraints, the function will still execute but may not behave as intended in terms of logical validity.

