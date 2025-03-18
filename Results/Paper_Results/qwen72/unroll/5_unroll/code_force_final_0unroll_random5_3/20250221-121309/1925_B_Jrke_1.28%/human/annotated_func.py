#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^3, x is an integer such that 1 <= x <= 10^8, and n is an integer such that 1 <= n <= x.
def func():
    for _ in range(int(input())):
        x, n = map(int, input().split())
        
        k = x // n
        
        if k == 1:
            print(1)
            continue
        
        ans = 1
        
        for i in range(1 + (1 if x % 2 == 0 else 0), int(x ** 0.5) + 1, 2):
            if x % i == 0:
                l = [ans]
                if i <= k:
                    l.append(i)
                if x // i <= k:
                    l.append(x // i)
                ans = max(l)
        
        print(ans)
        
    #State: t is an integer such that 1 <= t <= 10^3, x and n are undefined after the loop, and ans is the maximum integer divisor of x that is less than or equal to k, where k = x // n, for each iteration of the loop.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads two integers `x` and `n` from the input, where `1 <= x <= 10^8` and `1 <= n <= x`. It then calculates the maximum integer divisor of `x` that is less than or equal to `x // n` and prints this value. After processing all test cases, `t` remains defined, but `x` and `n` are undefined. The function does not return any value; it only prints the results.

