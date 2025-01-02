#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^9.
def func():
    n = int(raw_input())
    count = n
    while n != 1:
        i = 2
        
        while divmod(n, i)[1] != 0:
            i += 1
        
        b = divmod(n, i)[0]
        
        count += b
        
        n = b
        
    #State of the program after the loop has been executed: `n` is 1, `count` is the sum of the original value of `n` and the quotients obtained at each step of the division by the smallest prime factor of `n`.
    print(count)
#Overall this is what the function does:The function `func` reads an integer `n` (where 2 ≤ n ≤ 10^9) from the user, and then repeatedly divides `n` by its smallest prime factor until `n` becomes 1. During each division, it adds the quotient to a running total (`count`), which starts with the initial value of `n`. After the loop completes, the function prints the final value of `count`. The final state of the program is that `n` is 1, and `count` is the sum of the original value of `n` and all the quotients obtained during the division process.

