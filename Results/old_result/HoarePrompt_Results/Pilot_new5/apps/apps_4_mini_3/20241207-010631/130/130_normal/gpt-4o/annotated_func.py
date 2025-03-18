#State of the program right berfore the function call: N, M, K, and L are integers such that 1 <= K <= N <= 10^18 and 1 <= M, L <= 10^18.
def func():
    input = sys.stdin.read
    N, M, K, L = map(int, input().split())
    min_x = (L + M - 1) // M
    if (M * min_x <= N - K) :
        print(min_x)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`N`, `M`, `K`, and `L` are integers. If `M * min_x` is less than or equal to `N - K`, then `min_x` is printed. Otherwise, `M * min_x` is greater than `N - K`, and -1 is printed.
#Overall this is what the function does:The function reads four integers N, M, K, and L from input and calculates the minimum integer x such that M * x is less than or equal to N - K. If such an x exists, it prints the value of x; otherwise, it prints -1. The function does not return any value. It handles cases where the computed minimum x might not fit within the constraints of the inputs, leading to a possible output of -1 when the conditions are not met.

