#State of the program right berfore the function call: x is an integer such that 1 ≤ x ≤ 10^8, and n is an integer such that 1 ≤ n ≤ x.
def func_1():
    x, n = list(map(int, input().split()))
    ans = 0
    for i in range(1, isqrt(x) + 1):
        if x % i == 0:
            if n <= x // i:
                ans = max(ans, i)
            if n <= i:
                ans = max(ans, x // i)
        
    #State: `x` is an integer such that 1 ≤ x ≤ 10^8, `n` is an integer such that 1 ≤ n ≤ x, `i` is the largest integer such that `i` ≤ `isqrt(x)`, and `ans` is the largest divisor of `x` that is greater than or equal to `n`.
    print(ans)
    #This is printed: - The `print(ans)` statement will print the value of `ans`, which is the largest divisor of `x` that is greater than or equal to `n`.
    #
    #Since the exact values of `x` and `n` are not provided, we can't compute the exact numerical value of `ans`. However, based on the given conditions, the print statement will output the largest divisor of `x` that is greater than or equal to `n`.
    #
    #Output:
#Overall this is what the function does:The function `func_1` reads two integers `x` and `n` from the user input, where `1 ≤ x ≤ 10^8` and `1 ≤ n ≤ x`. It then calculates and prints the largest divisor of `x` that is greater than or equal to `n`. The function does not return any value. After the function concludes, the state of the program includes the printed value of the largest divisor of `x` that is greater than or equal to `n`.

