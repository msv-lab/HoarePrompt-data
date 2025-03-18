#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3. For each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^3, and the sum of n over all test cases does not exceed 10^3.
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
        
    #State: the loop has processed all `t` test cases, and the program has printed the appropriate output for each test case based on the conditions specified in the loop.
#Overall this is what the function does:The function processes multiple test cases. For each test case, given two integers `n` and `k`, it prints a sequence of numbers based on specific conditions: if `k` is 1, it prints numbers from 1 to `n`; if `k` is greater than or equal to 2 and `n` equals `k`, it prints `k` repeated `k` times; otherwise, it prints `-1`.

