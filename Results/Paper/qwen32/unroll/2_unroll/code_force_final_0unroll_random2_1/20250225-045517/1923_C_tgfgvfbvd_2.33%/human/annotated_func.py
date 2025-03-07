#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and q are integers such that 1 <= n, q <= 3 * 10^5. c is a list of n integers where each element is greater than 0, i.e., 1 <= c_i <= 10^9. For each query, l_i and r_i are integers such that 1 <= l_i <= r_i <= n. The sum of n over all test cases does not exceed 3 * 10^5, and the sum of q over all test cases does not exceed 3 * 10^5.
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
        
    #State: t is an integer such that 1 <= t <= 10^4.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a list of integers and a series of queries. For each query, it determines if the sum of a specified sub-list is at least twice the length of that sub-list, printing 'YES' if true and 'NO' otherwise.

