#State of the program right berfore the function call: **Precondition**: The input consists of two integers n and t where 1 ≤ n ≤ 100 and 1 ≤ t ≤ 10^6. The second line contains n integers ai representing the time Luba has to spend on work during each day, where 0 ≤ ai ≤ 86400.
def func():
    n, t = list(map(int, raw_input().split()))
    a = raw_input().split()
    i = 0
    while t > 0:
        t -= 86400 - int(a[i])
        
        i += 1
        
    #State of the program after the loop has been executed: `n` has been updated based on the calculations, `t` is 0 or negative, `i` has been incremented for each iteration of the loop
    print(i)
#Overall this is what the function does:The function reads input consisting of two integers n and t, where n represents the number of days and t is the total time available. It then reads n integers representing the time Luba has to spend on work each day. The function iterates through the days, subtracting the time Luba has to spend each day from the total time available. It prints the number of days Luba can work based on the given constraints.

