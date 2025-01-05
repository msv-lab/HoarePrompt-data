#State of the program right berfore the function call: ** n and s are integers such that 1 ≤ n ≤ 100 and 1 ≤ s ≤ 1000. The input details the arrival time and floor of each passenger within the valid range.
def func():
    n, s = map(int, raw_input().split())
    p = []
    for i in range(n):
        fi, ti = map(int, raw_input().split())
        
        p.append((fi, ti))
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `s` is an integer within the specified range, `p` contains a list of tuples (fi, ti) with n elements, each element corresponding to the input values provided during each iteration of the loop
    p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
    p.append((0, 0))
    time_passed = 0
    for i in range(n + 1):
        time_passed += s - p[i][0]
        
        s = p[i][0]
        
        if time_passed < p[i][1]:
            time_passed += p[i][1] - time_passed
        
    #State of the program after the  for loop has been executed: `n` is 0 or greater, `s` is the last element of the last tuple in list `p`, `p` contains a list of tuples sorted in descending order based on the first element of each tuple, `time_passed` is the sum of differences between consecutive elements of the first elements of tuples in list `p` and the maximum of the second elements of tuples in list `p`
    print(time_passed)
#Overall this is what the function does:The function `func` reads input details about the arrival time and floor of passengers in a building. It sorts the passengers based on their arrival time, calculates the total time passed based on the floor changes, and handles scenarios where time spent on a floor exceeds the passenger's specified time. The function then prints the total time passed. The function does not return any value. It processes input details for further analysis or actions.

