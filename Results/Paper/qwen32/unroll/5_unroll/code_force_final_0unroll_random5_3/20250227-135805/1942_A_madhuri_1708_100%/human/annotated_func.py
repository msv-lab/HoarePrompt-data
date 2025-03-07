#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^3, and for each test case, n and k are integers such that 1 <= k <= n <= 10^3. The sum of n over all test cases does not exceed 10^3.
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
        
    #State: A series of printed lines for each test case based on the conditions: if k >= 2 and n == k, prints k repeated k times; if k >= 2 and n != k, prints -1; if k < 2, prints numbers from 1 to n.
#Overall this is what the function does:The function processes multiple test cases, each defined by two integers `n` and `k`. For each test case, it prints a sequence of numbers based on the conditions: if `k >= 2` and `n == k`, it prints `k` repeated `k` times; if `k >= 2` and `n != k`, it prints `-1`; if `k < 2`, it prints numbers from `1` to `n`.

