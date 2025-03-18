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
        
    #State: Output State: After all iterations of the loop have finished, `t` is a positive integer such that \(1 \leq t \leq 10^4\). For each iteration \(i\) from 0 to \(t-1\), the following conditions hold:
    #
    #- `n` and `m` are the integers read from the input for the \(i\)-th iteration.
    #- `k` is the absolute difference between `n` and `m`.
    #- `l` is the binary string representation of `k` without the '0b' prefix.
    #- `p` is the length of `l`.
    #- `q` is calculated based on whether `k` is a power of 2:
    #  - If `k` is a power of 2, then `q` is 2.
    #  - Otherwise, `q` is \(2^{(p - 1)}\).
    #- `i` is the current iteration index, which will be \(t-1\) after all iterations.
    #
    #The loop processes each of the `t` test cases, updating `k`, `l`, `p`, and `q` according to the conditions specified in the loop body. The final state after all iterations will reflect the last values of these variables for the last test case processed.
#Overall this is what the function does:The function processes up to 10,000 test cases, where each test case involves two distinct non-negative integers \(n\) and \(m\). It calculates the absolute difference \(k\) between \(n\) and \(m\), and based on certain conditions, prints one of the following values: \(k\), 1, 2, or \(k - q\), where \(q\) is derived from the binary representation of \(k\). After processing all test cases, the function does not return any value but outputs the results for each test case.

