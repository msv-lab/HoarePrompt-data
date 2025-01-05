#State of the program right berfore the function call: n and t are positive integers such that 1 <= n <= 100 and 1 <= t <= 10^6. The list ai contains n non-negative integers such that 0 <= ai <= 86400 for each i.
def func():
    n, t = list(map(int, raw_input().split()))
    a = raw_input().split()
    i = 0
    while t > 0:
        t -= 86400 - int(a[i])
        
        i += 1
        
    #State of the program after the loop has been executed: `i` is the number of times the loop executed successfully, `t` is updated based on the calculations `t -= 86400 - int(a[i])`, `t` will eventually become less than 0, and the loop will terminate
    print(i)
#Overall this is what the function does:The function `func` reads input values for `n`, `t`, and a list `a` where `n` and `t` are positive integers within specific ranges and `a` contains non-negative integers. It then iterates over the elements in `a` subtracting each element from `86400` until `t` becomes less than 0. The function prints the number of successful iterations `i`. However, there is a missing return value in the function, and it does not handle the case where `t` becomes negative before iterating through all elements in `a`.

