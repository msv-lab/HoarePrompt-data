#State of the program right berfore the function call: The function is expected to handle multiple test cases. For each test case, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop processes each test case and prints the resulting array `ans` for each test case. The array `ans` is constructed such that it contains powers of 2 corresponding to the positions where the binary representation of `k` has a 1, and the remaining elements are 0. If the length of `ans` is less than `n`, it is padded with zeros. After all iterations of the loop, the variables `n`, `k`, and `k0` are reset for the next test case, and the loop continues until all test cases are processed.
#Overall this is what the function does:The function processes multiple test cases, each defined by two integers `n` and `k`. For each test case, it constructs an array `ans` of length `n` where the elements are powers of 2 corresponding to the positions of 1s in the binary representation of `k`. If the number of 1s in `k` is less than `n`, the remaining elements in `ans` are set to 0. The function prints the array `ans` for each test case. After processing all test cases, the function concludes.

