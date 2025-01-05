#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 10^5.**
def func_1(n):
    prim[1] = 1
    for i in range(2, n):
        if not prim[i]:
            for j in range(i, n, i):
                prim[j] = i
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 2, `m` is an integer such that 1 ≤ m ≤ 10^5, prim list contains 1 at index 1, `i` is equal to `n`, and for each index `j` that is a multiple of `i` and less than `n`, `prim[j]` is assigned the value of `i`.
#Overall this is what the function does:The function `func_1` accepts an integer parameter `n` such that 1 ≤ n ≤ 10^5. It initializes the prim list with 1 at index 1, then iterates through a range from 2 to n, assigning values to elements in the prim list based on certain conditions. The function does not explicitly return any value.

#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 10^5. The requests are in the form of "+ i" or "- i" where i is an integer such that 1 ≤ i ≤ n.**
def func_2(x):
    fac = []
    while x > 1:
        div = prim[x]
        
        fac.append(div)
        
        while x % div == 0:
            x //= div
        
    #State of the program after the loop has been executed: 'fac' contains the appended values of all divisors of the original 'x', 'x' is not divisible by any of the divisors, 'div' is assigned the value of 'prim[x]', 'x' is greater than 1
    return fac
    #The program returns the appended values of all divisors of the original 'x' stored in 'fac'
#Overall this is what the function does:The function `func_2` accepts an integer `x` and calculates all the divisors of `x`, storing them in a list called `fac`. If `x` is 1 or less, the function will not enter the while loop and will return an empty list. The function does not handle cases where `x` is negative.

