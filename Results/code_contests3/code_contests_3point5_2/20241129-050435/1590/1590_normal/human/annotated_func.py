#State of the program right berfore the function call: n and s are positive integers such that 1 ≤ n ≤ 100 and 1 ≤ s ≤ 1000. Each passenger's floor fi is an integer between 1 and s, and the time of arrival ti is a positive integer less than or equal to 1000.**
def func():
    n, s = map(int, raw_input().split())
    p = []
    for i in range(n):
        fi, ti = map(int, raw_input().split())
        
        p.append((fi, ti))
        
    #State of the program after the  for loop has been executed: `n` is a positive integer between 1 and 100, `s` is a positive integer between 1 and 1000, `p` contains a list of tuples with the values of `fi` and `ti` for each iteration of the loop
    p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
    p.append((0, 0))
    time_passed = 0
    for i in range(n + 1):
        time_passed += s - p[i][0]
        
        s = p[i][0]
        
        if time_passed < p[i][1]:
            time_passed += p[i][1] - time_passed
        
    #State of the program after the  for loop has been executed: `n` is a positive integer between 1 and 100, `s` is the first element of the tuple (0, 0) in p, `p` is sorted in descending order based on the first element of each tuple with a tuple (0, 0) appended to `p`, `time_passed` is the sum of the differences between consecutive elements in the first position of tuples in `p`, `i` is the last index of the loop, which is n. If time_passed is less than p[i][1], the program will remain in the current state.
    print(time_passed)
#Overall this is what the function does:The function accepts no parameters. It reads input data about passengers arriving at a building, calculates the time passed for each passenger based on the floor they arrived at and the time of arrival, and prints the total time passed. However, the current implementation does not accurately calculate the time passed for each passenger due to a logic error in the calculation. The code should be adjusted to correctly calculate the time passed for each passenger.

