#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, x and n are positive integers such that 1 ≤ x ≤ 10^8 and 1 ≤ n ≤ x.
def func():
    for _ in range(int(input())):
        x, n = map(int, input().split())
        
        ans = 1
        
        for i in range(1, int(x ** 0.5) + 1):
            if x % i == 0:
                if n <= x // i:
                    ans = max(ans, i)
                if n <= i:
                    ans = max(ans, x // i)
        
        print(ans)
        
    #State of the program after the  for loop has been executed: `t` is a positive integer such that \(1 \leq t \leq 10^3\), `x` is any integer within the range \(1 \leq x \leq t\), `n` is any integer within the range \(1 \leq n \leq t\), and `ans` is the maximum value among the values of `i` or `x // i` where `x % i == 0` and either `n <= x // i` or `n <= i` for all tested values of `x` and `n`.
#Overall this is what the function does:The function processes a series of test cases, each defined by three values: `t`, `x`, and `n`. For each test case, it calculates the maximum value between `i` and `x // i` where `x % i == 0` and either `n <= x // i` or `n <= i`. It then prints this maximum value for each test case. The function accepts no explicit parameters; instead, it reads `t` from the first line of input, followed by `t` pairs of integers `(x, n)`. There are no return values, but the function prints the calculated maximum value for each test case. Potential edge cases include when `x` is a perfect square, where both `i` and `x // i` might be considered for the maximum value. The function does not handle invalid inputs explicitly; it assumes valid input within the specified ranges.

