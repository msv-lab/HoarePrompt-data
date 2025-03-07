#State of the program right berfore the function call: t is a positive integer; for each test case, n and q are positive integers such that 1 ≤ n, q ≤ 3 × 10^5; c is a list of n positive integers where 1 ≤ c_i ≤ 10^9; for each query, l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n.
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
        
    #State: Output State: The program will execute a series of test cases. For each test case, it will first read two integers \(n\) and \(m\), then a list of \(n\) integers \(l\). It will compute a prefix sum list \(p\) from the list \(l\). Then, for each of the \(m\) queries, it will read two integers \(a\) and \(b\), and determine whether the sum of elements in the sublist \(l_{a-1}\) to \(l_{b-1}\) is at least twice the length of the sublist. If so, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases and queries, the output consists of 'YES' or 'NO' for each query across all test cases.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads two integers \(n\) and \(m\), followed by a list of \(n\) integers \(l\). It computes a prefix sum list \(p\) from the list \(l\). Then, for each of the \(m\) queries, it reads two integers \(a\) and \(b\), and determines whether the sum of elements in the sublist from index \(a-1\) to \(b-1\) is at least twice the length of the sublist. If so, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases and queries, the function outputs 'YES' or 'NO' for each query across all test cases.

