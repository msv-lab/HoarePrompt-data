#State of the program right berfore the function call: t is an integer where 1 <= t <= 10^3, x is an integer where 1 <= x <= 10^8, and n is an integer where 1 <= n <= x.
def func():
    for q in range(int(input())):
        x, n = list(map(int, input().split(' ')))
        
        ans = 1
        
        for i in range(1, int(sqrt(x)) + 1):
            if x % i == 0:
                if x - n * i >= 0 and (x - n * i) % i == 0:
                    ans = max(ans, i)
                if x - n * (x // i) >= 0 and x // i > 0 and (x - n * (x // i)) % (x //
                    i) == 0:
                    ans = max(ans, x // i)
        
        print(ans)
        
    #State: After all iterations, `i` will have reached `int(sqrt(x)) + 1` for each pair of `x` and `n` processed. The variable `ans` will hold the maximum value among all divisors `i` (from 1 to `int(sqrt(x))`) that satisfy the conditions: `x % i == 0`, `x - n * i >= 0`, `(x - n * i) % i == 0`, and `x - n * (x // i) >= 0`, `(x - n * (x // i)) % (x // i) == 0`, and `x // i > 0`. If no such divisor exists, `ans` will remain 1. The values of `x`, `n`, and `t` remain unchanged for each iteration, but `q` will have incremented from 0 to `t-1`.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads two integers `x` and `n`. It then calculates the largest divisor `ans` of `x` such that `x - n * i` is non-negative and divisible by `i`, where `i` is a divisor of `x` within the range from 1 to the square root of `x`. If no such divisor exists, `ans` remains 1. The function prints the value of `ans` for each test case. The values of `t`, `x`, and `n` are not modified during the function's execution.

