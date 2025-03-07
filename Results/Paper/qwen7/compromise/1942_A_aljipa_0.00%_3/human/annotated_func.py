#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3. For each test case, n and k are positive integers such that 1 ≤ k ≤ n ≤ 10^3 and the sum of n over all test cases does not exceed 10^3.
def func():
    t = int(input())
    for _ in range(t):
        n, k = (int(i) for i in input().split())
        
        res = [1] * n if k == n else range(n) if k == 1 else [-1]
        
        print(*res)
        
    #State: Output State: The output state will consist of `t` lines, each line containing either a list of `n` ones if `k` equals `n`, a range from `0` to `n-1` if `k` equals `1`, or `-1` if neither condition is met. Each value of `n` and `k` is determined by the input on that iteration of the loop.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers \( n \) and \( k \). For each test case, it generates and prints a list based on the values of \( n \) and \( k \). If \( k \) equals \( n \), it prints a list of \( n \) ones. If \( k \) equals 1, it prints a list containing numbers from 0 to \( n-1 \). In all other cases, it prints -1.

