#State of the program right berfore the function call: N, M, K, and L are integers such that 1 <= K <= N and 1 <= M, L, and 1 <= L <= N - K, and N, M, K, L >= 0 and N, M, K, L are within the range of 1 to 10^18.
def func():
    N, M, K, L = map(int, input().split())
    if (M >= N - K + 1 and M >= L) :
        print(1)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: `N`, `M`, `K`, `L` are integers, where `N`, `M`, `K`, `L` are input integers. If `M` is greater than or equal to `N - K + 1` and `M` is greater than or equal to `L`, then the value 1 has been printed. Otherwise, the condition `(M >= N - K + 1 and M >= L)` is false and the value -1 has been returned.
#Overall this is what the function does:The function reads four integers N, M, K, and L from user input, checks if the conditions M >= N - K + 1 and M >= L are met, and prints 1 if both conditions are true; otherwise, it prints -1. The function does not return any value but modifies the program's output based on the input integers. After execution, the program's state is determined by the printed value, which is either 1, indicating that the input conditions are satisfied, or -1, indicating that the conditions are not met. The function's operation is based on the constraints of the input integers, but it does not validate these constraints beyond what is specified in the conditional statement. The function's functionality implicitly assumes that the input integers are within the specified ranges (1 <= K <= N, 1 <= M, L, and 1 <= L <= N - K, and N, M, K, L >= 0), but it does not explicitly enforce these constraints.

