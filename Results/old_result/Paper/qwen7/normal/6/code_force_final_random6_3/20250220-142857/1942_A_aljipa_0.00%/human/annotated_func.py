#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3. For each test case, n and k are positive integers such that 1 ≤ k ≤ n ≤ 10^3, and the sum of n over all test cases does not exceed 10^3.
def func():
    t = int(input())
    for _ in range(t):
        n, k = (int(i) for i in input().split())
        
        res = [1] * n if k == n else range(n) if k == 1 else [-1]
        
        print(*res)
        
    #State: Output State: The value of `t` must be exactly equal to the total number of iterations the loop has executed, which is greater than 0. For each iteration, `n` is an input integer, and `k` is an input integer. The variable `res` will be a list with `n` elements all set to 1 if `k` equals `n`, a range object representing numbers from 0 to `n-1` if `k` equals 1, or a list with a single element `-1` otherwise.
    #
    #This means after all iterations of the loop have finished, `t` will reflect the total number of iterations, and for each iteration, `res` will be determined based on the conditions provided with the respective `n` and `k` values.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \( n \) and \( k \). It outputs a list \( res \) based on the values of \( n \) and \( k \) for each test case. If \( k \) equals \( n \), the list contains \( n \) ones. If \( k \) equals 1, the list is a range object from 0 to \( n-1 \). Otherwise, the list contains a single element \(-1\). The function does not return any value but prints the resulting list for each test case.

