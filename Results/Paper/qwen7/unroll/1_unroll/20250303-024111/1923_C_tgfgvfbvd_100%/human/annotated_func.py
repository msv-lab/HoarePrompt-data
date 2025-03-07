#State of the program right berfore the function call: t is a positive integer; for each test case, n and q are positive integers such that 1 ≤ n, q ≤ 3 × 10^5; c is a list of n positive integers where each integer is between 1 and 10^9 inclusive; for each query, l_i and r_i are positive integers such that 1 ≤ l_i ≤ r_i ≤ n.
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
        
    #State: Output State: The output state consists of "YES" or "NO" printed for each query within the range specified by `m` queries. For each query `(a, b)`, it checks if the number of `1`s in the subarray `l[a-1:b+1]` is at least half the length of the subarray plus one. If true, it prints "YES"; otherwise, it prints "NO".
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it handles a list of positive integers `c` and a series of queries. Each query specifies a range within the list, and the function determines whether the number of occurrences of the integer `1` in that range is at least half the length of the range plus one. If true, it prints "YES"; otherwise, it prints "NO". The function does not return any value but outputs the results for each query.

