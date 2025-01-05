#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^4.**
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
        
    #State of the program after the loop has been executed: `n` is an integer such that 1 ≤ n ≤ 10^4, `x` is the remainder after performing a specific operation involving `i` and `k`, `i` is the sum of consecutive integers starting from 1, `k` is the loop control variable, `c` is the number of iterations executed
    print(c)
#Overall this is what the function does:The function `func` reads an integer input, performs a series of operations involving the sum of consecutive integers starting from 1, and prints the number of iterations executed. The function does not accept any parameters and does not return any specific value.

