#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 5000), representing the number of test cases. Each test case consists of two integers n and k (2 ≤ n ≤ 5 · 10^4, 1 ≤ k ≤ ⌊n/2⌋), and a list a of 2n integers (1 ≤ a_i ≤ n) where each integer from 1 to n appears exactly twice. The sum of n over all test cases does not exceed 5 · 10^4.
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
        
    #State: After all iterations, `q` is `t - 1`, `n` is the last input integer for the final test case, `k` is 0 or less, `a` is the list of integers from the input for the final test case, `b` is a sorted list containing the first `n` elements of `a` for the final test case, `c` is a sorted list containing the elements of `a` starting from index `n` to the end of the list for the final test case, `ans1` contains pairs of elements from `b` where consecutive elements were equal, up to the point where `k` reached 0 or less, plus all elements from `l` that were processed before `k` became 0 or less, `ans2` contains pairs of elements from `c` where consecutive elements were equal, up to the point where `k` reached 0 or less, plus all elements from `l` that were processed before `k` became 0 or less, `l` has been fully iterated over, and `i` is the length of `l`. If `k` is 0, the loop terminates early.
#Overall this is what the function does:The function reads multiple test cases, each consisting of two integers `n` and `k`, and a list `a` of 2n integers where each integer from 1 to n appears exactly twice. For each test case, it splits the list `a` into two halves, sorts both halves, and then selects pairs of equal elements from these halves to form two lists `ans1` and `ans2`. The function ensures that each selected pair contributes to reducing the value of `k` by 2 until `k` reaches 0 or fewer. Any remaining elements that were not paired are also added to `ans1` and `ans2`. Finally, the function prints the contents of `ans1` and `ans2` for each test case. After processing all test cases, the function concludes with the final state of the program reflecting the last test case processed.

