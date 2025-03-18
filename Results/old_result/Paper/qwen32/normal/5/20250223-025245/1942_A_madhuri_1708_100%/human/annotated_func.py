#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10³. For each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10³. The sum of n over all test cases does not exceed 10³.
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
        
    #State: a sequence of printed results for each test case based on the conditions provided in the loop.
#Overall this is what the function does:The function reads a number of test cases, each defined by two integers `n` and `k`. For each test case, it prints a sequence of numbers based on the conditions: if `k` is at least 2 and `n` equals `k`, it prints `k` repeated `k` times; if `k` is at least 2 and `n` does not equal `k`, it prints `-1`; if `k` is less than 2, it prints numbers from 1 to `n`.

