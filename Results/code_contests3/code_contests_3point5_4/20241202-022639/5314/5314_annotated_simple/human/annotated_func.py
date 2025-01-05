#State of the program right berfore the function call: n and t are positive integers. ai is a non-negative integer and 0 <= ai <= 86400 for each i.**
def func():
    n, t = list(map(int, raw_input().split()))
    a = raw_input().split()
    i = 0
    while t > 0:
        t -= 86400 - int(a[i])
        
        i += 1
        
    #State of the program after the loop has been executed: `n` and `t` are positive integers, `a` is a list containing the input values, `i` is equal to the total number of elements in list `a`, `t` is updated by subtracting the sum of 86400 - `a[i]` for each element `a[i]` in the list
    print(i)
#Overall this is what the function does:The function `func` reads two positive integers `n` and `t`, as well as a list of non-negative integers `a`. It iterates through the list `a` and subtracts each element from 86400 from `t` until `t` becomes non-positive. The function then prints the total number of elements in the list `a`. The function does not return any specific value. It is missing a condition to handle the case where the loop runs out of elements in `a` before `t` becomes non-positive, which could lead to an index out of range error.

