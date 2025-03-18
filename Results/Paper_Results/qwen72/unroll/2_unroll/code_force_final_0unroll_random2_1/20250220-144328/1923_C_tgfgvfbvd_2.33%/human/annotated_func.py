#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and q are integers such that 1 ≤ n, q ≤ 3 · 10^5, c is a list of n integers where 1 ≤ c_i ≤ 10^9, and for each query, l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n. The sum of n over all test cases does not exceed 3 · 10^5, and the sum of q over all test cases does not exceed 3 · 10^5.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        p = []
        
        c = 0
        
        for x in l:
            c += x
            p.append(c)
        
        for _ in range(m):
            a, b = map(int, input().split())
            s = p[b - 1]
            if a - 2 >= 0:
                s -= p[a - 2]
            if b - a + 1 > 1 and s >= 2 * (b - a + 1):
                print('YES')
            else:
                print('NO')
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4, n and q are integers such that 1 ≤ n, q ≤ 3 · 10^5, c is a list of n integers where 1 ≤ c_i ≤ 10^9, and for each query, l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n. The sum of n over all test cases does not exceed 3 · 10^5, and the sum of q over all test cases does not exceed 3 · 10^5. The loop has processed all test cases, and for each query, it has printed 'YES' or 'NO' based on the conditions specified in the loop.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `n` and a list `l` of `n` integers, then constructs a prefix sum list `p` from `l`. It also reads an integer `m` and processes `m` queries, each defined by a range `[a, b]` within the list `l`. For each query, the function determines if the sum of elements in the range `[a, b]` is at least twice the length of the range. If this condition is met, it prints 'YES'; otherwise, it prints 'NO'. After processing all queries for all test cases, the function concludes.

