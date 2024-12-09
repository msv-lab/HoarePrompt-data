#State of the program right berfore the function call: N, M, K, and L are all positive integers such that 1 ≤ K ≤ N and 1 ≤ M, L ≤ 10^18.
def func():
    input = sys.stdin.read
    N, M, K, L = map(int, input().split())
    min_x = (L + M - 1) // M
    if (M * min_x <= N - K) :
        print(min_x)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`N`, `M`, `K`, and `L` are positive integers such that 1 ≤ K ≤ N and 1 ≤ M, L ≤ 10^18. If `M * min_x` is less than or equal to `N - K`, then `min_x` is printed and is equal to `(L + M - 1) // M`. Otherwise, `min_x` is calculated as `(L + M - 1) // M` but it holds that `M * min_x` is greater than `N - K`.
#Overall this is what the function does:The function reads four positive integers `N`, `M`, `K`, and `L` from input, where `1 ≤ K ≤ N` and `1 ≤ M, L ≤ 10^18`. It calculates the minimum number of times `min_x` needed to cover at least `L` using increments of `M`. If the total amount `M * min_x` does not exceed `N - K`, it prints `min_x`; otherwise, it prints `-1`. The function does not handle cases where `M` or `L` are zero, nor does it validate the input constraints beyond assuming they are satisfied.

