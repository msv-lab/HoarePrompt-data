#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop iterates through each test case, and for each test case, it generates an array `ans` of length `n` where the elements are powers of 2 corresponding to the positions of 1s in the binary representation of `k`. The last element of `ans` is adjusted to ensure the sum of the array equals `k`. The loop then prints the elements of `ans` for each test case. The variables `t`, `n`, and `k` are updated for each test case, but their initial constraints remain the same.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by two integers `n` and `k` where 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9. For each test case, it generates an array `ans` of length `n` such that the sum of the elements in `ans` equals `k`. The elements of `ans` are powers of 2 corresponding to the positions of 1s in the binary representation of `k`, and any remaining positions in `ans` are filled with 0s. The function prints the elements of `ans` for each test case. After processing all test cases, the function completes, and the variables `t`, `n`, and `k` are reset for the next call.

