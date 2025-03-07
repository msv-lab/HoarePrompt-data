#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and q are integers such that 1 ≤ n, q ≤ 3 · 10^5; c is a list of n integers such that 1 ≤ c_i ≤ 10^9; queries is a list of q tuples, each containing two integers l_i and r_i such that 1 ≤ l_i ≤ r_i ≤ n; the sum of n over all test cases does not exceed 3 · 10^5; the sum of q over all test cases does not exceed 3 · 10^5.
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
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and q are integers such that 1 ≤ n, q ≤ 3 · 10^5; c is a list of n + 1 integers such that 1 ≤ c_i ≤ 10^9; queries is a list of q tuples, each containing two integers l_i and r_i such that 1 ≤ l_i ≤ r_i ≤ n; the sum of n over all test cases does not exceed 3 · 10^5; the sum of q over all test cases does not exceed 3 · 10^5.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads the number of elements `n` and the number of queries `q`. It then reads a list `l` of `n` integers. The function constructs two auxiliary lists `p` and `c` where `p` keeps a cumulative sum of the elements in `l`, and `c` keeps a cumulative count of the number of 1s encountered in `l`. For each query, defined by a tuple `(a, b)`, the function checks if the sum of elements in the subarray `l[a:b+1]` minus the length of the subarray is greater than or equal to the count of 1s in the subarray. If this condition is met, it prints 'YES'; otherwise, it prints 'NO'. After processing all queries for all test cases, the function concludes.

