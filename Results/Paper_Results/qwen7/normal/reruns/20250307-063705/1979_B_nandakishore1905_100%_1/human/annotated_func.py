#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, and for each test case, x and y are distinct non-negative integers such that 0 <= x, y <= 10^9.
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
        
    #State: Output State: After the loop executes all its iterations, `t` is a positive integer such that \(1 \leq t \leq 10^4\). For each test case, `n` and `m` are distinct non-negative integers such that \(0 \leq n, m \leq 10^9\), and `k` is the absolute difference between `n` and `m`.
    #
    #If `k` is a power of 2, it will be printed as is. If `k` is odd, it will also be printed as is. If `k` is even but not a power of 2, the loop will reduce `k` to 0 by subtracting the highest power of 2 less than `k` repeatedly until `k` becomes 0. In the end, the value of `k` printed will be 0.
    #
    #The variable `i` will be equal to the total number of iterations, which is `t`. The variables `l`, `p`, `q`, and `f` will be irrelevant to the final output since they are used during the reduction process and reset or become 0 after the loop completes.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two distinct non-negative integers \(n\) and \(m\). For each test case, it calculates the absolute difference \(k\) between \(n\) and \(m\). If \(k\) is a power of 2 or odd, it prints \(k\) directly. If \(k\) is even and not a power of 2, it repeatedly subtracts the highest power of 2 less than \(k\) until \(k\) becomes 0. Finally, it prints 0. The function does not return any value but prints the result for each test case.

