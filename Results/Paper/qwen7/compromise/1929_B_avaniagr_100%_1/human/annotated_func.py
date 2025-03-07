#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, and for each test case, n and k are integers such that 2 <= n <= 10^8 and 1 <= k <= 4n - 2.
def func():
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        if k <= 4 * n - 4:
            print(math.ceil(k / 2))
        elif k == 4 * n - 3:
            print(2 * n - 1)
        elif k == 4 * n - 2:
            print(2 * n)
        
    #State: Output State: The output state consists of a series of lines, each containing either `math.ceil(k / 2)`, `2 * n - 1`, or `2 * n`. For each line, the value depends on the specific values of `n` and `k` provided in the input. If `k` is less than or equal to `4 * n - 4`, the output is `math.ceil(k / 2)`. If `k` is exactly `4 * n - 3`, the output is `2 * n - 1`. If `k` is exactly `4 * n - 2`, the output is `2 * n`.
#Overall this is what the function does:Functionality: The function processes multiple test cases, each defined by integers \( n \) and \( k \). It reads these values from standard input, calculates a specific output based on the relationship between \( n \) and \( k \), and prints the result for each test case. Specifically, if \( k \leq 4n - 4 \), it prints \( \lceil k / 2 \rceil \); if \( k = 4n - 3 \), it prints \( 2n - 1 \); and if \( k = 4n - 2 \), it prints \( 2n \). The function does not return any value but outputs a series of lines, each containing one of the calculated results.

