#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3. For each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^3. The sum of n over all test cases does not exceed 10^3.
def func():
    t = int(input())
    for _ in range(t):
        n, k = (int(i) for i in input().split())
        
        res = [1] * n if k == n else range(n) if k == 1 else [-1]
        
        print(*res)
        
    #State: For each test case, the output is a list of `n` ones if `k == n`, a list of the first `n` non-negative integers if `k == 1`, and a list with a single element `-1` if `k` is neither `n` nor `1`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `k` (with 1 ≤ k ≤ n ≤ 10^3). It then prints a list of `n` ones if `k` equals `n`, a list of the first `n` non-negative integers if `k` equals 1, and a list with a single element `-1` if `k` is neither `n` nor `1`.

