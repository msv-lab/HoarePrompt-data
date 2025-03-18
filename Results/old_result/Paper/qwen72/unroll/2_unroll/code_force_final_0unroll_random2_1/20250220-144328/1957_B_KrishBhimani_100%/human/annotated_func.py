#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, n and k are integers such that 1 <= n <= 2 \cdot 10^5 and 1 <= k <= 10^9. The sum of n over all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: For each test case, the loop prints a sequence of integers. If n == 1, it prints the value of k. Otherwise, it prints a sequence of n integers where the first integer is the largest power of 2 less than k, the second integer is k minus the first integer, and the remaining n-2 integers are 0. The values of t, n, and k for each test case remain unchanged.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by two integers `n` and `k`. For each test case, if `n` is 1, it prints the value of `k`. Otherwise, it prints a sequence of `n` integers where the first integer is the largest power of 2 less than `k`, the second integer is `k` minus the first integer, and the remaining `n-2` integers are 0. The function does not return any value; it only prints the results. The values of `t`, `n`, and `k` for each test case remain unchanged after the function execution.

