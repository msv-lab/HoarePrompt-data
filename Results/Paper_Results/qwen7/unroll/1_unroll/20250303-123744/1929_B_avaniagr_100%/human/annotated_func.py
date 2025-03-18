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
        
    #State: Output State: The output state will consist of a series of lines, each containing either `math.ceil(k / 2)`, `2 * n - 1`, or `2 * n`. The specific value on each line depends on the values of `n` and `k` for each test case. If `k` is less than or equal to `4 * n - 4`, it prints `math.ceil(k / 2)`. If `k` is exactly `4 * n - 3`, it prints `2 * n - 1`. If `k` is exactly `4 * n - 2`, it prints `2 * n`.
#Overall this is what the function does:The function processes a series of test cases, each defined by integers \( n \) and \( k \). For each test case, it calculates and prints one of three possible values based on the relationship between \( n \) and \( k \): \( \text{math.ceil}(k / 2) \), \( 2n - 1 \), or \( 2n \). The function reads these values from standard input, processes them according to the given conditions, and outputs the results to standard output.

