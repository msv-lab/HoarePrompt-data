#State of the program right berfore the function call: The function should take two parameters, n and k, where n is the length of the array and k is the number of sorted cyclic shifts required. Both n and k are integers such that 1 ≤ k ≤ n ≤ 10^3. The function should handle multiple test cases, where the number of test cases t is an integer such that 1 ≤ t ≤ 10^3. The sum of n over all test cases does not exceed 10^3.
def func():
    t = int(input())
    for _ in range(t):
        n, k = (int(i) for i in input().split())
        
        res = [1] * n if k == n else range(n) if k == 1 else [-1]
        
        print(*res)
        
    #State: `t` must be greater than 0, `_` is `t-1`, `n` is the input integer from the last iteration, `k` is the input integer from the last iteration, `res` is a list of `n` ones if `k == n`, a range from 0 to `n-1` if `k == 1`, or `[-1]` otherwise.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads two integers `n` and `k`, where `n` is the length of the array and `k` is the number of sorted cyclic shifts required. The function then prints a list `res` based on the following conditions: if `k == n`, it prints a list of `n` ones; if `k == 1`, it prints a list of integers from 0 to `n-1`; otherwise, it prints `[-1]`. The function does not return any value; it only prints the results for each test case.

