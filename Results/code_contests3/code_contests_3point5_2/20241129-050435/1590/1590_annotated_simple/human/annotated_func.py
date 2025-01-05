#State of the program right berfore the function call: n and s are integers such that 1 ≤ n ≤ 100 and 1 ≤ s ≤ 1000. Each fi and ti (floor and time of arrival) are integers such that 1 ≤ fi ≤ s and 1 ≤ ti ≤ 1000.**
def func():
    n, s = map(int, raw_input().split())
    p = []
    for i in range(n):
        fi, ti = map(int, raw_input().split())
        
        p.append((fi, ti))
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100, `s` is an integer such that 1 ≤ `s` ≤ 1000, `p` contains `n` tuples of `(fi, ti)` where each tuple is the input values converted to integers, `i` is `n-1` for the loop to have executed all `n` times.
    p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
    p.append((0, 0))
    time_passed = 0
    for i in range(n + 1):
        time_passed += s - p[i][0]
        
        s = p[i][0]
        
        if time_passed < p[i][1]:
            time_passed += p[i][1] - time_passed
        
    #State of the program after the  for loop has been executed: time_passed is the sum of differences between s and p[i][0] for all i in the range n+1, s is updated to the last p[i][0], n is at least 0, p contains n+1 tuples in descending order based on the first element
    print(time_passed)
#Overall this is what the function does:The function reads input values for the number of floors, time constraints, and arrival times for passengers. It then sorts the passengers based on arrival time in descending order and calculates the total time passed based on the constraints provided. Finally, it prints the total time passed.

