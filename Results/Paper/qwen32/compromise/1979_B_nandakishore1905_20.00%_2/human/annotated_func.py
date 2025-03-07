#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each of the t test cases, x and y are distinct non-negative integers such that 0 <= x, y <= 10^9.
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
        
    #State: The output state consists of `t` lines, each containing the result of the corresponding test case based on the provided conditions.
#Overall this is what the function does:The function processes `t` test cases, each consisting of two distinct non-negative integers `n` and `m`. For each test case, it calculates the absolute difference `k` between `n` and `m`, and then determines the output based on specific conditions related to the value of `k` and the values of `n` and `m`. The output for each test case is printed on a new line.

