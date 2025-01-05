#State of the program right berfore the function call: n is an integer such that 5 <= n <= 100.**
def func_1(n, a):
    r = 1
    s = 1
    p = n
    g = 1
    for i in range(a):
        r = r * p
        
        p -= 1
        
        s = s * g
        
        g += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer between 5 and 100, `r` is the factorial of `n`, `s` is the product of numbers from 1 to `n`, `p` is 0, `g` is `n + 1`, `a` is equal to `n`, for the loop to execute `n` times `i` is from 0 to `n-1`
    return r / s
    #The program returns the factorial of 'n' divided by the product of numbers from 1 to 'n'
#Overall this is what the function does:The function func_1 accepts two parameters, n and a, where n is an integer within the range of 5 to 100. It calculates the factorial of n and returns the result divided by the product of numbers from 1 to n. The function computes the factorial of n by multiplying the numbers from n down to 1 and also calculates the product of numbers from 1 to n.

