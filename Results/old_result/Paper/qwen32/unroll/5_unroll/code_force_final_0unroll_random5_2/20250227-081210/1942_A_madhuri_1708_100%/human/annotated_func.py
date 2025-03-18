#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3. For each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^3. The sum of n over all test cases does not exceed 10^3.
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
        
    #State: a series of lines where each line is either a sequence of `n` numbers where each number is `k` if `n == k` and `k >= 2`, or a sequence of numbers from `1` to `n` if `k < 2`, or `-1` if `n != k` and `k >= 2`.
#Overall this is what the function does:The function processes a series of test cases, each defined by two integers `n` and `k`. For each test case, it outputs a sequence of `n` numbers. If `k < 2`, the sequence contains numbers from `1` to `n`. If `k ≥ 2` and `n == k`, the sequence contains `k` repeated `k` times. If `k ≥ 2` and `n ≠ k`, it outputs `-1`.

