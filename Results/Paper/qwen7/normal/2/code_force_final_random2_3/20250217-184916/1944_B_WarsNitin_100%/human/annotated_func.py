#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 5000. For each test case, n and k are integers satisfying 2 ≤ n ≤ 5 × 10^4 and 1 ≤ k ≤ ⌊n/2⌋. The array a is a list of 2n integers where each integer from 1 to n appears exactly twice.
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
        
    #State: Output State: `i` is `2 * n - 1`, `k` is `-n`, `ans1` contains all elements from `l`, and `ans2` contains pairs of consecutive equal elements from the list `c` starting from index 1 up to `n-1`.
    #
    #Explanation: After all iterations of the loop, `i` will have incremented to `2 * n - 1` since it starts from `n` and increments by 1 in each iteration until `k` becomes 0. At this point, `k` will be `-n` because it starts at `2 * k` (which is `2 * n` initially) and decreases by 1 with each iteration. `ans1` will contain all elements from `l` as the loop continues to add elements from `l` until `k` becomes 0. `ans2` will contain pairs of consecutive equal elements from the list `c` starting from index 1 up to `n-1`, unless `k` becomes 0 before reaching the end of the list.
#Overall this is what the function does:The function processes a list of 2n integers where each integer from 1 to n appears exactly twice. It then prints two lists: the first list contains pairs of integers from the first half of the original list that meet certain conditions, and the second list contains pairs of consecutive equal elements from the second half of the original list. The function handles multiple test cases specified by the variable `t`.

