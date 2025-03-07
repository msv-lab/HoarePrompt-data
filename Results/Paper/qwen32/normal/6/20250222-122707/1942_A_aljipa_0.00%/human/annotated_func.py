#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3. For each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^3, and the sum of n over all test cases does not exceed 10^3.
def func():
    t = int(input())
    for _ in range(t):
        n, k = (int(i) for i in input().split())
        
        res = [1] * n if k == n else range(n) if k == 1 else [-1]
        
        print(*res)
        
    #State: The loop will have executed `t` times, where `t` is an integer read from input such that 1 ≤ t ≤ 10^3. For each iteration, `n` and `k` are integers read from the input. The variable `res` will be a list of 1s with length `n` if `k` equals `n`, a range object from 0 to `n-1` if `k` equals 1, or a list containing -1 if neither condition is met. The output for each iteration will be the contents of `res` printed to the console.
#Overall this is what the function does:The function processes `t` test cases, each defined by two integers `n` and `k`. For each test case, it outputs a list of `n` ones if `k` equals `n`, a sequence of numbers from 0 to `n-1` if `k` equals 1, or a list containing -1 if neither condition is met.

