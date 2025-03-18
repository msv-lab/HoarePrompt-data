#State of the program right berfore the function call: N, M, K, and L are integers such that 1 <= K <= N <= 10^18, and 1 <= M, L <= 10^18.
def func():
    input = sys.stdin.read
    N, M, K, L = map(int, input().split())
    min_x = (L + M - 1) // M
    if (M * min_x <= N - K) :
        print(min_x)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`N`, `M`, `K`, and `L` are integers assigned from input values; `min_x` is equal to `(L + M - 1) // M`. If `M * min_x <= N - K`, the current value of `min_x` is printed. Otherwise, the condition `M * min_x > N - K` holds true.
#Overall this is what the function does:The function reads four integers (N, M, K, L) from standard input, which represent certain constraints. It calculates a value min_x, which is the minimum number of full M-sized pieces needed to reach or exceed L. If the product of M and min_x is less than or equal to the remaining capacity (N - K), it prints the value of min_x; otherwise, it prints -1. The final output reflects whether it's possible to fit the required pieces within the given constraints. Notably, the function does not return any value; it only prints results directly. Edge cases such as the condition where no pieces can be allocated due to insufficient remaining capacity (N - K) are handled, as the function correctly assesses and prints -1 when applicable.

