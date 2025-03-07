#State of the program right berfore the function call: Each test case contains two integers n and k such that 2 \le n \le 5 \cdot 10^4 and 1 \leq k \leq \lfloor \frac{n}{2} \rfloor. The array a is of length 2n and contains integers from 1 to n, each appearing exactly twice.
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
        
    #State: For each test case, the loop outputs two lines of integers. The first line contains the integers from the first half of the sorted array `b` that are either duplicates or unique and not part of the last pair of duplicates. The second line contains the integers from the second half of the sorted array `c` that are duplicates. Both lines contain exactly `k` integers each, where `k` is the input value for that test case.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by two integers `n` and `k` and an array `a` of length `2n` containing integers from 1 to `n` (each appearing exactly twice). For each test case, it splits `a` into two halves `b` and `c`, sorts them, and then constructs two lists `ans1` and `ans2` by selecting elements based on the value of `k`. The first list `ans1` contains elements from the first half of the sorted array `b` that are either duplicates or unique and not part of the last pair of duplicates. The second list `ans2` contains elements from the second half of the sorted array `c` that are duplicates. Both lists are printed, each containing exactly `k` integers.

