#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of two integers n and k such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9, and the sum of all n values across all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: The output state after the loop executes all iterations will be a list `ans` of length `n`. The list `arr` will contain indices where `k` had its least significant bit set to 1 during the loop. The variable `c` will be equal to `n` plus the number of bits set in `k`. The list `ans` will start with values derived from powers of 2 based on the indices in `arr`, and will be extended by zeros to match the length of `n`. Specifically, `ans` will contain values calculated as follows:
    #
    #- For each index `i` in `arr`, `ans` will include `1 << i`.
    #- If `c` equals `n - 1`, the remaining elements of `ans` will be filled with the value `k0 - sum(ans)`, followed by zeros to reach the length `n`.
    #
    #Given the example provided, if the loop runs multiple times and the final state of `arr` contains the indices where `k` had its bits set, and if `c` is calculated correctly, the final `ans` will be constructed according to the described rules. Since the exact values of `n`, `k`, and `t` are not specified, the final `ans` will depend on these inputs, but it will follow the pattern described above.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers \( n \) and \( k \). For each test case, it constructs a list `ans` of length \( n \) based on the binary representation of \( k \). Specifically, it identifies the positions of the least significant bits set to 1 in \( k \), and populates `ans` with powers of 2 corresponding to these positions. If the count of such positions plus one equals \( n \), it fills the remaining elements of `ans` with a specific value derived from `k` and zeros. The function outputs the constructed list `ans` for each test case.

