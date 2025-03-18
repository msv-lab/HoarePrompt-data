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
        
    #State: The value of `t` remains unchanged, and for each iteration of the outer loop, the values of `x` and `n` are updated based on the input provided. The variable `ans` is calculated for each pair of `x` and `n`, and the final value of `ans` for each iteration is printed. After all iterations, the values of `x` and `n` are the last pair of values read from input, and `ans` is the last calculated value for that pair.
#Overall this is what the function does:The function `func` reads an integer `t` from input, which represents the number of test cases. For each test case, it reads two integers `x` and `n` from input. The function then calculates the largest integer `ans` such that `x - n * ans` is divisible by `ans` and is non-negative. After processing all test cases, the function prints the value of `ans` for each test case. The values of `x` and `n` are updated for each test case, and the final state of the program includes the last values of `x` and `n` read from input, and the last calculated value of `ans` for that test case. The function does not return any value.

