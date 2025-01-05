#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, s is an integer such that 1 ≤ s ≤ 1000, and each passenger's information consists of two integers fi and ti such that 1 ≤ fi ≤ s and 1 ≤ ti ≤ 1000.
def func():
    n, s = map(int, raw_input().split())
    p = []
    for i in range(n):
        fi, ti = map(int, raw_input().split())
        
        p.append((fi, ti))
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100, `i` is `n`, and `p` contains `n` tuples of the form (fi, ti).
    p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
    p.append((0, 0))
    time_passed = 0
    for i in range(n + 1):
        time_passed += s - p[i][0]
        
        s = p[i][0]
        
        if time_passed < p[i][1]:
            time_passed += p[i][1] - time_passed
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100, `i` is `n`, `p` is sorted in descending order, `s` is `p[n][0]`, and `time_passed` is the total accumulated time based on the values in `p`.
    print(time_passed)
#Overall this is what the function does:The function accepts no parameters directly but reads two integers `n` (the number of passengers) and `s` (the starting position), and then a list of `n` tuples containing passenger information `(fi, ti)`, where `fi` is the position and `ti` is the time constraint for each passenger. It calculates the total time passed based on these inputs, adjusting for time constraints, and prints this total time. The function does not handle cases where `n` is 0 or where all time constraints are met without additional time passed.

