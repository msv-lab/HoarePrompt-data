#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4; for each test case, n and q are integers where 1 ≤ n, q ≤ 3 · 10^5; c is a list of n integers where 1 ≤ c_i ≤ 10^9; q queries are provided, each consisting of two integers l_i and r_i where 1 ≤ l_i ≤ r_i ≤ n. The sum of n over all test cases does not exceed 3 · 10^5, and the sum of q over all test cases does not exceed 3 · 10^5.
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
        
    #State: _ is 0, t is an integer where 1 ≤ t ≤ 10^4, n and m are integers based on user input, l is a list of integers based on user input, p is a list containing the cumulative sums of the elements in l, c is equal to the sum of all elements in l. For each of the m queries, a and b are integers based on user input. If a - 2 is greater than or equal to 0, s is equal to p[b - 1] - p[a - 2]. Otherwise, s remains equal to p[b - 1]. If b - a + 1 > 1 and s >= 2 * (b - a + 1), the program prints 'YES'. Otherwise, it prints 'NO'.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `t` (number of test cases). For each test case, it reads two integers `n` and `m`, followed by a list `l` of `n` integers. It then computes a list `p` of cumulative sums of the elements in `l`. For each of the `m` queries, it reads two integers `a` and `b`, calculates a value `s` based on the cumulative sums in `p`, and checks if the condition `s >= 2 * (b - a + 1)` holds. If the condition is true, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function ends.

