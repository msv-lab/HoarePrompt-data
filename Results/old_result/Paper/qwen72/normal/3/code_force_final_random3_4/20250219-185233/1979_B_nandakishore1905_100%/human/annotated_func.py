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
        
    #State: `x` and `y` are distinct non-negative integers such that \(0 \leq x, y \leq 10^9\), `i` is the number of iterations specified by the input, `n` and `m` are the last input integers greater than 0, `k` is the absolute difference between `n` and `m`. If `k` is a power of two, `l` is "0", `p` is 1, `q` is 1, and `f` is 0. If `k` is odd, no additional changes are made. If `k` is even and not a power of two, `l` is the binary representation of `f` without the '0b' prefix, `p` is the length of `l`, `q` is \(2^{(p - 1)}\), and `f` is 0.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any values. It reads a number of iterations from the user, and for each iteration, it reads two integers `n` and `m`. It calculates the absolute difference `k` between `n` and `m`. If `k` is a power of two, it prints `k`. If `k` is odd, it prints `1`. If `k` is even and not a power of two, it performs a series of operations to reduce `k` to a smaller value and prints the final result. The function affects the state of the program by modifying local variables `i`, `n`, `m`, `k`, `l`, `p`, `q`, and `f` during its execution, but these changes do not persist outside the function.

