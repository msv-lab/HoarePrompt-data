#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 10^5. The requests are in the form of "+ i" or "- i" where i is an integer such that 1 ≤ i ≤ n.**
def func_1(n):
    prim[1] = 1
    for i in range(2, n):
        if not prim[i]:
            for j in range(i, n, i):
                prim[j] = i
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 3, `i` is defined, `j` is equal to the last value in the range for the loop to execute, `prim[j]` is assigned the value of `i` for all values of `i` from 1 to `n`. If `prim[i]` is false, `i` is a defined value, `j` is greater than or equal to `n + i`, `prim[j]` is assigned the value of `i` for all values of `i` from 1 to `n`.
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and initializes a list `prim` where the value at index 1 is set to 1. It then iterates through a range of numbers from 2 to `n-1` checking if the value at that index in the `prim` list is false. If false, it assigns the current index to all multiples of that index up to `n`. The function processes requests in the form of "+ i" or "- i" where i is an integer such that 1 ≤ i ≤ n. The function does not have a specific return value.

#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 10^5. Each request is in the form of "+ i" or "- i" where i is an integer such that 1 ≤ i ≤ n.**
def func_2(x):
    fac = []
    while x > 1:
        div = prim[x]
        
        fac.append(div)
        
        while x % div == 0:
            x //= div
        
    #State of the program after the loop has been executed: `fac` contains the product of all distinct prime factors of the original value of `x`, `x` is updated to a value where it is no longer divisible by any factor in `fac`, loop finishes execution
    return fac
    #The program returns the product of all distinct prime factors of the original value of `x`
#Overall this is what the function does:The function `func_2` accepts an integer `x` and calculates the product of all distinct prime factors of the original value of `x`. The function processes each request in the form of "+ i" or "- i" where i is an integer such that 1 ≤ i ≤ x. After processing the requests, it returns the product of prime factors. However, the function lacks handling of the case when x is less than or equal to 1, and it does not consider negative values of x.

