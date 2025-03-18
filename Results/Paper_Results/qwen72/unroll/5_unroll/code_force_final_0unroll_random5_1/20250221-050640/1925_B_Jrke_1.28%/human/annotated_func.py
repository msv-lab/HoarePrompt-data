#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^3, x is a positive integer such that 1 <= x <= 10^8, and n is a positive integer such that 1 <= n <= x.
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
        
    #State: t is a positive integer such that 1 <= t <= 10^3, x is a positive integer such that 1 <= x <= 10^8, and n is a positive integer such that 1 <= n <= x. The loop prints the largest odd divisor of x that is less than or equal to k for each iteration, where k = x // n. If k == 1, it prints 1.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads two positive integers `x` and `n` from the input. The function then calculates the largest odd divisor of `x` that is less than or equal to `k`, where `k = x // n`. If `k` is 1, it prints 1. Otherwise, it prints the largest odd divisor found. The function performs this operation for each of the `t` test cases.

