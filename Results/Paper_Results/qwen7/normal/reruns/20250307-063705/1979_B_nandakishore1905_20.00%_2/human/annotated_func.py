#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, and for each test case, x and y are distinct non-negative integers such that 0 <= x, y <= 10^9.
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
        
    #State: Postcondition: `t` is a positive integer such that \(1 \leq t \leq 10^4\), `i` is equal to `t-1`, `n` and `m` are the last two input integers processed in the loop, `k` is the absolute value of `n - m`. If `k` is a power of 2 (i.e., `k & k - 1 == 0`), then `l`, `p`, and `q` retain their original values from the last iteration. Otherwise, if `n` is 0 and `m` is odd, `l` is the binary string representation of `k` without the '0b' prefix, `p` is the length of `l`, and `q` is 2.
#Overall this is what the function does:The function processes a series of test cases, each containing two distinct non-negative integers \(n\) and \(m\). For each pair, it calculates the absolute difference \(k = |n - m|\) and then prints one of four possible values based on the properties of \(k\): if \(k\) is a power of 2, it prints \(k\); if \(n\) is 0 and \(m\) is odd, it prints 1; if \(n\) is 0 and \(m\) is even, it prints 2; otherwise, it prints \(k - 2^{p-1}\), where \(p\) is the number of bits in the binary representation of \(k\).

