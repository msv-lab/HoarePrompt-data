#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are integers such that 2 ≤ n ≤ 10^8 and 1 ≤ k ≤ 4n - 2.
def func():
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        if k <= 4 * n - 4:
            print(math.ceil(k / 2))
        elif k == 4 * n - 3:
            print(2 * n - 1)
        elif k == 4 * n - 2:
            print(2 * n)
        
    #State: Output State: The output state consists of a series of lines, each containing an integer result based on the value of `k` relative to `n`. For each test case, if `k` is less than or equal to `4 * n - 4`, the output is `math.ceil(k / 2)`. If `k` equals `4 * n - 3`, the output is `2 * n - 1`. If `k` equals `4 * n - 2`, the output is `2 * n`. The number of lines in the output state is equal to the number of test cases provided in the input.
#Overall this is what the function does:The function processes a series of test cases, each defined by integers \( n \) and \( k \). For each test case, it calculates and prints a specific integer value based on the relationship between \( k \) and \( 4n - 2 \). If \( k \leq 4n - 4 \), it prints \( \lceil k / 2 \rceil \). If \( k = 4n - 3 \), it prints \( 2n - 1 \). If \( k = 4n - 2 \), it prints \( 2n \). The function reads these values from standard input and outputs the results to standard output, with one line per test case.

