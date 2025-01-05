#State of the program right berfore the function call: n is an integer representing the number of passengers (1 ≤ n ≤ 100), s is an integer representing the number of the top floor (1 ≤ s ≤ 1000), and each passenger's floor fi and arrival time ti are integers such that (1 ≤ fi ≤ s) and (1 ≤ ti ≤ 1000).
def func():
    n, s = map(int, raw_input().split())
    p = []
    for i in range(n):
        fi, ti = map(int, raw_input().split())
        
        p.append((fi, ti))
        
    #State of the program after the  for loop has been executed: `n` is an integer representing the number of passengers, `p` is a list containing `n` tuples of integers (fi, ti) where each tuple is derived from user input, and `i` is equal to `n` after all iterations have completed.
    p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
    p.append((0, 0))
    time_passed = 0
    for i in range(n + 1):
        time_passed += s - p[i][0]
        
        s = p[i][0]
        
        if time_passed < p[i][1]:
            time_passed += p[i][1] - time_passed
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `i` is `n`, `s` is `p[n][0]`, and `time_passed` is the cumulative time calculated based on the loop's logic.
    print(time_passed)
#Overall this is what the function does:The function accepts two integers, `n` (the number of passengers, where 1 ≤ n ≤ 100) and `s` (the number of the top floor, where 1 ≤ s ≤ 1000). It calculates the total time taken to transport all passengers to their respective floors based on their arrival times and the order of floors, returning the cumulative time spent. The function does not handle any error messages for out-of-range inputs and does not return a list of results; it simply prints the total time.

