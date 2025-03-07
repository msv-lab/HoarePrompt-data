#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and q are integers such that 1 ≤ n, q ≤ 3 · 10^5; c is a list of n integers where each integer c_i satisfies 1 ≤ c_i ≤ 10^9; for each query, l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n; the sum of n over all test cases does not exceed 3 · 10^5; the sum of q over all test cases does not exceed 3 · 10^5.
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
        
    #State: The variable `t` remains an integer between 1 and 10^4 representing the total number of test cases. For each test case, `n` is the number of integers in the list `l`, and `m` is the number of queries. The list `l` contains `n` integers, and `p` is a list of cumulative sums derived from `l`. The variable `c` holds the total sum of all elements in `l`. The loop has processed all `m` queries for each of the `t` test cases. For each query defined by `a` and `b`, the sum `s` of the subarray from index `a-1` to `b-1` is calculated using the cumulative sums in `p`. If the length of the subarray is greater than 1 and the sum `s` is at least twice the length of the subarray, 'YES' is printed; otherwise, 'NO' is printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers and a series of queries. For each query, it determines if the sum of a specified subarray is at least twice the length of that subarray, printing 'YES' if true and 'NO' otherwise.

