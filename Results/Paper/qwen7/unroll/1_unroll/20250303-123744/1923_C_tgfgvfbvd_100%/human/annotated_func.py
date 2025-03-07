#State of the program right berfore the function call: t is a positive integer, and for each test case, n and q are positive integers such that 1 ≤ n, q ≤ 3 × 10^5. The array c is a list of n positive integers where each element is between 1 and 10^9 inclusive. Each query is defined by two integers l_i and r_i such that 1 ≤ l_i ≤ r_i ≤ n.
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
        
    #State: Output State: After processing all test cases, for each query, a 'YES' or 'NO' is printed based on the conditions specified in the loop. Specifically, for each query defined by \(a\) and \(b\), it checks if the number of 1s in the subarray from index \(a\) to \(b\) (inclusive) is at least half the length of the subarray. If true, it prints 'YES'; otherwise, it prints 'NO'.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an array `c` and a set of queries. For each query defined by indices `a` and `b`, it checks whether the number of 1s in the subarray from index `a` to `b` (inclusive) is at least half the length of the subarray. If true, it prints 'YES'; otherwise, it prints 'NO'. This process is repeated for all queries in each test case.

