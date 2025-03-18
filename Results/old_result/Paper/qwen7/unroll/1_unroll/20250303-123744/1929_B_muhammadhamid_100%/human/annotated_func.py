#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, and for each test case, n and k are integers such that 2 <= n <= 10^8 and 1 <= k <= 4n - 2.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        if k == 1:
            print(1)
            continue
        
        if k <= 2 * (n + (n - 2)):
            print(math.ceil(k / 2))
        else:
            print(k // 2 + 1)
        
    #State: Output State: The output state will consist of a series of lines, each containing either `1`, `math.ceil(k / 2)`, or `k // 2 + 1`. The specific value on each line depends on the values of `n` and `k` provided for each test case. For each test case, if `k` equals 1, the output will be `1`. Otherwise, if `k` is less than or equal to `2 * (n + (n - 2))`, the output will be `math.ceil(k / 2)`. If `k` exceeds this value, the output will be `k // 2 + 1`.
#Overall this is what the function does:The function processes a series of test cases, each defined by integers \( n \) and \( k \). For each test case, it calculates and prints a value based on the given conditions. If \( k \) is 1, it prints 1. If \( k \) is less than or equal to \( 2 \times (n + (n - 2)) \), it prints \( \lceil \frac{k}{2} \rceil \). Otherwise, it prints \( \frac{k}{2} + 1 \). The function reads the number of test cases from the first input, followed by pairs of \( n \) and \( k \) for each test case.

