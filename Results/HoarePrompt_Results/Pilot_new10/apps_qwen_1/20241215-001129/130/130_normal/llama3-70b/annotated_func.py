#State of the program right berfore the function call: N, M, K, L are integers such that 1 <= K <= N <= 10^18, 1 <= M, L <= 10^18, and M * L >= K.
def func():
    N, M, K, L = map(int, input().split())
    if (M >= N - K + 1 and M >= L) :
        print(1)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`N`, `M`, `K`, and `L` are integers such that 1 <= `K` <= `N` <= 10^18, 1 <= `M`, `L` <= 10^18, and `M` * `L` >= `K`. If `M` is greater than or equal to `N - K + 1` and `M` is greater than or equal to `L`, the program prints '1'. Otherwise, the program prints '-1'.
#Overall this is what the function does:The function reads four integers `N`, `M`, `K`, and `L` from the input and prints `1` if `M` is greater than or equal to both `N - K + 1` and `L`. Otherwise, it prints `-1`.

