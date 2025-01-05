#State of the program right berfore the function call: The input values for Stepan's integer and m are positive integers. The length of Stepan's integer is between 2 and 200,000 digits, and m is between 2 and 108 (inclusive).**
def func():
    a = int(input())
    b = int(input())
    c = 0
    copya = a
    while copya:
        copya //= 10
        
        c += 1
        
    #State of the program after the loop has been executed: `a` is a positive integer, `b` is an input integer, `c` is the number of digits in the original value of `a`, `copya` is 0
    ans = a % b
    for i in range(c):
        if a % 10 != 0:
            h = a % 10
            a //= 10
            a = 10 ** c * h + a
            ans = min(ans, a % b)
        else:
            h = a % 10
            a //= 10
            a = 10 ** c * h + a
        
    #State of the program after the  for loop has been executed: `a` is a positive integer, `b` is an input integer, `c` is the number of digits in the original value of `a`, `copya` is 0, `ans` is the minimum remainder of all the divisions of `a` by `b` after each iteration of the loop.
    print(ans)
#Overall this is what the function does:The function `func` accepts two positive integer inputs, Stepan's integer and m. Stepan's integer is a positive integer with a length between 2 and 200,000 digits, and m is a positive integer between 2 and 10^8 (inclusive). The function calculates the minimum remainder of the divisions of Stepan's integer by m and prints the result.

