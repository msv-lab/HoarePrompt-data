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
        
    #State: After processing all test cases, the maximum factors for each test case have been printed, and the values of `x` and `n` are as per the last test case processed. The value of `t` remains unchanged.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `x` and `n` (where `1 <= n <= x`). For each test case, it calculates and prints the largest factor of `x` that is less than or equal to `n`.

