#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000. For each test case, n is an integer such that 2 ≤ n ≤ 50,000, and k is an integer such that 1 ≤ k ≤ ⌊n/2⌋. a is a list of 2n integers where each integer from 1 to n appears exactly twice. The sum of n over all test cases does not exceed 50,000.
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
        
    #State: `t` remains the same, `n` remains the same, `k` is 0, `a` remains the same, `b` remains the same, `c` remains the same, `ans1` contains pairs of consecutive equal elements from `b` and the first `|k|/2` elements of `l`, `ans2` contains pairs of consecutive equal elements from `c` and the first `|k|/2` elements of `l`, `req` remains the same, `l` remains the same.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n`, an integer `k`, and a list `a` of 2n integers where each integer from 1 to n appears exactly twice. For each test case, it outputs two lists: `ans1` and `ans2`. These lists together contain `k` pairs of identical numbers from the input list `a`, with `ans1` and `ans2` each containing up to `k` numbers, ensuring that each number in the output appears exactly twice across both lists.

