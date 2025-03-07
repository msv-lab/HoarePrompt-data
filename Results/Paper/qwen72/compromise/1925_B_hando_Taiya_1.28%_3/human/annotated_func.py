#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^3, x is an integer such that 1 <= x <= 10^8, and n is an integer such that 1 <= n <= x.
def func_1():
    x, n = list(map(int, input().split()))
    ans = 0
    for i in range(1, isqrt(x) + 1):
        if x % i == 0:
            if n <= x // i:
                ans = max(ans, i)
            elif n <= i:
                ans = max(ans, x // i)
        
    #State: `t` is an integer such that 1 <= t <= 10^3, `x` and `n` are integers provided by the user, and 1 <= n <= x; `ans` is the largest divisor of `x` that is less than or equal to `n` or the largest quotient of `x` that is less than or equal to `n`.
    print(ans)
    #This is printed: - The `print(ans)` statement will print the value of `ans`, which is the largest divisor of `x` that is less than or equal to `n` or the largest quotient of `x` that is less than or equal to `n`.
    #
    #Since the exact values of `x` and `n` are not provided, we can't compute the exact numerical value of `ans`. However, based on the structure of the problem, the print statement will output the calculated value of `ans`.
    #
    #Output:
#Overall this is what the function does:The function `func_1` reads two integers `x` and `n` from the user input, where `1 <= x <= 10^8` and `1 <= n <= x`. It calculates the largest divisor of `x` that is less than or equal to `n` or the largest quotient of `x` that is less than or equal to `n`. The function then prints this value. The function does not return any value, and the state of the program after the function concludes is that `ans` contains the calculated value, which is printed to the console.

