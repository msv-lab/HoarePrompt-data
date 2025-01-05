#State of the program right berfore the function call: n and t are integers such that 1 <= n <= 100 and 1 <= t <= 10^6. The list ai contains n integers representing the time Luba has to spend on her work during each day, where each ai is an integer such that 0 <= ai <= 86400.**
def func():
    n, t = list(map(int, raw_input().split()))
    a = raw_input().split()
    i = 0
    while t > 0:
        t -= 86400 - int(a[i])
        
        i += 1
        
    #State of the program after the loop has been executed: `n` and `t` are integers satisfying the given constraints, `a` is a list of strings, `i` is equal to the number of elements in `a`, `t` is updated based on the sum of `86400 - int(a[i])` for each element in `a`
    print(i)
#Overall this is what the function does:The function `func` reads input values `n` and `t`, where `n` represents the number of time values Luba has to spend on work each day, and `t` represents the total number of days. It then reads a list of time values for each day and calculates the total time Luba has spent on work for `t` days by subtracting each day's time from 86400. The function prints the total number of days `i` that have been processed.

