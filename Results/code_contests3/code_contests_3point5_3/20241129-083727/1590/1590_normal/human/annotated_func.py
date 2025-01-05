#State of the program right berfore the function call: n and s are positive integers such that 1 <= n <= 100 and 1 <= s <= 1000. Each passenger's floor fi and arrival time ti are positive integers such that 1 <= fi <= s and 1 <= ti <= 1000.**
def func():
    n, s = map(int, raw_input().split())
    p = []
    for i in range(n):
        fi, ti = map(int, raw_input().split())
        
        p.append((fi, ti))
        
    #State of the program after the  for loop has been executed: `n` is a positive integer between 1 and 100, `s` is a positive integer between 1 and 1000, `p` contains tuples of (fi, ti) values for each iteration of the loop
    p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
    p.append((0, 0))
    time_passed = 0
    for i in range(n + 1):
        time_passed += s - p[i][0]
        
        s = p[i][0]
        
        if time_passed < p[i][1]:
            time_passed += p[i][1] - time_passed
        
    #State of the program after the  for loop has been executed: `n` remains a positive integer between 1 and 100, `s` is updated to a new positive integer between 1 and 1000, `p` remains the same with tuples of (fi, ti) values sorted in descending order, `time_passed` is updated to a new value after all iterations of the loop have finished.
    print(time_passed)
#Overall this is what the function does:The function reads input data for an elevator simulation in a building with `n` passengers. It sorts the passengers' information based on their floor numbers, simulates the elevator movement, and calculates the total time passed. The function then prints the final time passed, representing the total time the elevator spent in the building.

