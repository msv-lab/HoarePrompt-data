#State of the program right berfore the function call: t is a positive integer; for each test case, n and q are positive integers such that 1 ≤ n, q ≤ 3 × 10^5; c is a list of n positive integers where 1 ≤ c_i ≤ 10^9; for each query, l_i and r_i are positive integers such that 1 ≤ l_i ≤ r_i ≤ n.
def func_1():
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: Output State: `i` is equal to `n`, `x` is 1 or 2 based on the value of `a[i]`, `b[1]` is 2, `b[2]` is 3, ..., `b[n]` is either 3 or 4, depending on the value of `a[i]`, `n` is greater than or equal to 3, `a[i]` is greater than 1 for all `i` from 1 to `n`.
    #
    #This means that after the loop has executed all its iterations, the variable `i` will be equal to `n`, indicating that the loop has completed all its iterations. The variable `x` will be either 1 or 2, depending on whether `a[i]` is greater than 1 or not. The list `b` will have been updated such that each element `b[i]` (for `i` from 1 to `n`) will be 3 if `a[i]` is greater than 1, or 4 if `a[i]` is not greater than 1. The conditions that `n` must be at least 3 and that `a[i]` must be greater than 1 for all `i` from 1 to `n` must still hold.
    a = list(accumulate(a))
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: Output State: The value of `x` and `y` will be determined by the inputs provided during each iteration of the loop. After all iterations of the loop have finished, the variables `x` and `y` will hold the values from the last input provided to the loop. For each input pair `(x, y)`, the program will print 'NO' if `a[y] - a[x - 1] < b[y] - b[x - 1]` or if `x == y`, otherwise it will print 'YES'. The final output state will reflect the results of all these comparisons.
    #
    #In more detail, after the loop has executed all its iterations, `x` and `y` will be set to the values of the last input pair provided to the loop. The program will have printed 'NO' or 'YES' for each input pair based on the condition `a[y] - a[x - 1] >= b[y] - b[x - 1]` and `x != y`.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads two integers \( n \) and \( q \), followed by a list \( a \) of \( n \) positive integers. It then handles \( q \) queries, each consisting of two integers \( x \) and \( y \). Based on the values in the list \( a \), the function compares the sums of subarrays defined by the queries and prints 'YES' if the sum of the subarray from index \( x \) to \( y \) in list \( a \) is greater than or equal to the corresponding sum in list \( b \), and 'NO' otherwise. The function does not return any value but prints the results of the queries.

