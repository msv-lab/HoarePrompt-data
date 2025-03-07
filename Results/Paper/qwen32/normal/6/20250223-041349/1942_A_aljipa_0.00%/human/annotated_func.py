#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, and for each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^3. The sum of n over all test cases does not exceed 10^3.
def func():
    t = int(input())
    for _ in range(t):
        n, k = (int(i) for i in input().split())
        
        res = [1] * n if k == n else range(n) if k == 1 else [-1]
        
        print(*res)
        
    #State: `t` is 0; no more test cases are processed; the final `res` is determined by the last test case processed, which is a list of `n` ones if `k` equals `n`, a range object from 0 to `n-1` if `k` equals 1, or a list containing `-1` otherwise.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of two integers `n` and `k`. For each test case, it outputs a list of `n` ones if `k` equals `n`, a sequence of numbers from 0 to `n-1` if `k` equals 1, or a list containing `-1` otherwise.

