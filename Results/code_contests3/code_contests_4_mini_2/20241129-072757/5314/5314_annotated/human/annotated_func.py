#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100, t is a positive integer such that 1 ≤ t ≤ 10^6, and a is a list of n integers where each integer ai represents the time Luba has to spend on work during the i-th day and satisfies 0 ≤ ai ≤ 86400.
def func():
    n, t = list(map(int, raw_input().split()))
    a = raw_input().split()
    i = 0
    while t > 0:
        t -= 86400 - int(a[i])
        
        i += 1
        
    #State of the program after the loop has been executed: `t` is reduced by the sum of `86400 - int(a[j])` for all `j` from 0 to `i-1`, `i` is equal to the total number of iterations executed (which is the length of `a` or until `t` becomes non-positive), and `n` remains a positive integer such that 1 ≤ `n` ≤ 100.
    print(i)
#Overall this is what the function does:The function accepts a positive integer `n`, a positive integer `t`, and a list of `n` integers representing time spent on work. It calculates how many days it takes for `t` to be reduced to zero or less by subtracting the available time for each day and prints the number of days counted.

