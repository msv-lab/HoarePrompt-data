#State of the program right berfore the function call: n and s are integers such that 1 <= n <= 100 and 1 <= s <= 1000. Each passenger's arrival time and floor values are integers such that 1 <= fi <= s, 1 <= ti <= 1000.**
def func():
    n, s = map(int, raw_input().split())
    p = []
    for i in range(n):
        fi, ti = map(int, raw_input().split())
        
        p.append((fi, ti))
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `s` is an integer such that 1 <= s <= 1000, `p` is a list containing all the tuples `(fi, ti)` added during the iterations of the loop, `i` is equal to n, `fi` and `ti` are assigned the integer values obtained from splitting the input
    p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
    p.append((0, 0))
    time_passed = 0
    for i in range(n + 1):
        time_passed += s - p[i][0]
        
        s = p[i][0]
        
        if time_passed < p[i][1]:
            time_passed += p[i][1] - time_passed
        
    #State of the program after the  for loop has been executed: `time_passed` is the final accumulated time passed, `s` is the last value of `p[i][0]` after the loop finishes, `p` is a list containing all the tuples `(fi, ti)` added during the iterations of the loop and sorted based on the first element of each tuple in descending order, `i` is 0.
    print(time_passed)
#Overall this is what the function does:The function reads input regarding the arrival times and floor values of passengers in a building, sorts and processes them to calculate the total time passed, and then prints the final accumulated time passed.

