#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and q are integers such that 1 ≤ n, q ≤ 3 · 10^5. c is a list of n integers where each element is greater than 0 and 1 ≤ c_i ≤ 10^9. For each query, l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n. The sum of n over all test cases does not exceed 3 · 10^5, and the sum of q over all test cases does not exceed 3 · 10^5.
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
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4. No other variables retain their values as they are local to each test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` representing the number of elements and `q` representing the number of queries. It then reads a list `l` of `n` integers. For each query, which consists of two integers `l_i` and `r_i`, the function determines if the sum of the elements from index `l_i` to `r_i` (inclusive) minus the number of elements in this range is greater than or equal to the count of 1's in the same range. It prints 'YES' if the condition is met, otherwise 'NO'.

