#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each of the next t lines contains two integers n and k such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for _ in range(int(input())):
        l1 = input().split()
        
        n, k = list(map(int, l1))
        
        arr = []
        
        k0 = k
        
        i = 0
        
        while k:
            if k & 1 == 1:
                arr.append(i)
            k = k >> 1
            i += 1
        
        ans = []
        
        c = 0
        
        for i in arr:
            if c == n - 1:
                ans.append(k0 - sum(ans))
                break
            c += 1
            ans.append(1 << i)
        
        ans += [0] * (n - len(ans))
        
        print(*ans)
        
    #State: For each test case, a list of n integers where the sum of the integers equals k, and the integers are the smallest possible powers of 2 that sum up to k, followed by zeros if necessary to reach the length n.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `n` and `k`. For each test case, it generates a list of `n` integers where the sum of the integers equals `k`. The integers in the list are the smallest possible powers of 2 that sum up to `k`, and if necessary, the list is padded with zeros to reach the length `n`. The function outputs this list for each test case.

