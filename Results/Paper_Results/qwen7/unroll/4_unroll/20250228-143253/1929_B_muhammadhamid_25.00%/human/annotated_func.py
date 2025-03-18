#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, and for each test case, n and k are integers such that 2 <= n <= 10^8 and 1 <= k <= 4n - 2.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        if k == 1:
            print(1)
            continue
        
        if k <= 2 * n:
            print(math.ceil(k / 2))
        else:
            print(k // 2 + 1)
        
    #State: Output State: The output state consists of a series of lines, each containing either `1`, `math.ceil(k / 2)`, or `k // 2 + 1`, depending on the values of `n` and `k` for each test case. For each test case, if `k` equals 1, the output is `1`. If `k` is less than or equal to `2 * n`, the output is `math.ceil(k / 2)`. Otherwise, the output is `k // 2 + 1`. The number of lines in the output state corresponds to the number of test cases provided as input.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \( n \) and \( k \). For each test case, it prints either 1, \(\lceil \frac{k}{2} \rceil\), or \(\frac{k}{2} + 1\) based on the value of \( k \) relative to \( n \). Specifically, if \( k \) is 1, it prints 1. If \( k \) is less than or equal to \( 2n \), it prints \(\lceil \frac{k}{2} \rceil\). Otherwise, it prints \(\frac{k}{2} + 1\). The function does not return any value but outputs these results for each test case.

