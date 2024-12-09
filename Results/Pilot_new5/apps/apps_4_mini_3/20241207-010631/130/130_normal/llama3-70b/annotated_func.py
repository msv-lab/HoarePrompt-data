#State of the program right berfore the function call: N, M, K, and L are positive integers where 1 <= K <= N <= 10^18, and 1 <= M, L <= 10^18.
def func():
    N, M, K, L = map(int, input().split())
    if (M >= N - K + 1 and M >= L) :
        print(1)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`N`, `M`, `K`, and `L` are integers where 1 <= `K` <= `N` <= 10^18 and 1 <= `M`, `L` <= 10^18. If `M` is greater than or equal to `N - K + 1` and also greater than or equal to `L`, then the function executes normally. Otherwise, if `M` is less than `N - K + 1` or `M` is less than `L`, the function returns -1.
#Overall this is what the function does:The function accepts four positive integers (N, M, K, L) from user input and checks if M is greater than or equal to both (N - K + 1) and L. If both conditions are met, it prints 1; otherwise, it prints -1. The function does not return any values but outputs the result directly.

