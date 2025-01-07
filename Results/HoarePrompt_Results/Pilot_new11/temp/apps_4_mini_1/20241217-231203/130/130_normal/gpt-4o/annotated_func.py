#State of the program right berfore the function call: N, M, K, and L are positive integers such that 1 ≤ K ≤ N ≤ 10^18 and 1 ≤ M, L ≤ 10^18.
def func():
    input = sys.stdin.read
    N, M, K, L = map(int, input().split())
    min_x = (L + M - 1) // M
    if (M * min_x <= N - K) :
        print(min_x)
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`N`, `M`, `K`, and `L` are new positive integer values. If `M * min_x` is less than or equal to `N - K`, then `min_x`, calculated as `(L + M - 1) // M`, is printed. Otherwise, `min_x` is calculated and it is determined that `M * min_x` is greater than or equal to `N - K`, resulting in an output of -1.
#Overall this is what the function does:The function reads four positive integers, N, M, K, and L from the standard input, which must adhere to the constraints 1 ≤ K ≤ N ≤ 10^18 and 1 ≤ M, L ≤ 10^18. It calculates the minimum number of groups, `min_x`, required to satisfy the condition that the total quantity represented by L can be divided among M without exceeding the available resource of N minus K. If `M * min_x` (the required total) does not exceed `N - K`, it prints `min_x`. Otherwise, it prints -1, indicating that it is not possible to allocate the resources as required. After execution, the state of the program includes the variables N, M, K, and L remaining unchanged, but min_x being either a calculated number or the value -1 based on the conditions. Edge cases such as maximum allowable values for these integers and scenarios where L is 0 or less than M are not directly handled, potentially leading to incorrect assertions about feasibility.

