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
        
    #State: After the loop executes all the iterations, `t` is an integer where 1 <= t <= 10^3, `x` is the first integer from the last input, `n` is the second integer from the last input, `q` is `t - 1`, `i` is `int(sqrt(x)) + 1`, and `ans` is the largest divisor of `x` such that `x - n * d` is non-negative and divisible by `d`, where `d` is a divisor of `x` and `d` is less than or equal to `int(sqrt(x))`. If no such divisor exists, `ans` remains 1.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads two integers `x` and `n`. It then calculates the largest divisor `d` of `x` such that `x - n * d` is non-negative and divisible by `d`. If no such divisor exists, it defaults to 1. The function prints this value for each test case. After processing all test cases, the function completes, and the final state includes the values of `t`, `x`, and `n` from the last test case, with `t` being the total number of test cases processed.

