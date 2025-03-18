#State of the program right berfore the function call: t is a positive integer, each test case consists of n and q where 1 <= n, q <= 3 * 10^5, an array c of length n where each element is a positive integer not exceeding 10^9, and q queries defined by pairs of integers l_i and r_i such that 1 <= l_i <= r_i <= n.
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
        
    #State: Output State: The program processes multiple test cases. For each test case, it first reads two integers \(n\) and \(m\), then an array \(l\) of length \(n\). It calculates a prefix sum array \(p\) where each element \(p[i]\) is the sum of the first \(i+1\) elements of \(l\). Then, for each of the \(m\) queries, it reads two integers \(a\) and \(b\), and determines whether the sum of the subarray from index \(a-1\) to \(b-1\) is at least twice the length of this subarray. If so, it prints 'YES'; otherwise, it prints 'NO'. The output state includes the results of all these queries for each test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads the number of elements \(n\) and the number of queries \(m\), followed by an array \(l\) of length \(n\). It then calculates a prefix sum array \(p\) where each element \(p[i]\) represents the sum of the first \(i+1\) elements of \(l\). For each query defined by indices \(a\) and \(b\), it checks if the sum of the subarray from index \(a-1\) to \(b-1\) is at least twice the length of this subarray. If the condition is met, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but outputs the results of all queries for each test case.

