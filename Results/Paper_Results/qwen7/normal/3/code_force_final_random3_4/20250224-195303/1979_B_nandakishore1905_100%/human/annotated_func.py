#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, x and y are distinct non-negative integers such that 0 ≤ x, y ≤ 10^9.
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
        
    #State: Output State: After the loop executes all iterations, `t` is a positive integer such that \(1 \leq t \leq 10^4\), `i` is the total number of test cases minus one, `n` is an input integer, `m` is an input integer, `k` is the absolute difference between `n` and `m`. If `k` is a power of 2, `f` is 0, `l` is the binary string representation of `k` without the '0b' prefix, and `p` is the length of `l`, `q` is 2. Otherwise, `f` is the highest power of 2 less than or equal to \(k - 2^p - 3 \cdot 2^{(p - 1)}\), `l` is the binary string representation of `f` without the '0b' prefix, `p` is the length of the binary string representation of `f` without the '0b' prefix, and `q` is \(2^{(p - 1)}\).
    #
    #This final state indicates that after processing all test cases, for each test case, if the absolute difference `k` between `n` and `m` is a power of 2, the output is `k`. Otherwise, it outputs the highest power of 2 less than or equal to `k - 2^p - 3 \cdot 2^{(p - 1)}`, where `p` is the length of the binary representation of `k`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers \(n\) and \(m\). For each test case, it calculates the absolute difference \(k\) between \(n\) and \(m\). If \(k\) is a power of 2, it prints \(k\). Otherwise, it finds the highest power of 2 less than or equal to \(k - 2^p - 3 \cdot 2^{(p - 1)}\), where \(p\) is the length of the binary representation of \(k\), and prints that value. The function does not return any value; instead, it prints the result for each test case.

