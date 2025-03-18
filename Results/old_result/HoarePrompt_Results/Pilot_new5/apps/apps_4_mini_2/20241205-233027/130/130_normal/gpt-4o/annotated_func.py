#State of the program right berfore the function call: N, M, K, and L are integers such that 1 <= K <= N <= 10^18 and 1 <= M, L <= 10^18.
def func():
    input = sys.stdin.read
    N, M, K, L = map(int, input().split())
    min_x = (L + M - 1) // M
    if (M * min_x <= N - K) :
        print(min_x)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`N`, `K`, `M`, `L` are integers within specified ranges. If `M * min_x` is less than or equal to `N - K`, `min_x` is printed. Otherwise, if `M * min_x` is greater than `N - K`, the output is -1.
#Overall this is what the function does:The function reads four integers N, M, K, and L from input. It calculates the minimum number of units min_x required such that M multiplied by min_x does not exceed N minus K. If this condition is satisfied, it outputs min_x; otherwise, it outputs -1. The function does not return a value, but instead prints the result directly based on the conditions evaluated.

