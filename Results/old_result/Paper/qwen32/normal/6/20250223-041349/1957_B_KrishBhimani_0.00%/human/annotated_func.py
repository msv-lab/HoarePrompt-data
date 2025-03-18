#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each of the t test cases, n and k are integers such that 1 <= n <= 2 * 10^5 and 1 <= k <= 10^9. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: The output state after all iterations is a series of lists `ans` for each test case, where each `ans` is constructed based on the binary decomposition of `k` and adjusted to sum to `k`. Each `ans` list will have `n` elements, with the first `len(arr)` elements being powers of 2 corresponding to the positions of set bits in `k`, and the remaining elements being zeros, with the last element adjusted to ensure the sum equals `k`.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it takes two integers `n` and `k`. It generates a list `ans` of `n` elements where the sum of the elements equals `k`. The list is constructed using powers of 2 corresponding to the set bits in the binary representation of `k`, and the remaining elements are zeros, with the last element adjusted to ensure the sum equals `k`. The function outputs this list for each test case.

