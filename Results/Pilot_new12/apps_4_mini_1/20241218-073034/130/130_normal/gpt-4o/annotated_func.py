#State of the program right berfore the function call: N, M, K, and L are integers such that 1 ≤ K ≤ N ≤ 10^18 and 1 ≤ M, L ≤ 10^18.
def func():
    input = sys.stdin.read
    N, M, K, L = map(int, input().split())
    min_x = (L + M - 1) // M
    if (M * min_x <= N - K) :
        print(min_x)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`N`, `K`, `M`, and `L` are integers where `L` and `M` are in the range of 1 to 10^18. If `M * min_x` is less than or equal to `N - K`, then `min_x` is printed. Otherwise, if `M * min_x` is greater than `N - K`, the function outputs -1.
#Overall this is what the function does:The function reads four integers, N, M, K, and L, from standard input, ensuring that 1 ≤ K ≤ N ≤ 10^18 and 1 ≤ M, L ≤ 10^18. It calculates the minimum number of complete units, `min_x`, that can be obtained from L using a rate of M (specifically, `min_x = (L + M - 1) // M`), which is the ceiling of L / M. The function then checks if M multiplied by `min_x` can be accommodated within the remaining value of N minus K. If it can, it prints `min_x`. If it cannot, it prints -1. Thus, the final program state includes integers N, K, M, and L remaining unchanged, while the output will be either the computed `min_x` or -1 based on the comparison. The function does not return any values, but rather prints its result directly. It should be noted that no error handling exists for the input, so if the input values do not conform to the specified constraints, the function will still attempt to compute and print a result.

