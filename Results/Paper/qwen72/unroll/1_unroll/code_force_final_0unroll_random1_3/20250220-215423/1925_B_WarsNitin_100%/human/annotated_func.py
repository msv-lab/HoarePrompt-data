#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^3, x is an integer such that 1 <= x <= 10^8, and n is an integer such that 1 <= n <= x.
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
        
    #State: t is an integer such that 1 <= t <= 10^3, x and n are unchanged, and ans contains the largest integer divisor of x such that (x - n * divisor) is divisible by the divisor and non-negative.
#Overall this is what the function does:The function `func` reads an integer `t` from user input, which represents the number of test cases. For each test case, it reads two integers `x` and `n` from user input. The function then calculates and prints the largest integer divisor of `x` such that `(x - n * divisor)` is divisible by the divisor and non-negative. The function does not return any value; it only prints the result for each test case. After the function concludes, `t` remains an integer between 1 and 10^3, and `x` and `n` are unchanged for each test case.

