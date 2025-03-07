#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4; for each test case, n and q are integers such that 1 <= n, q <= 3 * 10^5; c is a list of n integers where each element is greater than 0 and the sum of n over all test cases does not exceed 3 * 10^5; for each query, l_i and r_i are integers such that 1 <= l_i <= r_i <= n and the sum of q over all test cases does not exceed 3 * 10^5.
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
        
    #State: t is an integer such that 1 <= t <= 10^4; for each test case, n and q are integers such that 1 <= n, q <= 3 * 10^5; c is a list of n integers where each element is greater than 0 and the sum of n over all test cases does not exceed 3 * 10^5; for each query, l_i and r_i are integers such that 1 <= l_i <= r_i <= n and the sum of q over all test cases does not exceed 3 * 10^5. The loop has finished executing all test cases, and for each query in each test case, it has printed either 'YES' or 'NO' based on the condition provided. The variables n, m, l, p, c, a, b, and s are not in a defined state as they are local to the loop iterations and do not persist after the loop completes.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it receives an integer `n`, a list `c` of `n` integers, and `q` queries. Each query consists of two integers `l_i` and `r_i`, and the function determines if the sum of the elements in the list `c` from index `l_i` to `r_i` (inclusive) is at least twice the number of elements in that range. It prints 'YES' if the condition is met, otherwise 'NO'. The function does not return any value explicitly; it outputs the result of each query directly.

