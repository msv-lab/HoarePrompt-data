#State of the program right berfore the function call: t is a positive integer, and for each test case, n and q are positive integers such that 1 ≤ n, q ≤ 3 × 10^5. The array c is a list of n positive integers, each between 1 and 10^9 inclusive. For each query, l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n.
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
        
    #State: Output State: After processing all test cases, for each query, the program prints 'YES' if the sum of elements in the subarray from index `a-1` to `b-1` is at least twice the length of the subarray, otherwise it prints 'NO'.
#Overall this is what the function does:The function processes multiple test cases, each involving an array `c` of positive integers. For each test case, it handles a series of queries. Each query specifies a subarray of `c` defined by indices `a` and `b`. The function calculates the sum of the elements in this subarray and checks if the sum is at least twice the length of the subarray. If the condition is met, it prints 'YES'; otherwise, it prints 'NO'. This process is repeated for all queries in each test case.

