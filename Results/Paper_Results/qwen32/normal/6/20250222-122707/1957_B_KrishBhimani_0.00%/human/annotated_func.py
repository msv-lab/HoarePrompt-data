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
        
    #State: After all iterations of the loop have finished, the output state will be as follows:
    #
    #- `t` remains the same, representing the number of test cases.
    #- For each test case, the output will be a list `ans` of length `n` where the sum of the elements in `ans` equals `k0` (the original value of `k` for that test case). The list `ans` is constructed by adding powers of 2 corresponding to the set bits in `k0` and adjusting the last element to ensure the sum matches `k0`.
    #
    #In natural language, after all iterations, the output state is that for each test case, a list `ans` of length `n` is printed where the sum of the elements in `ans` equals `k0` (the original value of `k` for that test case). The list is constructed by adding powers of 2 corresponding to the set bits in the binary representation of `k0` and adjusting the last element to ensure the sum matches `k0`.
    #
    #Output State:
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `k`. It then constructs and prints a list `ans` of length `n` where the sum of the elements in `ans` equals `k`. The list is constructed by adding powers of 2 corresponding to the set bits in the binary representation of `k` and adjusting the last element to ensure the sum matches `k`.

