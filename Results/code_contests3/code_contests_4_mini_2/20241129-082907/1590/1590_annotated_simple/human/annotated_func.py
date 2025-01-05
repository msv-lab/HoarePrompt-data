#State of the program right berfore the function call: n is an integer representing the number of passengers (1 ≤ n ≤ 100), s is an integer representing the number of the top floor (1 ≤ s ≤ 1000), and for each passenger, fi is an integer representing the floor number (1 ≤ fi ≤ s) and ti is an integer representing the time of arrival in seconds (1 ≤ ti ≤ 1000).
def func():
    n, s = map(int, raw_input().split())
    p = []
    for i in range(n):
        fi, ti = map(int, raw_input().split())
        
        p.append((fi, ti))
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 100, `i` is `n - 1`, `p` contains `n` tuples of the form `(fi, ti)`.
    p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
    p.append((0, 0))
    time_passed = 0
    for i in range(n + 1):
        time_passed += s - p[i][0]
        
        s = p[i][0]
        
        if time_passed < p[i][1]:
            time_passed += p[i][1] - time_passed
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 100; `i` is `n + 1`; `p` is sorted based on the first element of each tuple in descending order; `s` is assigned the value of `p[n][0]`; `time_passed` is equal to the maximum of `p[i][1]` and the accumulated time from all previous iterations.
    print(time_passed)
#Overall this is what the function does:The function accepts two integers, `n` (number of passengers) and `s` (the top floor), followed by `n` pairs of integers representing the floor number (`fi`) and arrival time (`ti`) for each passenger. It calculates the total time passed for all passengers to reach the ground floor, accounting for their arrival times and the order in which they are processed based on their floor numbers. The function outputs the total time taken, but does not handle input validation or potential edge cases explicitly, such as when `n` or `s` are outside the specified ranges.

