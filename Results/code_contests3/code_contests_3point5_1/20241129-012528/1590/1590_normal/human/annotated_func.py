#State of the program right berfore the function call: n and s are integers such that 1 ≤ n ≤ 100 and 1 ≤ s ≤ 1000. Each passenger's arrival floor and time are integers such that 1 ≤ fi ≤ s and 1 ≤ ti ≤ 1000.**
def func():
    n, s = map(int, raw_input().split())
    p = []
    for i in range(n):
        fi, ti = map(int, raw_input().split())
        
        p.append((fi, ti))
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `s` is assigned a value based on user input, `p` contains a list of tuples obtained from user input, where each tuple represents the values entered during each iteration of the loop
    p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
    p.append((0, 0))
    time_passed = 0
    for i in range(n + 1):
        time_passed += s - p[i][0]
        
        s = p[i][0]
        
        if time_passed < p[i][1]:
            time_passed += p[i][1] - time_passed
        
    #State of the program after the  for loop has been executed: `n` is less than or equal to the length of list `p`, `s` is the last updated value from `p`, `p` contains a list of tuples sorted in descending order, `time_passed` is updated based on the values in tuples of `p` from index 0 to `n-1`. If `time_passed` is less than `p[i][1]`, the loop will update `time_passed` accordingly.
    print(time_passed)
#Overall this is what the function does:The function reads input for the number of passengers and the time constraints. It then processes the arrival information for each passenger, calculates the time taken for each passenger to arrive, and prints the total time passed. The passengers are sorted based on their arrival floors, and the time taken is adjusted based on the specified time constraints.

