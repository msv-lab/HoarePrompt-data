#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and q are integers such that 1 <= n, q <= 3 * 10^5. c is a list of n integers where each element c_i satisfies 1 <= c_i <= 10^9. For each query i, l_i and r_i are integers such that 1 <= l_i <= r_i <= n. The sum of n over all test cases does not exceed 3 * 10^5 and the sum of q over all test cases does not exceed 3 * 10^5.
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
        
    #State: The output state consists of a series of 'YES' or 'NO' responses for each query in every test case, based on the conditions specified in the loop. The variables `t`, `n`, `q`, `c`, and the individual queries `l_i` and `r_i` remain unchanged from their initial state, except that `t` decrements as each test case is processed. The lists `p` and `c` are recalculated for each test case and are not preserved across different test cases. The final state of `t` will be 0, indicating that all test cases have been processed.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a list of integers and a series of queries. For each query, it determines if the sum of the elements in a specified range of the list, minus the number of elements in that range, is greater than or equal to the count of the number 1s in that range. It outputs 'YES' if the condition is met and 'NO' otherwise.

