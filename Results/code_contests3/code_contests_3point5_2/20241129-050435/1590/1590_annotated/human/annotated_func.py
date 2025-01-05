#State of the program right berfore the function call: **Precondition**: **n and s are positive integers such that 1 <= n <= 100 and 1 <= s <= 1000. Each fi and ti are positive integers such that 1 <= fi <= s and 1 <= ti <= 1000.**
def func():
    n, s = map(int, raw_input().split())
    p = []
    for i in range(n):
        fi, ti = map(int, raw_input().split())
        
        p.append((fi, ti))
        
    #State of the program after the  for loop has been executed: `p` contains a list of tuples with values `(fi, ti)` for each iteration of the loop, `i` is equal to the total number of iterations, `n` is the total number of iterations
    p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
    p.append((0, 0))
    time_passed = 0
    for i in range(n + 1):
        time_passed += s - p[i][0]
        
        s = p[i][0]
        
        if time_passed < p[i][1]:
            time_passed += p[i][1] - time_passed
        
    #State of the program after the  for loop has been executed: `p` contains a list of tuples with values `(fi, ti)` for each iteration of the loop with an additional tuple `(0, 0)` appended at the end and sorted in descending order, `i` is equal to the total number of iterations, `n` is equal to the total number of iterations, `time_passed` is updated by adding the difference between each `p[i][1]` and `p[i][0]`, `s` is updated to the value of `p[i][0]`. If `time_passed` is less than `p[i][1]`, then the program continues.
    print(time_passed)
#Overall this is what the function does:The function `func` reads input values `n` and `s`, then proceeds to read `n` pairs of integers `(fi, ti)` and stores them in a list `p`. It sorts the list `p` based on the first element of the tuple in descending order, then calculates `time_passed` by summing differences between elements of `p`. It updates `s` and checks if `time_passed` is less than `p[i][1]`, adjusting `time_passed` accordingly. Finally, it prints the calculated `time_passed`. The function does not have explicit return values and operates solely based on the input constraints and calculations.

