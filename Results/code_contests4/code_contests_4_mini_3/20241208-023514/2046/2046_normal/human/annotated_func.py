#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 10^6 and the length of the string describing the level is equal to n, consisting only of the characters '.' and '*'. The total sum of n across all test cases does not exceed 10^6.
def func():
    le = sys.__stdin__.read().split('\n')[::-1]
    af = []
    for zorg in range(int(le.pop())):
        n = int(le.pop())
        
        l = le.pop()
        
        l = [k for k in range(n) if l[k] == '*']
        
        l = [(b - a) for a, b in enumerate(l)]
        
        if l:
            med = l[len(l) // 2]
            af.append(sum(abs(k - med) for k in l))
        else:
            af.append(0)
        
    #State of the program after the  for loop has been executed: `le` is a list with fewer elements than the initial state, `af` is a list containing the sum of absolute differences from `med` for each iteration where `l` was populated; if `l` was empty in any iteration, `af` includes a corresponding 0 for that iteration, and `n` is the integer value of the last string in `le` before it was fully processed.
    print('\n'.join(map(str, af)))
#Overall this is what the function does:The function accepts multiple test cases, where each test case consists of a positive integer `n` and a string of length `n` containing characters `.` and `*`. It calculates the median position of the `*` characters in the string and sums the absolute differences between each `*`'s position and the median. If there are no `*` characters, it appends 0 to the results for that test case. Finally, it prints the results for all test cases. If all strings contain only `.` (i.e., no `*`), the function will return 0 for those cases.

