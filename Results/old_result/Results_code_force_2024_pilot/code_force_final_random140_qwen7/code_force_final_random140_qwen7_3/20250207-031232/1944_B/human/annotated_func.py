#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 5000. For each test case, n and k are integers such that 2 ≤ n ≤ 5 × 10^4 and 1 ≤ k ≤ ⌊n/2⌋. The list a is a list of 2n integers where each integer from 1 to n appears exactly twice.
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
        
    #State: Output State: `i` is `n-1`, `k` is `-2 * (n - 1)`, `ans1` is a list containing all pairs of consecutive duplicate elements from `b` found during the loop, `ans2` is a list containing all elements from `c[1]` onwards where each element is a duplicate of its preceding element, `q` is `t`, `req` is unchanged, `l` is an empty list.
    #
    #Explanation: After all iterations of the loop, `q` will be equal to `t` because the loop runs `t` times. The variable `i` will reach `n-1` as the loop continues to increment `i` until it reaches the end of `l`. The value of `k` will be `-2 * (n - 1)` because `k` is initially set to `2 * k` (which is `2 * (n + k)`, but `k` is set to `2 * k` again before the loop starts), and it decreases by 2 with each iteration of the loop. `ans1` will contain all pairs of consecutive duplicate elements from `b` found during the loop, and `ans2` will contain all elements from `c[1]` onwards where each element is a duplicate of its preceding element. Finally, `l` will be an empty list because no new elements are appended to it after the first three iterations.
#Overall this is what the function does:The function processes a series of test cases, each involving a list of 2n integers where each integer from 1 to n appears exactly twice. For each test case, it identifies and prints two lists of integers. The first list contains all pairs of consecutive duplicate elements from the first half of the input list, and the second list contains all elements from the second half of the input list where each element is a duplicate of its preceding element. The function handles up to 5000 test cases, where each test case involves a list size of up to 50,000 integers.

