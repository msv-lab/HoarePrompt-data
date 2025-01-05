#State of the program right berfore the function call: The input consists of two positive integers: Stepan's integer and the number m. Stepan's integer has a length between 2 and 200,000 digits, inclusive, and does not contain leading zeros. The number m is between 2 and 10^8, inclusive.**
def func():
    a = int(input())
    b = int(input())
    c = 0
    copya = a
    while copya:
        copya //= 10
        
        c += 1
        
    #State of the program after the loop has been executed: Stepan's integer is assigned to `a` (unknown non-zero value), `m` is not specified, `b` is an input integer, `c` is the number of digits in the original value of `a`, `copya` is 0
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
        
    #State of the program after the  for loop has been executed: `a`, `b`, `h`, `c`, `copya`, `ans` are integers. The loop will execute `c` times, and after all iterations, `ans` will contain the minimum remainder of the divisions of `a` by `b`. The values of `a`, `h`, and `c` will be updated throughout the loop based on the conditions provided.
    print(ans)
#Overall this is what the function does:The function `func` accepts two positive integers: Stepan's integer `a` and the number `b`. The function calculates the minimum remainder of the divisions of `a` by `b` by iterating over the digits of `a`. The number of digits in `a` is determined by the variable `c`. The function does not have a return value but prints the calculated minimum remainder `ans`.

