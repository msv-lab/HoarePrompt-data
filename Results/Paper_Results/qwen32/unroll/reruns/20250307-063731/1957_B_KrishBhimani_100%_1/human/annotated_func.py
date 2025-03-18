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
        
    #State: For each test case, the output is a list of integers of length `n`. The first element is the largest power of 2 less than `k` minus 1, the second element is `k - (2^i - 1)`, and the rest of the elements are zeros.
#Overall this is what the function does:The function processes multiple test cases, each defined by two integers `n` and `k`. For each test case, it outputs a list of `n` integers. If `n` is 1, the output is simply `k`. Otherwise, the output list contains the largest power of 2 less than `k` minus 1 as the first element, followed by `k` minus this power of 2 minus 1 as the second element, and the rest of the elements are zeros.

