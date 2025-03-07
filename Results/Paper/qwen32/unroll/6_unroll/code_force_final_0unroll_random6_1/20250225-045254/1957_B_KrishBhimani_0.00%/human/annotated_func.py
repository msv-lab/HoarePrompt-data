#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and k are integers such that 1 <= n <= 2 * 10^5 and 1 <= k <= 10^9. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: For each test case, a list `ans` of `n` integers where the first `n-1` elements are powers of 2 corresponding to the set bits in the binary representation of `k`, and the last element is chosen such that the sum of all elements in `ans` equals `k`. The state of `t`, `n`, and `k` from the initial conditions remain unchanged except that they have been processed.
#Overall this is what the function does:The function processes `t` test cases, each consisting of integers `n` and `k`. For each test case, it generates a list `ans` of `n` integers where the first `n-1` elements are powers of 2 corresponding to the set bits in the binary representation of `k`, and the last element is chosen such that the sum of all elements in `ans` equals `k`. The function prints this list for each test case.

