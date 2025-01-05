#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10,000.
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
        
    #State of the program after the loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 10,000; `x` is the remainder after subtracting the largest possible sum of consecutive integers from the initial `x`; `i` is the last value incremented before exiting the loop; `k` is the final incremented value which will be greater than the last used `k`; `c` is the total number of successful iterations of the loop.
    print(c)
#Overall this is what the function does:The function accepts an integer input `x` (where 1 ≤ x ≤ 10,000) and calculates the maximum number of consecutive integers starting from 1 that can be summed without exceeding `x`. It then prints the count of these integers. The function does not return any value.

