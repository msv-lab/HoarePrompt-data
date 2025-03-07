#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and q are integers such that 1 <= n, q <= 3 * 10^5. c is a list of n integers where each element c_i satisfies 1 <= c_i <= 10^9. For each query, l_i and r_i are integers such that 1 <= l_i <= r_i <= n. The sum of n over all test cases does not exceed 3 * 10^5, and the sum of q over all test cases does not exceed 3 * 10^5.
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
        
    #State: For each test case, the code will output 'YES' or 'NO' for each query based on whether the sum of the subarray from index l_i to r_i is at least twice the length of the subarray. The variables n, m, l, p, and c will not retain their values after the loop finishes as they are reinitialized for each test case. The variable t, which represents the number of test cases, will be decremented to 0 after all test cases have been processed.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it receives an integer `n` representing the number of elements in a list `c`, and an integer `q` representing the number of queries. It then processes `q` queries, each consisting of two integers `l_i` and `r_i`, to determine if the sum of the subarray of `c` from index `l_i` to `r_i` (inclusive) is at least twice the length of the subarray. The function outputs 'YES' if the condition is met, otherwise 'NO'.

