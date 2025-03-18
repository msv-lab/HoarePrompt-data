#State of the program right berfore the function call: x and y are distinct non-negative integers such that 0 ≤ x, y ≤ 10^9 and x ≠ y.
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
        
    #State: x and y remain distinct non-negative integers such that 0 ≤ x, y ≤ 10^9 and x ≠ y.
#Overall this is what the function does:The function `func` reads an integer from the user, which determines the number of iterations. For each iteration, it reads two integers `n` and `m` from the user. It then calculates the absolute difference `k` between `n` and `m`. If `k` is a power of two, it prints `k`. If `n` is 0 and `m` is odd, it prints 1. If `n` is 0 and `m` is even, it prints 2. Otherwise, it calculates the largest power of two less than or equal to `k` and prints the difference between `k` and this power of two. The function does not modify the input parameters `x` and `y` mentioned in the comments.

