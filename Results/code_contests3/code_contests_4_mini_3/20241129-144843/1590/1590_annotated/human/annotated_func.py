#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, s is an integer such that 1 ≤ s ≤ 1000, and for each passenger i, fi is an integer such that 1 ≤ fi ≤ s and ti is an integer such that 1 ≤ ti ≤ 1000.
def func():
    n, s = map(int, raw_input().split())
    p = []
    for i in range(n):
        fi, ti = map(int, raw_input().split())
        
        p.append((fi, ti))
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100, `s` is an integer such that 1 ≤ `s` ≤ 1000, `p` contains `n` tuples of the form `(fi, ti)`, `i` is equal to `n`.
    p = sorted(p, key=lambda passenger: passenger[0], reverse=True)
    p.append((0, 0))
    time_passed = 0
    for i in range(n + 1):
        time_passed += s - p[i][0]
        
        s = p[i][0]
        
        if time_passed < p[i][1]:
            time_passed += p[i][1] - time_passed
        
    #State of the program after the  for loop has been executed: `s` is equal to `p[n][0]`, `time_passed` is the cumulative time calculated based on the values in `p`.
    print(time_passed)
#Overall this is what the function does:The function accepts two integers `n` (the number of passengers) and `s` (the initial capacity). It then reads `n` pairs of integers `fi` (the passenger's fixed value) and `ti` (the passenger's time value). The function calculates the cumulative time based on the sorted order of the passengers' fixed values and their corresponding time requirements, ultimately printing the total calculated time. The function does not explicitly handle edge cases such as invalid inputs or constraints outside the specified ranges.

