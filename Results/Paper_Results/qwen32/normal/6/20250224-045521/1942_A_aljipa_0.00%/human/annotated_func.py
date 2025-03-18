#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, and for each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^3. The sum of n over all test cases does not exceed 10^3.
def func():
    t = int(input())
    for _ in range(t):
        n, k = (int(i) for i in input().split())
        
        res = [1] * n if k == n else range(n) if k == 1 else [-1]
        
        print(*res)
        
    #State: `t` is `0`; `n` and `k` are undefined as the loop has finished executing; `res` is undefined as the loop has finished executing.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `k` where `1 ≤ k ≤ n`. It then prints a list of `n` integers based on the value of `k`: if `k` equals `n`, it prints a list of `n` ones; if `k` equals `1`, it prints a list of integers from `0` to `n-1`; otherwise, it prints `-1`.

