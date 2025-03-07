#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^3, x is a positive integer such that 1 <= x <= 10^8, and n is a positive integer such that 1 <= n <= x.
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
        
    #State: After the loop executes all iterations, `t` is a positive integer such that 1 <= t <= 10^3, `x` and `n` are updated to the values provided by the user input (with 1 <= x <= 10^8 and 1 <= n <= x) for each iteration, `q` is `t - 1`, and `ans` is the largest divisor of `x` for each iteration such that `x - n * d` is non-negative and divisible by `d`, where `d` is a divisor of `x`. If no such divisor exists for any iteration, `ans` remains 1 for that iteration.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases, followed by `t` pairs of integers `x` and `n` from the user. For each pair, it calculates the largest divisor `d` of `x` such that `x - n * d` is non-negative and divisible by `d`. If no such divisor exists, it defaults to 1. The function prints the result for each test case. After all iterations, `t` remains a positive integer between 1 and 10^3, and for each iteration, `x` and `n` are updated to the values provided by the user, while the final printed value is the largest valid divisor found for each pair.

