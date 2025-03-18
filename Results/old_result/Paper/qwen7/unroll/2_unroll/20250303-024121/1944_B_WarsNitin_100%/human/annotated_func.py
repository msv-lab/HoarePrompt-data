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
        
    #State: Output State: The output state will consist of multiple pairs of lines, each pair corresponding to the output of one iteration of the loop. For each iteration:
    #
    #1. Two lists (`ans1` and `ans2`) are printed.
    #2. `ans1` contains elements from the first half of the sorted array `b`, and `ans2` contains elements from the second half of the sorted array `c`.
    #3. Elements are added to `ans1` and `ans2` based on the conditions in the loop, ensuring that no element is repeated more than necessary to meet the requirement of using up `k` elements (where `k` is initially twice the value of `k` provided in the input).
    #
    #Each line of output will contain space-separated integers representing the elements of `ans1` and `ans2` for that particular iteration.
#Overall this is what the function does:The function processes a list of 2n integers where each integer from 1 to n appears exactly twice, along with two integers n and k. It sorts the first half and the second half of the list separately. Based on the value of k, it constructs two lists, ans1 and ans2, by selecting elements from the sorted halves, ensuring no element is repeated more than necessary. Finally, it prints these two lists for each test case.

