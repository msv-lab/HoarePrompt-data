#State of the program right berfore the function call: N, M, K, and L are positive integers such that 1 ≤ K ≤ N, 1 ≤ M, and 1 ≤ L, with constraints up to 10^18.
def func():
    input = sys.stdin.read
    N, M, K, L = map(int, input().split())
    min_x = (L + M - 1) // M
    if (M * min_x <= N - K) :
        print(min_x)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`N`, `M`, `K`, `L` are positive integers, and `min_x` is calculated as `(L + M - 1) // M`. If `M * min_x` is less than or equal to `N - K`, then the value of `min_x` is printed. Otherwise, `M * min_x` is greater than `N - K`.
#Overall this is what the function does:The function reads four positive integers `N`, `M`, `K`, and `L` from input, calculates `min_x`, which represents the minimum number of `M` units needed to meet or exceed `L`. If the product of `M` and `min_x` is less than or equal to `N - K`, it prints the value of `min_x`. Otherwise, it prints `-1`. This means that if the remaining units available (given by `N - K`) cannot accommodate the required units to meet `L`, the function correctly returns `-1`. The function does not explicitly return any value, it only prints the result.

