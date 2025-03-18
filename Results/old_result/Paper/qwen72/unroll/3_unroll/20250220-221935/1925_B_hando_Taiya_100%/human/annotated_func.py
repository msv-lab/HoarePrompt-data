#State of the program right berfore the function call: The function should take two parameters, x and n, where x is an integer representing the difficulty of the original problem (1 ≤ x ≤ 10^8) and n is an integer representing the number of sub-problems (1 ≤ n ≤ x).
def func_1():
    x, n = list(map(int, input().split()))
    ans = 0
    for i in range(1, isqrt(x) + 1):
        if x % i == 0:
            if n <= x // i:
                ans = max(ans, i)
            if n <= i:
                ans = max(ans, x // i)
        
    #State: `ans` is the maximum divisor of `x` that is greater than or equal to `n`.
    print(ans)
    #This is printed: ans (where ans is the maximum divisor of x that is greater than or equal to n)
#Overall this is what the function does:The function `func_1` reads two integers, `x` and `n`, from the user input. It then calculates and prints the maximum divisor of `x` that is greater than or equal to `n`. If no such divisor exists, it prints 0. The function does not return any value.

