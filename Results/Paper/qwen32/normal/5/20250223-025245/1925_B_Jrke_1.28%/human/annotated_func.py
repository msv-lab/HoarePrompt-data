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
        
    #State: t is an integer such that 1 <= t <= 10^3, and for each of the t test cases, the maximum divisor of x that is less than or equal to k (where k = x // n) has been printed.
#Overall this is what the function does:The function processes `t` test cases, each consisting of two integers `x` and `n`. For each test case, it calculates the maximum divisor of `x` that is less than or equal to `x // n` and prints this value.

