#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 10^5.**
def func_1(n):
    prim[1] = 1
    for i in range(2, n):
        if not prim[i]:
            for j in range(i, n, i):
                prim[j] = i
        
    #State of the program after the  for loop has been executed: Output State: `prim[1]` is 1, all other `prim` values are set to the smallest prime factor of their index, `i` is `n`, `n` is the upper limit of the range for the loops.
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` as a parameter. It initializes `prim[1]` to 1 and then iterates through a loop setting the smallest prime factor of each index in `prim` up to `n`. The function does not have a specified return value.

#State of the program right berfore the function call: **n and m are positive integers such that 1 ≤ n, m ≤ 10^5. Each request is in the form of either "+ i" or "- i" where i is an integer such that 1 ≤ i ≤ n.**
def func_2(x):
    fac = []
    while x > 1:
        div = prim[x]
        
        fac.append(div)
        
        while x % div == 0:
            x //= div
        
    #State of the program after the loop has been executed: `fac` contains all the prime factors of the initial value of `x`, `x` is less than 1, the loop does not execute again
    return fac
    #The program returns all the prime factors of the initial value of `x` stored in `fac`
#Overall this is what the function does:The function func_2 accepts a positive integer x and calculates all the prime factors of x. It stores these prime factors in a list called fac. The function then returns the list of prime factors. If x is less than or equal to 1, the function does not enter the loop and returns an empty list.

