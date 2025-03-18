#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each of the following t lines contains two distinct non-negative integers x and y such that 0 <= x, y <= 10^9 and x != y.
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
        
    #State: a sequence of printed values, one for each pair of integers (n, m), based on the conditions provided in the loop.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of two distinct non-negative integers `x` and `y`. For each pair, it calculates the absolute difference `k` between `x` and `y` and prints a value based on specific conditions: if `k` is a power of two, it prints `k`; if `x` is 0 and `y` is odd, it prints 1; if `x` is 0 and `y` is even, it prints 2; otherwise, it prints the difference between `k` and the largest power of two less than or equal to `k`.

