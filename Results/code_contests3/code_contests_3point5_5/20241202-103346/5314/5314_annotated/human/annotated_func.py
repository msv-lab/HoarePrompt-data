#State of the program right berfore the function call: n and t are positive integers such that 1 <= n <= 100 and 1 <= t <= 10^6. The list ai contains n non-negative integers where each element is less than or equal to 86400.**
def func():
    n, t = list(map(int, raw_input().split()))
    a = raw_input().split()
    i = 0
    while t > 0:
        t -= 86400 - int(a[i])
        
        i += 1
        
    #State of the program after the loop has been executed: `i` is equal to the total number of elements in list `a`, `t` is equal to the remaining time after processing all elements in list `a`
    print(i)
#Overall this is what the function does:The function `func` reads two positive integers `n` and `t`, as well as a list of `n` non-negative integers. It then iterates through the list elements subtracting each element from the time `t` until `t` becomes less than or equal to 0. Finally, it prints the total number of elements processed `i`. The function aims to find the maximum number of consecutive integers in the list `a` that sum up to less than or equal to `t` and outputs this maximum number. However, the implementation does not consider cases where the sum exceeds `t` or when all elements have been processed but `t` is still positive.

