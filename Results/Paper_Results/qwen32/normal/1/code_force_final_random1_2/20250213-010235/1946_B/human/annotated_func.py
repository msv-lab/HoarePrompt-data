#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n, k ≤ 2 · 10^5. a is a list of n integers where each integer a_i satisfies -10^9 ≤ a_i ≤ 10^9. The sum of the values of n and k across all test cases does not exceed 2 · 10^5.
def func():
    t = int(input())
    for j in range(t):
        b = input().split()
        
        n = int(b[0])
        
        k = int(b[1])
        
        l = list(map(int, input().split()))
        
        suf = []
        
        suf.append(0)
        
        for i in range(n):
            suf.append(suf[i] + l[i])
        
        smin = [0]
        
        for i in range(n):
            if suf[i + 1] < smin[i]:
                smin.append(suf[i + 1])
            else:
                smin.append(smin[i])
        
        sm = -111
        
        for i in range(n + 1):
            if suf[i] - smin[i] > sm or sm == -111:
                sm = suf[i] - smin[i]
        
        sm = 2 ** k * sm - sm
        
        sm += suf[n]
        
        if sm < 0:
            a = abs(sm) // (10 ** 9 + 7)
            sm += (a + 1) * (10 ** 9 + 7)
        else:
            sm = sm % (10 ** 9 + 7)
        
        print(sm)
        
    #State: 
#Overall this is what the function does:The function processes multiple test cases. For each test case, it calculates a specific value based on the given integers `n` and `k`, and the list `a` of `n` integers. It computes a result that involves the maximum subarray sum adjusted by a factor of `2^k` minus the original maximum subarray sum, adds the total sum of the list `a`, and ensures the result is within the bounds of modulo \(10^9 + 7\). The result for each test case is printed.

