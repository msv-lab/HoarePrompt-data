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
        
    #State: t is an integer such that 1 <= t <= 10^3, x is an integer such that 1 <= x <= 10^8, and n is an integer such that 1 <= n <= x. The loop has printed the largest divisor of x that is less than or equal to k (x // n) for each iteration, where k is the integer division of x by n. If k is 1, the loop prints 1.
#Overall this is what the function does:The function reads an integer `t` from input, which represents the number of test cases. For each test case, it reads two integers `x` and `n` from input. It then calculates the largest divisor of `x` that is less than or equal to `x // n`. If `x // n` is 1, it prints 1. Otherwise, it prints the largest such divisor. After processing all test cases, the function concludes without returning any value.

