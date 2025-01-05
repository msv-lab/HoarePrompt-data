#State of the program right berfore the function call: n and s are positive integers such that 1 <= n <= 100 and 1 <= s <= 1000. Each passenger's floor (fi) is between 1 and s, and the time of arrival (ti) is between 1 and 1000.**
def func():
    n, s = map(int, raw_input().split())
    p = []
    for i in range(n):
        fi, ti = map(int, raw_input().split())
        
        p.append((fi, ti))
        
    #State of the program after the  for loop has been executed: `n` is a positive integer between 1 and 100, `s` is a positive integer between 1 and 1000, `p` contains all the tuples `(fi, ti)` appended during the loop execution, where each tuple represents the values inputted during each iteration.
    p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
    p.append((0, 0))
    time_passed = 0
    for i in range(n + 1):
        time_passed += s - p[i][0]
        
        s = p[i][0]
        
        if time_passed < p[i][1]:
            time_passed += p[i][1] - time_passed
        
    #State of the program after the  for loop has been executed: `n` is a positive integer between 1 and 100, `s` is equal to the first element of tuple `p` at index n, `p` contains all the tuples `(fi, ti)` sorted in descending order based on the first element with an additional tuple `(0, 0)`, `time_passed` is equal to the sum of all `p[i][1]` for i in range(n), `i` is n.
    print(time_passed)
#Overall this is what the function does:The function `func` reads input data for the number of passengers and the elevator capacity. It then calculates the average waiting time for all passengers based on their floor and time of arrival. The passengers are sorted based on their floor in descending order. However, there is a potential issue in the calculation logic where the time passed is not correctly calculated due to the condition check `time_passed < p[i][1]`. This could lead to incorrect waiting time calculations for passengers.

