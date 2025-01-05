#State of the program right berfore the function call: n and s are positive integers such that 1 ≤ n ≤ 100 and 1 ≤ s ≤ 1000. Each fi and ti (floor and time of arrival) are positive integers such that 1 ≤ fi ≤ s and 1 ≤ ti ≤ 1000.**
def func():
    n, s = map(int, raw_input().split())
    p = []
    for i in range(n):
        fi, ti = map(int, raw_input().split())
        
        p.append((fi, ti))
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ n ≤ 100, `fi` and `ti` are assigned values from the input after splitting them for each iteration, `p` contains all the tuples appended in each iteration of the loop
    p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
    p.append((0, 0))
    time_passed = 0
    for i in range(n + 1):
        time_passed += s - p[i][0]
        
        s = p[i][0]
        
        if time_passed < p[i][1]:
            time_passed += p[i][1] - time_passed
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `fi` and `ti` have their respective values, `p` is sorted in descending order based on the first element of each tuple, a tuple (0, 0) has been appended to `p`, `time_passed` has been updated according to the loop calculations, `s` has the value of the first element of the last tuple in `p`.
    print(time_passed)
#Overall this is what the function does:The function `func` reads input data about passengers and their arrival times on different floors, sorts the passengers based on their floor number, calculates the total time passed considering the time each passenger arrives and departs, and then prints the total time passed. The function does not accept any parameters explicitly but relies on user input.

