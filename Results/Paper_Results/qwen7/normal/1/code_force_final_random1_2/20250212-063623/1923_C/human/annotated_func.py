#State of the program right berfore the function call: t is a positive integer; for each test case, n and q are positive integers such that 1 ≤ n, q ≤ 3 × 10^5; c is a list of n positive integers where each integer is between 1 and 10^9 inclusive; for each query, l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n.
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
        
    #State: After the loop executes all iterations, `m` will be equal to the total number of valid query pairs `(a, b)` that satisfy the condition `(b - a + 1 > 1 and s - (b - a + 1) >= i)` across all queries. The variables `n`, `q`, `l`, `p`, and `c` will be updated based on the final input values of `a` and `b` for each query. `a` and `b` will contain the last pair of integers entered through input for the final query. `i` will be `c[b] - c[a - 1]`, and `s` will be `p[b] - p[a - 1]`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of positive integers `c` and a set of queries. For each query, it checks if the sum of elements in a specified range `[l_i, r_i]` minus the length of the range is greater than or equal to a specific count of ones in that range. If the condition is met, it prints 'YES'; otherwise, it prints 'NO'. The function updates variables based on the inputs and finalizes with the results of the last query.

