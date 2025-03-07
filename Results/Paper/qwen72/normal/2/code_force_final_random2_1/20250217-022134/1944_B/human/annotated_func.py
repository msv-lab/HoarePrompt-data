#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 5000), representing the number of test cases. For each test case, n and k are integers where 2 ≤ n ≤ 5 · 10^4 and 1 ≤ k ≤ ⌊n/2⌋. a is a list of 2n integers (1 ≤ a_i ≤ n), where each integer from 1 to n appears exactly twice.
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
        
    #State: After the loop executes all iterations, `q` is `t`, `n` and `k` retain their final values from the last iteration, `a`, `b`, and `c` are reset for each new iteration with new inputs, `ans1` and `ans2` contain the results of the processing for each iteration, and `l` is reset for each new iteration.
#Overall this is what the function does:The function reads multiple test cases, each defined by integers `n` and `k`, and a list `a` of 2n integers. For each test case, it processes the list `a` to generate two lists, `ans1` and `ans2`, which are printed as the output. The function ensures that `ans1` and `ans2` contain elements from `a` such that certain conditions are met, particularly focusing on the distribution of unique and duplicate elements. After processing all test cases, the function has no return value, but it prints the results for each test case. The state of the program after the function concludes includes the completion of all test cases, with `t` being fully processed, and the variables `n`, `k`, `a`, `b`, `c`, `ans1`, `ans2`, and `l` being reset for each new test case.

