#State of the program right berfore the function call: t is a positive integer; for each test case, n and q are positive integers such that 1 ≤ n, q ≤ 3 × 10^5; c is a list of n positive integers where 1 ≤ c_i ≤ 10^9; for each query, l_i and r_i are positive integers such that 1 ≤ l_i ≤ r_i ≤ n.
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
        
    #State: Output State: After the loop executes all iterations, `m` will be 0 because `m` is decremented in each iteration of the inner loop until it reaches 0. The variables `a` and `b` will contain the values from the last input pair of integers provided during the loop's execution. The variable `i` will be `c[b] - c[a - 1]`, which represents the count of 1s between indices `a-1` and `b` inclusive. The variable `s` will be `p[b] - p[a - 1]`, representing the sum of elements between indices `a-1` and `b` inclusive. The condition `b - a + 1 > 1 and s - (b - a + 1) >= i` will be evaluated for the last input pair, and either 'YES' or 'NO' will be printed based on the result. The lists `p` and `c` will be fully constructed based on the input sequence `l`, with `p` containing cumulative sums and `c` containing cumulative counts of 1s. Variables `j` and the input list `l` will remain unchanged from their initial states as they are not affected by the loop.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `t`, followed by an integer `n`, an integer `m`, a list `c` of `n` positive integers, and `m` queries. Each query involves two integers `l_i` and `r_i`. For each query, the function calculates the sum of elements and the count of 1s within the specified range `[l_i, r_i]` in the list `c`. It then checks if the difference between the sum and the length of the range is greater than or equal to the count of 1s. If the condition is met, it prints 'YES'; otherwise, it prints 'NO'. After processing all queries for a test case, the function moves to the next test case.

