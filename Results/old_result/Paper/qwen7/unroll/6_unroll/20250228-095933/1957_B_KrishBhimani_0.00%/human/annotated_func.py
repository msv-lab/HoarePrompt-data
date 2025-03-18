#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of two integers n and k such that 1 ≤ n ≤ 2 \cdot 10^5 and 1 ≤ k ≤ 10^9, and the sum of all n values across all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: Output State: t test cases are processed, each test case outputs an array ans of length n, where ans[i] is either \(2^i\) or 0, and the last element of ans is always 0 if the number of elements in ans is less than n. The specific values of ans are determined based on the binary representation of k, with each set bit in k corresponding to a power of 2 in the ans array.
#Overall this is what the function does:The function processes multiple test cases, each containing two integers n and k. For each test case, it constructs an array ans of length n. This array contains either \(2^i\) or 0 for each index i, based on the binary representation of k. Specifically, if the i-th bit of k is set, ans[i] will be \(2^i\); otherwise, it will be 0. The function ensures that the last element of ans is always 0 if the array length is less than n. After processing all test cases, it prints the resulting array ans for each test case.

