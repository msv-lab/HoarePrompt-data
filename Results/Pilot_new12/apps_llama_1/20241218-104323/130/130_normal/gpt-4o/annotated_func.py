#State of the program right berfore the function call: N, M, K, and L are integers, where 1 <= K <= N, 1 <= M, 1 <= L, and 1 <= K <= 10^18, 1 <= M <= 10^18, and 1 <= L <= 10^18.
def func():
    input = sys.stdin.read
    N, M, K, L = map(int, input().split())
    min_x = (L + M - 1) // M
    if (M * min_x <= N - K) :
        print(min_x)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`N` is an input integer, `M` is an input integer, `K` is an input integer with `1 <= K <= N`, `L` is an input integer, and `min_x` equals `(L + M - 1) // M`. If `M * min_x <= N - K`, the value of `min_x` has been printed. Otherwise, the value -1 has been returned as output, indicating `M * min_x > N - K`.
#Overall this is what the function does:The function calculates and returns the minimum number of items (`min_x`) that need to be added to a set of `N` items, given `M` items can be added at a time, `K` items are reserved and cannot be removed, and `L` items are required in total. It takes four integer parameters: `N`, `M`, `K`, and `L`, where `1 <= K <= N`, `1 <= M`, `1 <= L`, and `1 <= K, M, L <= 10^18`. If the minimum number of items to add (`min_x`) does not exceed the available space (`N - K`), the function prints the value of `min_x`. Otherwise, it prints `-1`, indicating that there is not enough space to add the required number of items. The function assumes that the input values are provided through standard input, separated by spaces. The program state after execution will have either the minimum number of items to add or `-1` printed to the output, depending on whether the required items can fit within the available space.

