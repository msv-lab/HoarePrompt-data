#State of the program right berfore the function call: x and y are distinct non-negative integers such that 0 <= x, y <= 10^9.
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
        
    #State: `x` and `y` are distinct non-negative integers such that \(0 \leq x, y \leq 10^9\), `i` is the number of iterations specified by the user input, `n` and `m` are the last input integers greater than 0, `k` is the absolute difference between `n` and `m`. If `k` is a power of 2, `l` is the binary representation of `k` without the '0b' prefix, `p` is the number of bits in this binary representation, and `q` is \(2^{(p - 1)}\). If `k` is even and not a power of 2, `l` is the binary representation of the largest power of 2 less than or equal to `k` without the '0b' prefix, `p` is the number of bits in this binary representation, and `q` is \(2^{(p - 1)}\). If `k` is odd, no changes are made to `k`.
#Overall this is what the function does:The function `func` reads a number of iterations from the user, then for each iteration, it reads two distinct non-negative integers `n` and `m` from the user. It calculates the absolute difference `k` between `n` and `m`. If `k` is a power of 2, it prints `k`. If `k` is odd, it prints `1`. If `k` is even but not a power of 2, it prints the largest power of 2 that can be obtained by subtracting powers of 2 from `k` until the result is a power of 2. The function does not return any value. After the function concludes, the program state includes the number of iterations specified by the user, the last input integers `n` and `m`, and the final value of `k` which is the absolute difference between `n` and `m`.

