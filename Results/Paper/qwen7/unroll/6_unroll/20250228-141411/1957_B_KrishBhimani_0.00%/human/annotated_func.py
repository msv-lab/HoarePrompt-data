#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n and k are positive integers such that 1 ≤ n ≤ 2 \cdot 10^5 and 1 ≤ k ≤ 10^9, and the sum of all n over all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n and k are positive integers such that 1 ≤ n ≤ 2 \cdot 10^5 and 1 ≤ k ≤ 10^9, and the sum of all n over all test cases does not exceed 2 \cdot 10^5; after executing the loop, ans is a list of length n filled with powers of 2 based on the binary representation of k, followed by zeros to make the total length of ans equal to n. If the length of ans is less than n after processing all bits of k, the remaining positions are filled with 0.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it takes two integers `n` and `k` as inputs. It then constructs a list `ans` containing `n` elements. Each element in `ans` is set to a power of 2 based on the binary representation of `k`. If the binary representation of `k` has fewer bits than `n`, the remaining elements in `ans` are filled with zeros. Finally, it prints the constructed list `ans` for each test case.

