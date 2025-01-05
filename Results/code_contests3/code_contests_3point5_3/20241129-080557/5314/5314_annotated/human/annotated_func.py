#State of the program right berfore the function call: n is a positive integer representing the number of days, t is a positive integer representing the time required to read the book, ai is a non-negative integer representing the time Luba has to spend on work during the i-th day.**
def func():
    n, t = list(map(int, raw_input().split()))
    a = raw_input().split()
    i = 0
    while t > 0:
        t -= 86400 - int(a[i])
        
        i += 1
        
    #State of the program after the loop has been executed: `n` is a positive integer, `t` is a positive integer greater than or equal to 86400 - int(a[i]), `ai` represents the time Luba has to spend on work during the i-th day, `a` is a list containing the input values, `i` is equal to the number of elements in list `a`
    print(i)
#Overall this is what the function does:The function `func` reads input values for the number of days `n`, the time required to read the book `t`, and the time Luba spends on work each day `ai`. It then iterates over the list `a` containing Luba's work times for each day, subtracting the time spent on work from the available time `t` until `t` becomes less than the difference between 86400 and the work time on a particular day. The function prints the number of days `i` for which the time spent on work exceeds the available time. The function does not have an explicit return value and focuses on iterating through the work times and tracking the number of days exceeding the available time.

