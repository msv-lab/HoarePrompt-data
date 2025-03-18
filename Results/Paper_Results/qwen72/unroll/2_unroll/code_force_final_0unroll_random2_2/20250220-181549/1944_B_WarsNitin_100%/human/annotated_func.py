#State of the program right berfore the function call: The function `func` should be defined with parameters `a` and `k`, where `a` is a list of integers of length `2n` containing each integer from 1 to `n` exactly twice, and `k` is an integer such that \(1 \leq k \leq \left\lfloor \frac{n}{2} \right\rfloor\). Additionally, `n` is an integer such that \(2 \leq n \leq 5 \cdot 10^4\).
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
        
    #State: The loop iterates `t` times. In each iteration, it reads two integers `n` and `k` from input, and a list `a` of integers from input. It then processes the list `a` to create two new lists `ans1` and `ans2` based on the sorting and selection criteria described in the loop. After processing, it prints the elements of `ans1` and `ans2`. The variables `n`, `k`, and `a` are re-initialized in each iteration, so their values are not retained between iterations. The variable `t` remains unchanged and is the only variable that persists across all iterations.
#Overall this is what the function does:The function `func` processes a series of test cases. Each test case involves reading two integers `n` and `k` from input, followed by a list `a` of integers of length `2n` where each integer from 1 to `n` appears exactly twice. The function then splits `a` into two halves, sorts each half, and constructs two new lists `ans1` and `ans2` based on the sorted halves and the value of `k`. Specifically, it tries to fill `ans1` and `ans2` with pairs of identical elements from the sorted halves, and if necessary, with unique elements from a temporary list `l`. The function prints the elements of `ans1` and `ans2` for each test case. The variables `n`, `k`, and `a` are re-initialized in each iteration, so their values are not retained between iterations. The variable `t` remains unchanged and is the only variable that persists across all iterations.

