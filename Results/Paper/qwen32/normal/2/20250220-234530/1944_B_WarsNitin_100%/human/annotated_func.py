#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000. For each test case, n is an integer such that 2 ≤ n ≤ 50,000, and k is an integer such that 1 ≤ k ≤ ⌊n/2⌋. The array a is a list of 2n integers where each integer from 1 to n appears exactly twice. The sum of n over all test cases does not exceed 50,000.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 5000, `q` is `t-1` (the index of the last test case), `n` is an integer greater than 2, `a` is the list of integers read from the input for the last test case, `b` is the sorted list of the first `n` integers from `a` for the last test case, `c` is the sorted list of integers from `a` starting from index `n` to the end of `a` for the last test case, `ans1` contains pairs of consecutive equal elements from `b` up to the point where `k` becomes 0 plus elements from `l` until `k` reaches 0 or `l` is exhausted for the last test case, `req` is twice the second integer read from the input for the last test case, `i` is the last index processed before the loop breaks for the last test case, `ans2` contains pairs of consecutive equal elements from `c` up to the point where `k` becomes 0 plus elements from `l` until `k` reaches 0 or `l` is exhausted for the last test case, and `l` contains elements from `b` that are not part of any pair of consecutive equal elements and are not equal to their next element for the last test case. `k` is 0 if the loop broke due to `k` reaching 0, otherwise it is the remaining value.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it takes an integer `n` and an integer `k`, and a list `a` of 2n integers where each integer from 1 to n appears exactly twice. It then outputs two lists of integers, `ans1` and `ans2`, each containing `k` integers selected from the first `n` and the last `n` integers of the list `a`, respectively, following specific rules to ensure that pairs of equal integers are included when possible.

