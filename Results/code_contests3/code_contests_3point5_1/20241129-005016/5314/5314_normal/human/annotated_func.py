#State of the program right berfore the function call: **
def func():
    n, t = list(map(int, raw_input().split()))
    a = raw_input().split()
    i = 0
    while t > 0:
        t -= 86400 - int(a[i])
        
        i += 1
        
    #State of the program after the loop has been executed: 't' will be less than 0 after the loop finishes executing, 'n', 'a', and 'i' will retain their initial values
    print(i)
#Overall this is what the function does:The function `func` reads inputs for `n` and `t`, then reads a list of integers `a`. It iterates through the elements of `a` subtracting each element from `86400` from `t` until `t` becomes less than 0. Finally, it prints the value of `i`, which represents how many elements of `a` were subtracted from `t`. The function does not have a specified return value. However, a potential edge case to consider is what happens if the loop finishes and `t` is still greater than 0.

