#State of the program right berfore the function call: t is a positive integer where 1 ≤ t ≤ 5000, representing the number of test cases. For each test case, n and k are integers where 2 ≤ n ≤ 50000 and 1 ≤ k ≤ floor(n/2). The array a is a list of 2n integers where 1 ≤ a[i] ≤ n, and each integer from 1 to n appears exactly twice in a.
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
        
        for i in range(1, n):
            if k == 0:
                break
            if b[i] == b[i - 1]:
                ans1.append(b[i])
                ans1.append(b[i])
                k -= 2
            elif b[i - 1] not in ans1:
                l.append(b[i - 1])
        
        if b[n - 1] not in ans1:
            l.append(b[n - 1])
        
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
        
        print(*ans1)
        
        print(*ans2)
        
    #State: After the loop has executed all iterations, `i` is the index of the last element processed in `l` (which is `len(l) - 1`), `ans1` contains all elements from `l` that were processed before `k` reached 0, `ans2` contains all elements from `l` that were processed before `k` reached 0, `k` is 0 if it was reduced to 0 during the loop execution, otherwise `k` is 2 times its original input value minus the total reduction due to the loop, `l` is a non-empty list containing elements from `b` that are not in `ans1` and were encountered before the loop terminated. If `b[n-1]` is not in `ans1`, then the last element of `b` (i.e., `b[n-1]`) is included in `l`. The values of `t`, `n`, `a`, `q`, `b`, `c`, and `req` remain unchanged.
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by the parameters `n`, `k`, and an array `a`. For each test case, `n` is an integer representing the length of the array divided by 2, `k` is an integer, and `a` is a list of 2n integers where each integer from 1 to n appears exactly twice. The function splits the array `a` into two halves, `b` and `c`, sorts both halves, and then selects pairs of identical elements from these halves to form two new lists, `ans1` and `ans2`. It ensures that the total number of selected pairs is equal to `2 * k`. If there are not enough pairs in `b` or `c`, it uses additional elements from a list `l` that contains unique elements from `b` not already in `ans1`. The function prints the contents of `ans1` and `ans2` for each test case. After processing all test cases, the function terminates, leaving the input variables `t`, `n`, `a`, `q`, `b`, `c`, and `req` unchanged.

