#State of the program right berfore the function call: N, M, K, and L are positive integers where 1 ≤ K ≤ N ≤ 10^18, and 1 ≤ M, L ≤ 10^18.
def func():
    N, M, K, L = map(int, input().split())
    if (M >= N - K + 1 and M >= L) :
        print(1)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`N`, `M`, `K`, and `L` are positive integers. If `M` is greater than or equal to `N - K + 1` and `M` is greater than or equal to `L`, the function continues normally. Otherwise, if `M` is less than `N - K + 1` or `M` is less than `L`, `-1` is printed.
#Overall this is what the function does:The function accepts input of four positive integers N, M, K, and L from standard input. It checks if M is greater than or equal to N - K + 1 and M is also greater than or equal to L. If both conditions are satisfied, it prints 1; otherwise, it prints -1. There are no return values.

