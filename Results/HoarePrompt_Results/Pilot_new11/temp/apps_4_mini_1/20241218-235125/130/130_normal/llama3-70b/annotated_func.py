#State of the program right berfore the function call: N, M, K, and L are positive integers such that 1 ≤ K ≤ N ≤ 10^18 and 1 ≤ M, L ≤ 10^18.
def func():
    N, M, K, L = map(int, input().split())
    if (M >= N - K + 1 and M >= L) :
        print(1)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`N`, `M`, `K`, and `L` are positive integers. If `M` is greater than or equal to `N - K + 1` and `M` is also greater than or equal to `L`, then the condition holds true. Otherwise, it is not the case that `M` meets these conditions.
#Overall this is what the function does:The function accepts four positive integers N, M, K, and L. It checks whether M is greater than or equal to both (N - K + 1) and L. If both conditions are satisfied, it prints 1, indicating that M meets the criteria. Otherwise, it prints -1, indicating that M does not meet the criteria. The function does not return any value; it only prints the result based on the evaluation of the conditions. Note that potential edge cases, such as what happens if M is on the boundary of the conditions or if any of the input parameters exceed expected values beyond given constraints, are not handled in the code.

