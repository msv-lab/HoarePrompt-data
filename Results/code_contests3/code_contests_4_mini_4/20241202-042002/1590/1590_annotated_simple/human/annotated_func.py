#State of the program right berfore the function call: n is an integer representing the number of passengers (1 ≤ n ≤ 100), s is an integer representing the top floor number (1 ≤ s ≤ 1000), and each passenger has a floor number fi (1 ≤ fi ≤ s) and an arrival time ti (1 ≤ ti ≤ 1000).
def func():
    n, s = map(int, raw_input().split())
    p = []
    for i in range(n):
        fi, ti = map(int, raw_input().split())
        
        p.append((fi, ti))
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 100, `p` contains `n` tuples of the form (fi, ti) where each tuple corresponds to the input received in each iteration of the loop, and `i` is equal to `n` after all iterations are completed.
    p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
    p.append((0, 0))
    time_passed = 0
    for i in range(n + 1):
        time_passed += s - p[i][0]
        
        s = p[i][0]
        
        if time_passed < p[i][1]:
            time_passed += p[i][1] - time_passed
        
    #State of the program after the  for loop has been executed: `n` is between 1 and 100, `i` is `n`, `p` is sorted in descending order based on the first element of the tuples, `s` is equal to `p[n][0]`, and `time_passed` is the total time passed after accounting for all tuples in `p`.
    print(time_passed)
#Overall this is what the function does:The function accepts an integer `n` representing the number of passengers and an integer `s` representing the top floor number. It takes input for each passenger's floor number `fi` and arrival time `ti`, processes this information to calculate the total time passed for the elevator to pick up all passengers, and prints the total time passed. The function does not return any value. Potential edge cases include ensuring that the arrival times are respected and that the floor numbers are properly processed even if they are the same.

