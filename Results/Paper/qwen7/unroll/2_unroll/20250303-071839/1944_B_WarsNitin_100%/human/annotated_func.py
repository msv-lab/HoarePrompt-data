#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 5000. For each test case, n and k are integers satisfying 2 ≤ n ≤ 5 × 10^4 and 1 ≤ k ≤ ⌊n/2⌋. Additionally, a is a list of 2n integers where each integer from 1 to n appears exactly twice.
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
        
    #State: After executing the loop for `t` iterations, the output will consist of `t` pairs of lists. Each pair contains two lists `ans1` and `ans2`. The elements in `ans1` and `ans2` are derived from sorting the first `n` elements and the remaining elements of the input list `a`, respectively. The lists `ans1` and `ans2` are constructed by selecting elements based on the value of `k`, ensuring that no element is repeated more than twice unless it is the last or second last element in the sorted segments, and then filling the remaining positions with unique elements from the sorted segments.
#Overall this is what the function does:The function processes a list 'a' of 2n integers where each integer from 1 to n appears exactly twice, along with two integers 'n' and 'k'. It sorts the first n elements and the remaining elements separately. Based on the value of k, it constructs two lists, ans1 and ans2, by selecting elements from the sorted segments, ensuring no element is repeated more than twice unless it is the last or second last element in the sorted segments. Finally, it prints t pairs of lists, each containing ans1 and ans2, for t test cases.

