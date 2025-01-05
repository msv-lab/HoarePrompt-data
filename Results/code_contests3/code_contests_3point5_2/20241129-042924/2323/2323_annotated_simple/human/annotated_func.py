#State of the program right berfore the function call: **
def func():
    a = int(input())
    b = int(input())
    c = 0
    copya = a
    while copya:
        copya //= 10
        
        c += 1
        
    #State of the program after the loop has been executed: `a` is an input integer, `b` is an input integer, `c` is the number of digits in the original value of `a`, `copya` is 0
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
        
    #State of the program after the  for loop has been executed: `a`, `b`, `c`, `copya`, `ans`, `i`, `h` are integers. The final value of `a` is 10, final value of `b`, `c`, `copya`, `i`, and `h` remain unchanged. The final value of `ans` is the minimum value of `a % b` for all iterations of the loop.
    print(ans)
#Overall this is what the function does:The function `func` reads two integer inputs `a` and `b`, calculates the number of digits in `a` and then performs a series of operations on `a` and `b` based on the digits of `a`. It finds the minimum value of `a % b` for all iterations and prints the result. However, the code does not handle cases where `b` is 0, which could result in a division by zero error.

