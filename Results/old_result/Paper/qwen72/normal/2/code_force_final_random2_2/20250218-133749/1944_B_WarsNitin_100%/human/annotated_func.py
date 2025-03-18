#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 5000), representing the number of test cases. For each test case, n and k are integers where 2 ≤ n ≤ 50000 and 1 ≤ k ≤ ⌊n/2⌋. a is a list of 2n integers (1 ≤ a_i ≤ n), where each integer from 1 to n appears exactly twice.
def func():
    t = int(input())
    for q in range(t):
        n, k = list(map(int, input().split(' ')))
        
        a = list(map(int, input().split(' ')))
        
        b = a[:n]
        
        c = a[n:]
        
        b.sort()
        
        c.sort()
        
        ans1 = []
        
        ans2 = []
        
        k = 2 * k
        
        req = k
        
        l = []
        
        if b[0] != b[1]:
            l.append(b[0])
        
        if b[n - 2] != b[n - 1]:
            l.append(b[n - 1])
        else:
            ans1.append(b[n - 1])
            ans1.append(b[n - 1])
            k -= 2
        
        for i in range(1, n - 1):
            if k == 0:
                break
            if b[i] == b[i - 1]:
                ans1.append(b[i])
                ans1.append(b[i])
                k -= 2
            elif b[i] != b[i + 1]:
                l.append(b[i])
        
        k = req
        
        for i in range(1, n):
            if k == 0:
                break
            if c[i] == c[i - 1]:
                ans2.append(c[i])
                ans2.append(c[i])
                k -= 2
        
        for i in range(len(l)):
            if k == 0:
                break
            ans1.append(l[i])
            ans2.append(l[i])
            k -= 1
        
        print(*ans1)
        
        print(*ans2)
        
    #State: After the loop has executed all iterations, `t` is 0, `q` is `t - 1`, `ans1` and `ans2` contain the selected elements based on the conditions specified in the loop, `k` is `max(0, req - 2 * m - len(l))` where `m` is the number of times `c[i] == c[i - 1]` was true, `l` contains the unique elements from `b` and `c` that were not paired, and `a`, `b`, `c`, `req`, and `n` remain unchanged for each test case.
#Overall this is what the function does:The function `func` processes a series of test cases. Each test case involves an integer `n`, an integer `k`, and a list `a` of 2n integers where each integer from 1 to n appears exactly twice. The function splits the list `a` into two halves, sorts them, and then selects elements based on specific conditions to form two lists `ans1` and `ans2`. These lists are printed as the output for each test case. After processing all test cases, the function completes without returning any value. The final state of the program is that all test cases have been processed, and the results have been printed.

