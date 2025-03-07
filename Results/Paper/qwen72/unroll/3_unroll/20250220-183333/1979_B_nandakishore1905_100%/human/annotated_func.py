#State of the program right berfore the function call: x and y are distinct non-negative integers such that 0 <= x, y <= 10^9 and x ≠ y.
def func():
    for i in range(int(input())):
        n, m = map(int, input().split())
        
        k = abs(n - m)
        
        if k & k - 1 == 0:
            print(k)
        elif k % 2 != 0:
            print(1)
        else:
            l = bin(k).replace('0b', '')
            p = len(l)
            q = 2 ** (p - 1)
            f = k - q
            while f & f - 1 != 0:
                l = bin(f).replace('0b', '')
                p = len(l)
                q = 2 ** (p - 1)
                f = f - q
            print(f)
        
    #State: The values of x and y remain unchanged as they are not modified within the loop. The loop processes inputs n and m, and for each iteration, it prints a value based on the conditions specified in the loop body. The loop does not alter the initial state of x and y.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. Instead, it reads an integer from the user, which determines the number of iterations. For each iteration, it reads a pair of integers `n` and `m` from the user, computes the absolute difference `k` between them, and prints a value based on the following conditions: if `k` is a power of 2, it prints `k`; if `k` is odd, it prints `1`; otherwise, it prints the largest power of 2 that is less than or equal to `k` after subtracting all smaller powers of 2 from `k`. The function does not modify any external variables or the initial state of the program.

