#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each of the following t lines contains two integers n and k such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: a series of lists, each of length `n` corresponding to each test case, where each element is either a power of 2 corresponding to a set bit in `k` or `0`, and the sum of the elements in each list is less than or equal to `k`
#Overall this is what the function does:The function processes multiple test cases, each defined by two integers `n` and `k`. For each test case, it generates a list of length `n` where each element is either a power of 2 corresponding to a set bit in `k` or `0`, ensuring the sum of the elements in the list is less than or equal to `k`. The function outputs these lists, one for each test case.

