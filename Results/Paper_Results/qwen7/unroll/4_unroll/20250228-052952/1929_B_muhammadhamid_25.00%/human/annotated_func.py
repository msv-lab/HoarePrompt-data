#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are integers such that 2 ≤ n ≤ 10^8 and 1 ≤ k ≤ 4n - 2.
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
        
    #State: Output State: The output state will consist of a series of lines, each containing either `1`, `math.ceil(k / 2)`, or `k // 2 + 1`. The specific value on each line depends on the values of `n` and `k` provided for each test case within the range specified. For each test case, if `k` equals 1, the output will be `1`. If `k` is less than or equal to `2 * n`, the output will be `math.ceil(k / 2)`. Otherwise, the output will be `k // 2 + 1`.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \( t \), \( n \), and \( k \). For each test case, it prints one of three possible values based on the relationship between \( n \) and \( k \): 1, \(\lceil k / 2 \rceil\), or \( k // 2 + 1 \). If \( k \) equals 1, it prints 1. If \( k \) is less than or equal to \( 2n \), it prints \(\lceil k / 2 \rceil\). Otherwise, it prints \( k // 2 + 1 \). The function does not return any value but outputs these results for each test case.

