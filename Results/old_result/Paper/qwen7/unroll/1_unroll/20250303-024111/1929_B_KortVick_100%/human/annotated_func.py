#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are integers such that 2 ≤ n ≤ 10^8 and 1 ≤ k ≤ 4n - 2.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        if 4 * n - 2 == k:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))
        
    #State: Output State: The output state will consist of a series of lines, each containing either the result of `k // 2 + 1` or `ceil(k / 2)`, depending on whether `4 * n - 2` equals `k` for each iteration of the loop. The number of lines will be equal to the value of `t`, which is a positive integer between 1 and 1000 (inclusive). Each line's content depends on the specific values of `n` and `k` provided in the input for that iteration.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers \( n \) and \( k \). For each test case, it checks if \( 4n - 2 \) equals \( k \). If true, it prints \( \frac{k}{2} + 1 \); otherwise, it prints \( \lceil \frac{k}{2} \rceil \). The function reads these test cases from standard input and outputs the results to standard output, with the number of outputs equal to the value of \( t \), which is a positive integer between 1 and 1000.

