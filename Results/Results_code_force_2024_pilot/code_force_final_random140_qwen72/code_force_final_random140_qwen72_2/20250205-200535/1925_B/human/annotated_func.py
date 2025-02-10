#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^3, x is a positive integer such that 1 <= x <= 10^8, and n is a positive integer such that 1 <= n <= x.
def func():
    for _ in range(int(input())):
        x, n = map(int, input().split())
        
        k = x // n
        
        ans = 1
        
        for i in range(1, int(x ** 0.5) + 2):
            if x % i == 0:
                l = [ans]
                if i <= k:
                    l.append(i)
                if x // i <= k:
                    l.append(x // i)
                ans = max(l)
        
        print(ans)
        
    #State: `t` is a positive integer such that 1 <= t <= 10^3, `x` is a positive integer such that 1 <= x <= 10^8, `n` is a positive integer such that 1 <= n <= x, `k` is the integer division of `x` by `n` (i.e., `k = x // n`), `ans` is the largest divisor of `x` that is less than or equal to `k`, `i` is the integer part of the square root of `x` plus 1.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads two integers `x` and `n`. It then calculates the largest divisor of `x` that is less than or equal to the integer division of `x` by `n` (`x // n`). This largest divisor is printed for each test case. The function does not return any value; it only prints the results. After the function concludes, `t` remains a positive integer between 1 and 10^3, `x` and `n` are positive integers within their respective ranges, and the largest divisor of `x` that is less than or equal to `x // n` has been printed for each test case.

