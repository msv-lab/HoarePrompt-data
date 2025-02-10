#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^3, x is an integer such that 1 <= x <= 10^8, and n is an integer such that 1 <= n <= x.
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
        
    #State: After the loop has executed all iterations, `t` is an integer such that \(1 \leq t \leq 10^3\), `x` and `n` are integers provided by the input, `k` is the integer division result of `x` by `n`, `ans` is the maximum divisor of `x` that is less than or equal to `k`, and `i` is the last value it reached, which is `int(x
#Overall this is what the function does:The function reads multiple pairs of integers (x, n) from the standard input, where each pair represents a test case. For each test case, it calculates the largest divisor of x that is less than or equal to the integer division of x by n. It then prints this divisor for each test case. The function does not return any value; it only prints the results to the standard output.

