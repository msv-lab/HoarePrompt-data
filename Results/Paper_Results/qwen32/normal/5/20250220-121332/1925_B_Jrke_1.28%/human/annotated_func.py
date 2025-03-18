#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^3. For each test case, x and n are integers such that 1 <= x <= 10^8 and 1 <= n <= x.
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
        
    #State: After all iterations, for each test case provided by the input, the output is the largest divisor of `x` that is less than or equal to `k`, where `k` is the integer division of `x` by `n`.
#Overall this is what the function does:For each of the `t` test cases, the function takes two integers `x` and `n` as input, with `1 <= n <= x` and `1 <= x <= 10^8`. It calculates the largest divisor of `x` that is less than or equal to the integer division of `x` by `n` and prints this value for each test case.

