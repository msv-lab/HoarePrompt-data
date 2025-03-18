#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and q are integers such that 1 ≤ n, q ≤ 3 · 10^5; c is a list of n integers where each element is greater than 0 and 1 ≤ c_i ≤ 10^9; for each query, l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n; the sum of n over all test cases does not exceed 3 · 10^5; the sum of q over all test cases does not exceed 3 · 10^5.
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
        
    #State: The loop has processed all `t` test cases. For each test case, it has read `n` and `m`, the list `l` of `n` integers, and `m` pairs of integers `(a, b)`. It has computed the cumulative sum list `p` and the cumulative count of 1s list `c`. For each query `(a, b)`, it has determined whether the condition `b - a + 1 > 1` and `s - (b - a + 1) >= i` holds, where `i` is the count of 1s in the sublist `l[a-1:b]` and `s` is the sum of the elements in the same sublist, printing 'YES' if the condition is met and 'NO' otherwise. The variables `t`, `n`, `m`, `l`, `p`, `c`, `i`, `j`, `a`, and `b` are in their final states as per the last test case processed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers and a series of queries. For each query, it determines if the sum of the elements in a specified range of the list, minus the number of elements in that range, is greater than or equal to the count of 1s in that range, and prints 'YES' if true, otherwise 'NO'.

