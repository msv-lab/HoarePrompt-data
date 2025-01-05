#State of the program right berfore the function call: The input consists of two positive integers: Stepan's integer and m, where the length of Stepan's integer is between 2 and 200,000 digits inclusive, and m is an integer such that 2 <= m <= 10^8.**
def func():
    a = int(input())
    b = int(input())
    c = 0
    copya = a
    while copya:
        copya //= 10
        
        c += 1
        
    #State of the program after the loop has been executed: `a` is the input integer provided by the user, `b` is an input integer, `c` is the number of digits in the input integer `a`, `copya` is 0
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
        
    #State of the program after the  for loop has been executed: `a`, `b`, `c`, `copya`, `ans`, `h` are integers. The loop will execute at least once if the number of digits in `a` is greater than 0. If `a` is not divisible by 10, `a`, `b`, `c`, `copya`, `h` will remain the same, and `ans` will be the minimum value between the previous `ans` and the result of `a % b`. If `a` is divisible by 10, `a` will be updated to `a // 10`, and `h` will be assigned the value of `a % 10`. The loop will continue until `c` becomes 0.
    print(ans)
#Overall this is what the function does:The function `func` reads two positive integers as input: Stepan's integer and m, where Stepan's integer has a length between 2 and 200,000 digits inclusive, and m is an integer from 2 to 10^8. It calculates the number of digits in Stepan's integer, performs a series of operations on the integer, and prints the final result. The function does not return any specific output, only processes the input data according to the constraints.

