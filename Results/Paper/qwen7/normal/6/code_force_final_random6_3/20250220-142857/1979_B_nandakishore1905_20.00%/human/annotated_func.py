#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, x and y are distinct non-negative integers such that 0 ≤ x, y ≤ 10^9.
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
        
    #State: Output State: The loop will execute exactly `t` times, where `t` is the initial positive integer input. For each iteration `i` from 0 to `t-1`, the following process occurs:
    #
    #1. Two integers `n` and `m` are read as input.
    #2. `k` is calculated as the absolute difference between `n` and `m`.
    #3. If `k` is a power of 2, `k` is printed.
    #4. If `k` is not a power of 2, and `n` is 0 and `m` is odd, then 1 is printed.
    #5. If `k` is not a power of 2, and `n` is 0 and `m` is even, then 2 is printed.
    #6. If none of the above conditions are met, `l` is the binary string representation of `k` without the '0b' prefix, `p` is the length of `l`, and `q` is \(2^{(p - 1)}\). Then, `k - q` is printed.
    #
    #After all iterations, the final values of `n`, `m`, `k`, `i`, `l`, `p`, and `q` will depend on the inputs provided for each iteration, but the loop will have completed its execution, and `i` will be equal to `t-1`. The specific values of `n`, `m`, `k`, `l`, `p`, and `q` will be determined by the last set of inputs processed by the loop.
#Overall this is what the function does:The function processes a series of test cases, each defined by a positive integer `t` (1 ≤ t ≤ 10^4) and two distinct non-negative integers `n` and `m` (0 ≤ n, m ≤ 10^9). For each test case, it calculates the absolute difference `k` between `n` and `m`. Based on the value of `k`, it prints one of the following:
- If `k` is a power of 2, it prints `k`.
- If `k` is not a power of 2, and `n` is 0 and `m` is odd, it prints 1.
- If `k` is not a power of 2, and `n` is 0 and `m` is even, it prints 2.
- Otherwise, it calculates `q` as \(2^{(p - 1)}\) where `p` is the length of the binary representation of `k`, and prints `k - q`.

After processing all `t` test cases, the function completes, and the final output consists of `t` printed values corresponding to each test case.

