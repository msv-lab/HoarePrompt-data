#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, k, and x are integers such that 1 ≤ n ≤ 2 · 10^5, 1 ≤ k ≤ n, and 1 ≤ x ≤ n. The array a contains n integers where each element a_i satisfies 1 ≤ a_i ≤ 1000. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for _ in range(int(input())):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        a.reverse()
        
        sum1 = sum(a)
        
        ans = []
        
        for i in range(k + 1):
            if i == 0:
                sums = sum1 - 2 * sum(a[:x])
                ans.append(sums)
            elif i + x - 1 < n:
                sums = sums + a[i - 1] - 2 * a[i + x - 1]
                ans.append(sums)
            else:
                sums = sums + a[i - 1]
                ans.append(sums)
        
        print(max(ans))
        
    #State: `t` is an integer such that 0 ≤ t ≤ 10^4 - `number_of_test_cases`, `n`, `k`, and `x` are integers read from the input, `a` is a list of `n` integers sorted in descending order, `sum1` is the sum of the elements in the original `a`, `ans` is a list containing `k + 1` values of `sums` computed during each iteration, and `sums` holds the value computed in the last iteration (`i = k`). This process has been repeated for all `number_of_test_cases` provided initially.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `n`, `k`, `x`, and a list `a` of `n` integers. For each test case, it calculates and prints the maximum possible sum after performing a series of operations involving the first `k` elements and the subarray of length `x`.

