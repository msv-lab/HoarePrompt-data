#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, x and y are distinct non-negative integers such that 0 <= x, y <= 10^9.
def func():
    for i in range(int(input())):
        n, m = map(int, input().split())
        
        k = abs(n - m)
        
        if k & k - 1 == 0:
            print(k)
        elif n == 0 and m % 2 != 0:
            print(1)
        elif n == 0 and m % 2 == 0:
            print(2)
        else:
            l = bin(k).replace('0b', '')
            p = len(l)
            q = 2 ** (p - 1)
            print(k - q)
        
    #State: The loop will have printed a value for each of the `t` test cases, based on the conditions specified in the loop.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of two distinct non-negative integers `n` and `m`. For each test case, it calculates the absolute difference `k` between `n` and `m` and prints a specific value based on certain conditions: if `k` is a power of two, it prints `k`; if `n` is 0 and `m` is odd, it prints 1; if `n` is 0 and `m` is even, it prints 2; otherwise, it prints `k` minus the largest power of two less than or equal to `k`.

