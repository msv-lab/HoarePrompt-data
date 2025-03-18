#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3. For each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^3, and the sum of n over all test cases does not exceed 10^3.
def func():
    t = int(input())
    for _ in range(t):
        n, k = (int(i) for i in input().split())
        
        res = [1] * n if k == n else range(n) if k == 1 else [-1]
        
        print(*res)
        
    #State: Output State: After the loop executes all its iterations, `t` will be 0, as it starts from a value between 1 and \(10^3\) and decreases by 1 with each iteration until it reaches 0. For each iteration, `n` and `k` will be input integers that determine the value of `res`. The value of `res` will depend on the conditions: if `k == n`, then `res` will be `[1] * n`; if `k == 1`, then `res` will be `range(n)`; otherwise, `res` will be `[-1]`.
    #
    #In summary, after all iterations of the loop, `t` will be 0, and `res` will be determined by the last values of `n` and `k` entered by the user, following the specified conditions.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \(n\) and \(k\). Based on the values of \(n\) and \(k\), it generates a list `res` with specific configurations: if \(k = n\), `res` is a list of \(n\) ones; if \(k = 1\), `res` is a range of integers from 0 to \(n-1\); otherwise, `res` is a list containing a single `-1`. After processing all test cases, the function prints the list `res` for each test case and sets the counter `t` to 0.

