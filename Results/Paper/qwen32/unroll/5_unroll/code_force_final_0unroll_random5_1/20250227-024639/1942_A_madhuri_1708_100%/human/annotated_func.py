#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, and for each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^3. The sum of n over all test cases does not exceed 10^3.
def func():
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        if k >= 2:
            if n == k:
                print(*[k for j in range(k)])
            else:
                print('-1')
        else:
            print(*[(j + 1) for j in range(n)])
        
    #State: The output state consists of `t` lines, each representing the result of a test case. Each result is either a list of integers or `-1`, depending on the values of `n` and `k` for that test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by two integers `n` and `k`. For each test case, it outputs either a list of `k` integers where each integer is `k`, or `-1`, based on the conditions: if `k` is at least 2 and `n` equals `k`, it outputs the list; otherwise, it outputs `-1`. If `k` is less than 2, it outputs a list of the first `n` positive integers.

