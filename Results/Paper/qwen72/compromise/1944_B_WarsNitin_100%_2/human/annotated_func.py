#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 5000), representing the number of test cases. Each test case consists of two integers n and k (2 ≤ n ≤ 50000, 1 ≤ k ≤ floor(n/2)), and a list a of 2n integers (1 ≤ a[i] ≤ n) where each integer from 1 to n appears exactly twice. The sum of n over all test cases does not exceed 50000.
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
        
    #State: After the loop executes all the iterations, `q` is `t - 1`, `ans1` and `ans2` contain the selected elements from `b` and `c` respectively, ensuring that each element in `ans1` and `ans2` is part of the pairs or unique elements as required by `k`. `k` is 0, indicating that the required number of elements has been added to `ans1` and `ans2`. The lists `b` and `c` remain sorted, and `l` contains the unique elements from `b` that were not paired. The original values of `n`, `k` (before modification in the loop), and `req` remain unchanged.
#Overall this is what the function does:The function processes a series of test cases, each defined by integers `n` and `k`, and a list `a` of 2n integers. For each test case, it divides the list `a` into two equal parts, `b` and `c`, sorts both parts, and then selects elements to form two new lists, `ans1` and `ans2`. The selection ensures that each list contains pairs of identical elements from `b` and `c`, and possibly some unique elements, based on the value of `k`. The function prints the contents of `ans1` and `ans2` for each test case. After processing all test cases, the function completes, and the state reflects that all test cases have been processed according to the specified rules.

