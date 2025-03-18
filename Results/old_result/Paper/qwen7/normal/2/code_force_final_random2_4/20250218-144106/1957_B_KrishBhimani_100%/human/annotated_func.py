#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of two integers n and k such that 1 ≤ n ≤ 2 \cdot 10^5 and 1 ≤ k ≤ 10^9, and the sum of n over all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: Output State: The loop has completed all its iterations. The variable `l1` is a list of strings obtained from splitting the input string for the last test case, `n` is the first element of `l1` converted to an integer, and `k` is the second element of `l1` converted to an integer. 
    #
    #If `n` equals 1, then `k` remains unchanged, and `ans` is simply `k` itself. Otherwise, `i` is the final value determined by the loop (either the number of times the loop executed or one less than that), `arr` is an empty list, `k0` equals `k`, `ans` is a list containing `(1 << i) - 1` and `k - sum(ans)`, and `temp` is 2 if `temp * 2 >= k` after the last iteration of the loop, otherwise `temp` is the highest power of 2 less than `k`. `ans` is extended by `[0] * (n - len(ans))` to match the length of `n`.
    #
    #All other variables that were not affected by the loop remain in their initial or previously calculated states from the last iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \( n \) and \( k \). For each test case, if \( n = 1 \), it prints \( k \) directly. Otherwise, it calculates a list \( ans \) containing two elements: \((1 << i) - 1\) and \( k - \text{sum}(ans) \), where \( i \) is the highest power of 2 less than or equal to \( k \). The list \( ans \) is then extended with zeros to match the length \( n \). The function prints the final list \( ans \) for each test case.

