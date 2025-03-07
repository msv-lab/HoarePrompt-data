#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and q are integers such that 1 ≤ n, q ≤ 3 · 10^5; c is a list of n integers where each element is greater than 0 and 1 ≤ c_i ≤ 10^9; for each query, l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n; the sum of n over all test cases does not exceed 3 · 10^5; the sum of q over all test cases does not exceed 3 · 10^5.
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
        
    #State: t is an integer such that \(1 \leq t \leq 10^4\); the loop has executed `t` times, with each execution involving reading `n` and `m`, a list `l` of `n` integers, computing cumulative sums into list `p`, and processing `m` queries. Each query involves reading `a` and `b`, computing `s` as the sum of elements from index `a-1` to `b-1` in `l`, and printing 'YES' if `b - a + 1 > 1` and `s >= 2 * (b - a + 1)`, otherwise 'NO'. The variables `n`, `m`, `l`, `p`, and `c` are reset for each test case, while `_` in the outer loop is decremented until it reaches 0.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and `q`, a list `c` of `n` positive integers, and `q` queries. Each query consists of two integers `l_i` and `r_i`. The function calculates the sum of the elements in the list `c` from index `l_i` to `r_i` (inclusive) and prints 'YES' if the sum is at least twice the number of elements in the queried range and the range contains more than one element; otherwise, it prints 'NO'.

