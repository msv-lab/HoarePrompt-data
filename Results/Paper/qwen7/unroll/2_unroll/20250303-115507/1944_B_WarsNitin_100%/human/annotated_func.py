#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 5000. Each test case consists of two integers n and k such that 2 ≤ n ≤ 5 × 10^4 and 1 ≤ k ≤ ⌊n/2⌋. Additionally, there is an array a of length 2n containing each integer from 1 to n exactly twice.
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
        
    #State: The output state will consist of multiple pairs of lists printed for each iteration of the outer loop. For each iteration, two lists `ans1` and `ans2` are formed based on the sorted segments `b` and `c` of the input array `a`. The first list `ans1` contains elements from the first segment of `a` (excluding the last element if it's equal to its predecessor), and the second list `ans2` contains elements from the second segment of `a`. Each list is constructed by pairing adjacent equal elements and then filling with unique elements from both segments until `k` (doubled within the loop) is exhausted or the segments are fully processed.
#Overall this is what the function does:The function processes an array `a` of length 2n, where each integer from 1 to n appears exactly twice. It also takes two integers `n` and `k` as input. The function splits the array into two halves, sorts them, and constructs two lists `ans1` and `ans2` by pairing adjacent equal elements from these halves. If `k` is not exhausted, it fills the lists with unique elements from both halves until `k` is used up or the segments are fully processed. Finally, it prints the two lists for each test case.

