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
        
    #State: `x` and `y` are distinct non-negative integers such that \(0 \leq x, y \leq 10^9\) and \(x \neq y\), `i` is the number of iterations specified by the user input, `n` and `m` are the last input integers greater than 0, `k` is the absolute difference between `n` and `m`. If `k` is a power of 2, no changes are made to the variables. If `k` is odd, no changes are made to the variables. If `k` is even and not a power of 2, `l` is the binary representation of `f` without the '0b' prefix, `p` is the number of digits in the binary representation of `f`, `q` is \(2^{(p - 1)}\), and `f` is 0.
#Overall this is what the function does:The function reads a number of iterations from the user, and for each iteration, it reads two integers `n` and `m`. It then calculates the absolute difference `k` between `n` and `m`. If `k` is a power of 2, it prints `k`. If `k` is odd, it prints 1. If `k` is even and not a power of 2, it performs a series of operations to reduce `k` to the largest power of 2 less than or equal to `k` and prints the result of this reduction. The function does not return any value; it only prints the results for each iteration. After the function concludes, the input variables `x` and `y` remain unchanged, and the final state of the program is determined by the last values of `n`, `m`, and `k` processed in the loop.

