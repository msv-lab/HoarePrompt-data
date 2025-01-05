#State of the program right berfore the function call: n is an integer such that 1 <= n <= 10^4.**
def func():
    x = int(input())
    i = 0
    k = 1
    c = 0
    while x - (i + k) >= 0:
        i = i + k
        
        x = x - i
        
        c = c + 1
        
        k = k + 1
        
    #State of the program after the loop has been executed: `n` is an integer such that 1 <= n <= 10^4, `x` is updated to x - i - k, `i` is increased by a value of 2 for each iteration of the loop, `k` is equal to the final value of k after the loop completes, `c` is the total number of times the loop executed
    print(c)
#Overall this is what the function does:The function `func` reads an integer `x` from the user, then iterates using a loop until `x` becomes negative. During each iteration, it updates `i`, `x`, `c`, and `k` accordingly. Finally, it prints the total number of loop iterations `c`. The function does not accept any explicit parameters and relies solely on the input `x` provided by the user.

