#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, and for each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^3. The sum of n over all test cases does not exceed 10^3.
def func():
    t = int(input())
    for _ in range(t):
        n, k = (int(i) for i in input().split())
        
        res = [1] * n if k == n else range(n) if k == 1 else [-1]
        
        print(*res)
        
    #State: A series of printed lists where each list corresponds to the result of a test case: a list of `n` ones if `k == n`, a range from `0` to `n-1` if `k == 1`, or a list containing `-1` if `k` is neither `n` nor `1`.
#Overall this is what the function does:The function processes `t` test cases, each defined by two integers `n` and `k`. For each test case, it prints a list of `n` ones if `k` equals `n`, a sequence from `0` to `n-1` if `k` equals `1`, or a list containing `-1` if `k` is neither `n` nor `1`.

