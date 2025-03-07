#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 5000. Each test case consists of two integers n and k such that 2 ≤ n ≤ 5 × 10^4 and 1 ≤ k ≤ ⌊n/2⌋. Additionally, an array a of length 2n is given, where each integer from 1 to n appears exactly twice.
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
        
    #State: Output State: `i` is equal to `n + len(l)`, `k` is equal to `req - 2 * (2n - len(l) - 1)`, `ans1` contains all elements from the original list `l` and all pairs of consecutive identical elements found in the lists `b` and `c`, and `ans2` contains the same elements as `ans1`.
    #
    #Explanation: After the loop has executed all its iterations, the variable `i` will be equal to the total length of the list `l` plus `n`, indicating that the loop has processed every element in both the list `l` and the original lists `b` and `c`. The variable `k` will be equal to `req` minus twice the number of consecutive pairs found in the lists `b` and `c`, which is `2n - len(l) - 1`. The list `ans1` will contain all elements from the original list `l` and all pairs of consecutive identical elements found in the lists `b` and `c`. Similarly, the list `ans2` will contain the same elements as `ans1` since `ans1` and `ans2` append the same elements from `l`.
#Overall this is what the function does:The function processes multiple test cases, each defined by a positive integer \( t \) (1 ≤ \( t \) ≤ 5000), an array \( a \) of length 2\( n \) where each integer from 1 to \( n \) appears exactly twice, and two integers \( n \) and \( k \) (2 ≤ \( n \) ≤ 5 × 10^4, 1 ≤ \( k \) ≤ ⌊\( n \)/2⌋). For each test case, it splits the array \( a \) into two halves, sorts them, and then constructs two lists, \( ans1 \) and \( ans2 \), by selecting specific elements from the sorted halves and the original array. Finally, it prints these two lists. The function ensures that \( ans1 \) and \( ans2 \) contain all necessary elements from the original array and the sorted halves, adhering to the constraints on \( k \).

