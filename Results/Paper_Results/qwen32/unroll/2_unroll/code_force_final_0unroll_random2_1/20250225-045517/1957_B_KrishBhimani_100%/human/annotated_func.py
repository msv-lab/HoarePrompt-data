#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for _ in range(int(input())):
        l1 = input().split()
        
        n, k = list(map(int, l1))
        
        if n == 1:
            print(k)
        else:
            arr = []
            k0 = k
            i = 0
            ans = []
            temp = 1
            while True:
                if temp * 2 < k:
                    temp *= 2
                    i += 1
                else:
                    break
            ans.append((1 << i) - 1)
            ans.append(k - sum(ans))
            ans += [0] * (n - len(ans))
            print(*ans)
        
    #State: The output state is a series of printed lists corresponding to each test case. For each test case, if `n == 1`, it prints `k`. If `n > 1`, it prints a list starting with the largest power of 2 minus 1 that is less than `k`, followed by the remainder when `k` is subtracted by the sum of the list so far, and the rest of the list filled with zeros to make its length `n`.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of two integers `n` and `k`. If `n` is 1, it outputs `k`. If `n` is greater than 1, it outputs a list of length `n` starting with the largest power of 2 minus 1 that is less than `k`, followed by the remainder when `k` is subtracted by this power of 2 minus 1, and the rest of the list filled with zeros.

