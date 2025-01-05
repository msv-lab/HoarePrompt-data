#State of the program right berfore the function call: n is an integer representing the number of days (1 ≤ n ≤ 100), t is an integer representing the time required to read the book in seconds (1 ≤ t ≤ 10^6), and ai is a list of n integers where each ai represents the time Luba has to work on the i-th day (0 ≤ ai ≤ 86400).
def func():
    n, t = list(map(int, raw_input().split()))
    a = raw_input().split()
    i = 0
    while t > 0:
        t -= 86400 - int(a[i])
        
        i += 1
        
    #State of the program after the loop has been executed: `t` is the remaining time after subtracting the total of `86400 - int(a[j])` for each `j` from 0 to `i-1`, `i` is the total number of elements processed from list `a`, which is equal to the number of days (or until `t` becomes non-positive). If `t` is not enough for all days in `a`, `i` will be less than the length of `a`. If `t` was sufficient for all days, `i` will be equal to the length of `a`.
    print(i)
#Overall this is what the function does:The function accepts an integer `n` representing the number of days and an integer `t` representing the total time required to read a book in seconds. It processes a list of integers `a`, where each value represents the time Luba has to work on each respective day. The function calculates how many days Luba can spend reading the book based on the available time each day by deducting the time worked from a full day (86400 seconds) until the total reading time `t` is exhausted or there are no more days left. It returns the number of days Luba can read before running out of time. If `t` is greater than the total available time across all days, the function will return `n`, indicating she can read for all days.

