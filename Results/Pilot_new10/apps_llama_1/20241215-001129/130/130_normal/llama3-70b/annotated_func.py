#State of the program right berfore the function call: N, M, K, and L are integers such that 1 <= K <= N and 1 <= M, L, and 1 <= L <= N - K, and 1 <= M <= N.
def func():
    N, M, K, L = map(int, input().split())
    if (M >= N - K + 1 and M >= L) :
        print(1)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: `N`, `M`, `K`, and `L` are integers where their values are determined by the user's input, if `M` is greater than or equal to `N - K + 1` and `M` is greater than or equal to `L`, then the value 1 has been printed, otherwise, the value -1 is returned at the output.
#Overall this is what the function does:The function reads four integers `N`, `M`, `K`, and `L` from the user, checks if `M` is greater than or equal to both `N - K + 1` and `L`, and prints `1` if the condition is true, otherwise prints `-1`, without enforcing any specific constraints on the input values internally.

