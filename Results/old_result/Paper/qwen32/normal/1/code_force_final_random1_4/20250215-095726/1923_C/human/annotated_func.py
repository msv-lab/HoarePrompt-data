#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and q are integers such that 1 ≤ n, q ≤ 3 · 10^5; c is a list of n integers where each element c_i satisfies 1 ≤ c_i ≤ 10^9; for each query, l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n; the sum of n over all test cases does not exceed 3 · 10^5; the sum of q over all test cases does not exceed 3 · 10^5.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        p = [0]
        
        c = [0]
        
        i, j = 0, 0
        
        for x in l:
            if x == 1:
                j += 1
            i += x
            p.append(i)
            c.append(j)
        
        for _ in range(m):
            a, b = map(int, input().split())
            i = c[b] - c[a - 1]
            s = p[b] - p[a - 1]
            if b - a + 1 > 1 and s - (b - a + 1) >= i:
                print('YES')
            else:
                print('NO')
        
    #State: `t` is an integer such that \(1 \leq t \leq 10^4\); `n` and `m` are integers read from the last test case; `l` is the list of `n` integers from the last test case; `p` is a list starting with `0` and ending with the cumulative sums of elements in `l` from the last test case; `c` is a list starting with `0` and ending with the cumulative counts of `1`s encountered in `l` from the last test case; `i` is the sum of all elements in `l` from the last test case; `j` is the count of `1`s in `l` from the last test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers and a series of queries. For each query, it determines whether a specific condition involving the sum and count of elements in a sublist is met, printing 'YES' if the condition is satisfied and 'NO' otherwise.

