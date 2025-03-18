#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3. For each test case, n and k are positive integers such that 1 ≤ k ≤ n ≤ 10^3 and the sum of n over all test cases does not exceed 10^3.
def func():
    t = int(input())
    for _ in range(t):
        n, k = (int(i) for i in input().split())
        
        res = [1] * n if k == n else range(n) if k == 1 else [-1]
        
        print(*res)
        
    #State: Output State: The output state will consist of multiple lines, each containing either a list of 1s of length `n`, a range from 0 to `n-1`, or `-1`, depending on the values of `n` and `k` entered for each iteration. The number of such lines will be equal to the value of `t`. Each line's content is determined by the conditions inside the loop body.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two positive integers \( n \) and \( k \). Based on the values of \( n \) and \( k \), it prints one of three possible outputs for each test case: a list of \( n \) ones, a range from 0 to \( n-1 \), or -1. The number of test cases is determined by the first input \( t \), which represents the total count of test cases. The function does not return any value but outputs the results directly.

