#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, t is an integer such that 1 ≤ t ≤ 10^6, and a is a list of n integers where each integer ai (0 ≤ ai ≤ 86400) represents the time in seconds Luba has to spend working on the i-th day.
def func():
    n, t = list(map(int, raw_input().split()))
    a = raw_input().split()
    i = 0
    while t > 0:
        t -= 86400 - int(a[i])
        
        i += 1
        
    #State of the program after the loop has been executed: `t` is less than or equal to `0`, `i` is equal to the minimum of `n` and the number of iterations executed, `n` is an integer such that 1 ≤ `n` ≤ 100, `a` is a list of `n` strings representing input values.
    print(i)
#Overall this is what the function does:The function reads two integers `n` (the number of days) and `t` (the total time in seconds available to work), and a list of `n` integers representing the time in seconds Luba can work on each day. It calculates how many days Luba can work before the total time `t` runs out, and returns the count of days worked. If `t` becomes less than or equal to 0, the loop stops, and the function prints the number of days worked, which may be less than `n` if `t` runs out before all days are accounted for.

