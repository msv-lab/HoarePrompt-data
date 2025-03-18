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
        
    #State: Output State: The loop will continue to execute until there are no more inputs to process. After all iterations, `i` will be 255 (since the maximum value for `k` is \(10^9\) and the binary representation of numbers up to \(10^9\) has 29 bits, but `i` starts from 0 and goes up to 255 in the given code). The value of `t` will remain within the range \(1 \leq t \leq 10^4\). `l1` will contain the last input split into a list of strings. `n` and `k` will be the last values read from the input. `k0` will be equal to the last value of `k`. `arr` will contain a list of integers from 0 to 255, as it iterates through all possible bit positions for the maximum `k`. `ans` will be constructed based on the values in `arr`, with each element being either a power of 2 or zero, depending on whether the corresponding bit in `k` was set. The list `ans` will be padded with zeros to ensure its length matches `n`. The final `ans` list will contain the calculated values based on the last `k0` and the constructed `arr`.
    #
    #The exact content of `ans` cannot be determined without knowing the specific values of `n` and `k` for the last input, but it will follow the pattern described above.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \( n \) and \( k \). For each test case, it constructs a list `ans` based on the binary representation of \( k \). Specifically, it appends powers of 2 to `ans` corresponding to the bits set in \( k \), and pads the list with zeros to match the length \( n \). Finally, it prints the constructed list `ans` for each test case.

