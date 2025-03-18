#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3. Each test case consists of two integers n and k such that 1 ≤ k ≤ n ≤ 10^3, and the sum of n over all test cases does not exceed 10^3.
def func():
    t = int(input())
    for _ in range(t):
        n, k = (int(i) for i in input().split())
        
        res = [1] * n if k == n else range(n) if k == 1 else [-1]
        
        print(*res)
        
    #State: Output State: The output state will consist of multiple lines, each containing either a list of 1s of length `n`, a range from 0 to `n-1`, or `-1`. The number of lines and their contents depend on the input values for `t`, `n`, and `k` provided by the user. Each line corresponds to one iteration of the loop, where `t` is the total number of iterations. If `k` equals `n`, the line will contain a list of `n` 1s. If `k` equals 1, the line will contain a range from 0 to `n-1`. Otherwise, the line will contain `-1`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers \( n \) and \( k \). For each test case, it generates and prints one of three possible outputs: a list of \( n \) ones if \( k \) equals \( n \), a range from 0 to \( n-1 \) if \( k \) equals 1, or \(-1\) otherwise. The function reads the number of test cases \( t \) first, then iterates through each test case, performing the specified output generation and printing.

