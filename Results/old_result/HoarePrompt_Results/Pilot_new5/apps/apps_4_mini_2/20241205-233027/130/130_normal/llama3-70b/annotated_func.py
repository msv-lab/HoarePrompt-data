#State of the program right berfore the function call: N, M, K, and L are integers such that 1 ≤ K ≤ N ≤ 10^18 and 1 ≤ M, L ≤ 10^18.
def func():
    N, M, K, L = map(int, input().split())
    if (M >= N - K + 1 and M >= L) :
        print(1)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`N`, `M`, `K`, `L` are integers such that 1 ≤ K ≤ N ≤ 10^18 and 1 ≤ M, L ≤ 10^18. If `M` is greater than or equal to `N - K + 1` and `M` is greater than or equal to `L`, then the integer 1 has been printed. Otherwise, it holds that `M` is less than `N - K + 1` or `M` is less than `L.
#Overall this is what the function does:The function reads four integers N, M, K, and L from input. It prints 1 if M is greater than or equal to both N - K + 1 and L, otherwise it prints -1. It does not accept any parameters.

