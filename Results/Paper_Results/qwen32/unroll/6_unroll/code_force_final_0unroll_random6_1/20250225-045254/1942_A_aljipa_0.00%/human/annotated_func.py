#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10³, and for each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10³. The sum of n over all test cases does not exceed 10³.
def func():
    t = int(input())
    for _ in range(t):
        n, k = (int(i) for i in input().split())
        
        res = [1] * n if k == n else range(n) if k == 1 else [-1]
        
        print(*res)
        
    #State: a series of printed lists for each test case, where each list is determined by the conditions on `n` and `k` for that test case.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `k` where `1 ≤ k ≤ n`. Based on the values of `n` and `k`, it prints a list of integers. If `k` equals `n`, it prints a list of `n` ones. If `k` equals `1`, it prints a list of integers from `0` to `n-1`. For all other values of `k`, it prints a list containing a single element `-1`.

