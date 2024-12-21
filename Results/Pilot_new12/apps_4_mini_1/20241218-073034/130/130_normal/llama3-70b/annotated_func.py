#State of the program right berfore the function call: N, M, K, and L are integers such that 1 ≤ K ≤ N ≤ 10^18 and 1 ≤ M, L ≤ 10^18.
def func():
    N, M, K, L = map(int, input().split())
    if (M >= N - K + 1 and M >= L) :
        print(1)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`N`, `M`, `K`, `L` are integers assigned new values from input such that 1 ≤ `K` ≤ `N` ≤ 10^18 and 1 ≤ `M`, `L` ≤ 10^18. If `M` is greater than or equal to `N - K + 1` and `M` is also greater than or equal to `L`, the function outputs 1. Otherwise, if the condition is not satisfied (implying that either `M` is less than `N - K + 1` or `M` is less than `L`), the function outputs -1.
#Overall this is what the function does:The function reads four integers N, M, K, and L from input, validates them within specified constraints (1 ≤ K ≤ N ≤ 10^18 and 1 ≤ M, L ≤ 10^18), and evaluates a condition based on the values of M, N, and K. If M is greater than or equal to N - K + 1 and also greater than or equal to L, the function outputs 1. If the condition is not satisfied, the function outputs -1. However, the function does not return any values or perform further actions beyond outputting the result as an integer, which indicates whether certain conditions on the input values are satisfied. Additionally, it should be noted that the function lacks error handling for invalid input forms, which could lead to unexpected behavior if non-integer inputs are provided.

