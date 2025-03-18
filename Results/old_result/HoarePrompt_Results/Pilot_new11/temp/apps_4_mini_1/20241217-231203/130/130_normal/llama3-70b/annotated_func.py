#State of the program right berfore the function call: N, M, K, and L are positive integers such that 1 <= K <= N, 1 <= M, and 1 <= L; N, M, K, and L can be as large as 10^18.
def func():
    N, M, K, L = map(int, input().split())
    if (M >= N - K + 1 and M >= L) :
        print(1)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`N`, `M`, `K`, and `L` are positive integers such that 1 <= `K` <= `N`, 1 <= `M`, and 1 <= `L`. If `M` is greater than or equal to `N - K + 1` and `M` is greater than or equal to `L`, then the function continues its execution normally. Otherwise, -1 has been printed to the console.
#Overall this is what the function does:The function reads four positive integers, N, M, K, and L, from user input. It checks if M is greater than or equal to both N - K + 1 and L. If this condition is met, it outputs 1 to the console; otherwise, it outputs -1. N, M, K, and L must satisfy the constraints 1 <= K <= N, 1 <= M, and 1 <= L, with potential values for these variables as large as 10^18. The function does not return a value but prints output based on the conditional check. There is missing functionality in the sense that the function lacks error handling for invalid inputs or scenarios where constraints might not be met, which could lead to runtime errors. Additionally, the function does not provide any other means of communicating results other than the printed output.

