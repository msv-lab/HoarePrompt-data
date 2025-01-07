#State of the program right berfore the function call: N, M, K, and L are positive integers such that 1 <= K <= N <= 10^18, and 1 <= M, L <= 10^18.
def func():
    N, M, K, L = map(int, input().split())
    if (M >= N - K + 1 and M >= L) :
        print(1)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`N`, `M`, `K`, and `L` are positive integers such that 1 <= K <= N. If `M` is greater than or equal to `N - K + 1` and `M` is greater than or equal to `L`, the output is 1. Otherwise, if `M` is less than `N - K + 1` or `M` is less than `L`, the output is -1.
#Overall this is what the function does:The function accepts four positive integers N, M, K, and L as input. It checks if M is greater than or equal to both (N - K + 1) and L. If both conditions are satisfied, it outputs 1; otherwise, it outputs -1. There are no return statements, and the function operates solely by printing the output based on the condition checks.

