#State of the program right berfore the function call: t is a positive integer; for each test case, n and q are positive integers such that 1 ≤ n, q ≤ 3 × 10^5; c is a list of n positive integers where each integer is between 1 and 10^9 inclusive; for each query, l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n.
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
        
    #State: Output State: After the loop executes all iterations, `c` will be the sum of all elements in the list `l`, and `p` will be a list containing the cumulative sums of the elements in `l`. The variable `m` will hold the total number of iterations the loop executed. For each query, the variable `s` will be calculated as `p[b - 1] - p[a - 2]` and checked against the condition `(b - a + 1 > 1 and s >= 2 * (b - a + 1))`. If the condition is met, 'YES' will be printed; otherwise, 'NO'. After processing all queries, the loop will terminate, and the final state of `m` will reflect the total number of queries processed.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads two integers \( n \) and \( m \), a list \( l \) of \( n \) positive integers, and \( m \) queries. It calculates the cumulative sums of the list \( l \) and then for each query, it determines if the sum of any subarray within the specified range meets a specific condition. If the condition is satisfied, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but prints the results for each query.

