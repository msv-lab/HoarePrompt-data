#State of the program right berfore the function call: n and a are integers such that 1 ≤ a ≤ n ≤ 100 000 and n is even.
def func():
    n, a = map(int, input().split())
    if (a <= n // 2) :
        print(a // 2 + a % 2)
    else :
        print((n - a + 1) // 2 + (n - a + 1) % 2)
    #State of the program after the if-else block has been executed: *`a` is an integer between 1 and `n` inclusive, `n` is an even integer between `a` and 100,000 inclusive. If `a` is less than or equal to `n // 2`, the value of `a` is printed as `a // 2 + a % 2`. Otherwise, the output is `n - a + 2`.
#Overall this is what the function does:The function reads two integers \( n \) and \( a \) from the standard input, where \( 1 \leq a \leq n \leq 100,000 \) and \( n \) is even. It then prints one of two possible values based on the comparison of \( a \) and \( n/2 \). Specifically, if \( a \leq n/2 \), it prints \( a // 2 + a \% 2 \). Otherwise, it prints \( (n - a + 1) // 2 + (n - a + 1) \% 2 \). The function does not return a value but modifies the standard output directly. Potential edge cases include when \( a \) is exactly \( n/2 \), which falls under the first condition. The function also handles the maximum constraint on \( n \) and ensures \( n \) remains even throughout the process.

