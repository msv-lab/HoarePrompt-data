#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n and k are integers where 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9, representing the number of non-negative integers to be printed and their sum, respectively.
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
        
    #State: After the loop executes all the iterations, `t` is 0, indicating that all test cases have been processed. For each test case, if `n` was 1, no changes were made to `n`, `k`, or any other variables. If `n` was not 1, `arr` remains an empty list, `k0` retains the original value of `k`, `i` is the largest integer such that \(2^i < k\), `ans` contains the values \((1 << i) - 1\), \(k - ((1 << i) - 1)\), and `n - 2` zeros, and `temp` is the largest power of 2 less than `k`. The loop has printed the list `ans` for each test case.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of two integers `n` and `k`. For each test case, if `n` is 1, it prints the integer `k`. Otherwise, it constructs a list of `n` non-negative integers that sum up to `k`, where the first two elements are calculated based on the largest power of 2 less than `k`, and the remaining elements are zeros. The function does not return any value; it only prints the results for each test case. After processing all test cases, the function completes its execution.

