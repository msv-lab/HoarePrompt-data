#State of the program right berfore the function call: n and t are integers such that 1 <= n <= 100 and 1 <= t <= 10^6. The list ai contains n integers where 0 <= ai <= 86400 for each element.**
def func():
    n, t = list(map(int, raw_input().split()))
    a = raw_input().split()
    i = 0
    while t > 0:
        t -= 86400 - int(a[i])
        
        i += 1
        
    #State of the program after the loop has been executed: `n` and `t` are assigned correctly, `ai` remains uninitialized, `i` is the total number of times the loop executed, for the loop to execute the last time `t` is greater than 0 and `t` is updated by subtracting 86400 - int(a[i]) for the last time
    print(i)
#Overall this is what the function does:The function `func` reads input values for `n` and `t`, then processes a list `a` containing `n` integers. It iterates over the list until `t` becomes zero, decrementing `t` by the difference between 86400 and the integer value of each element in `a`. The function prints the total number of iterations `i`. The function does not explicitly return any value. Potential edge cases or missing logic include handling cases where `t` could become negative during the loop execution.

