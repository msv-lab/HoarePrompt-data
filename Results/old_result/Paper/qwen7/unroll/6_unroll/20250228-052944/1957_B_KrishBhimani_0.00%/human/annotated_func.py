#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of two integers n and k such that 1 ≤ n ≤ 2 \cdot 10^5 and 1 ≤ k ≤ 10^9, and the sum of all n values across test cases does not exceed 2 \cdot 10^5.
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
        
    #State: Output State: The output state will consist of a series of lists `ans` for each test case, where each list contains integers generated based on the binary representation of `k` and padded to length `n` with zeros if necessary. Specifically, for each test case, the list `ans` will contain powers of 2 corresponding to the positions set in the binary representation of `k`, followed by zeros to make the total length of the list equal to `n`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \( n \) and \( k \). For each test case, it generates a list `ans` containing powers of 2 corresponding to the positions set in the binary representation of \( k \), and pads the list with zeros to ensure its length is \( n \). The function then prints this list for each test case.

