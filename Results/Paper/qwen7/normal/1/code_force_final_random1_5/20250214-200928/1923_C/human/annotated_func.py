#State of the program right berfore the function call: t is a positive integer, and for each test case, n and q are positive integers such that 1 ≤ n, q ≤ 3 × 10^5. c is a list of n positive integers where 1 ≤ c_i ≤ 10^9, and for each query, l_i and r_i are positive integers such that 1 ≤ l_i ≤ r_i ≤ n.
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
        
    #State: After the loop executes all the iterations, `m` will be equal to the total number of iterations performed, `a` and `b` will be the last pair of integers entered by the user for the final iteration, `i` will be `c[b] - c[a - 1]`, `s` will be `p[b] - p[a - 1]`. The condition inside the if statement will be evaluated based on the last values of `a`, `b`, `i`, and `s`. If the condition `b - a + 1 > 1` and `s - (b - a + 1) >= i` is true, 'YES' will be printed; otherwise, 'NO' will be printed.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads two integers \( n \) and \( m \), followed by a list of \( n \) integers \( l \). It then handles \( m \) queries, each defined by two integers \( a \) and \( b \). For each query, it calculates the number of 1s in the subarray from index \( a-1 \) to \( b \) and the sum of the subarray. Based on these calculations, it prints 'YES' if the subarray meets a specific condition (i.e., the number of 1s plus the length of the subarray minus one is less than or equal to the sum of the subarray), otherwise it prints 'NO'. After processing all queries for a test case, the function moves on to the next test case until all test cases are processed.

