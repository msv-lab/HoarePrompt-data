#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each of the t test cases, there are two integers n and k such that 1 <= n <= 2 * 10^5 and 1 <= k <= 10^9. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: For each test case with integers `n` and `k`, the output is a line containing `n` integers. If `n` is 1, the output is `k`. Otherwise, the output starts with the largest power of 2 less than `k` minus 1, followed by the difference `k - (largest power of 2 less than k - 1)`, and then `n-2` zeros if necessary.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of two integers `n` and `k`. For each test case, it outputs `n` integers. If `n` is 1, the output is `k`. Otherwise, the output starts with the largest power of 2 less than `k` minus 1, followed by the difference between `k` and this largest power of 2 minus 1, and then `n-2` zeros if necessary.

