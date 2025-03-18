#State of the program right berfore the function call: The function `func` is expected to take two parameters, `n` and `k`, where `n` is an integer such that 1 ≤ n ≤ 2 · 10^5, and `k` is an integer such that 1 ≤ k ≤ 10^9. Additionally, the function should be able to handle multiple test cases, where the number of test cases `t` is an integer such that 1 ≤ t ≤ 10^4. The sum of `n` over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop has processed all test cases. For each test case, the output is a list of integers `ans` of length `n`, where the sum of the elements in `ans` equals `k`. The elements in `ans` are powers of 2, and any remaining positions in the list are filled with zeros. The loop has finished executing, and all variables within the loop body have been reset for each new test case.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by two integers `n` and `k`. For each test case, it generates a list `ans` of length `n` such that the sum of the elements in `ans` equals `k`. The elements in `ans` are powers of 2, and any remaining positions in the list are filled with zeros. The function prints the list `ans` for each test case. After processing all test cases, the function concludes, and the final state is that all test cases have been processed and their respective lists have been printed.

