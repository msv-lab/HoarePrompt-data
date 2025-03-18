#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, k, and x are integers such that 1 ≤ n ≤ 2 · 10^5, 1 ≤ k ≤ n, and 1 ≤ x ≤ n. The array a contains n integers such that 1 ≤ a_i ≤ 1000. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: t is an integer such that 0 ≤ t ≤ 10^4 - 1; the loop has executed `t` times, where for each execution, `n` is the first integer from the input, `k` is the second integer from the input, `x` is the third integer from the input, `a` is a sorted list of integers in reverse order, `sum1` is the sum of the list `a`, `ans` is a list containing `k + 1` elements, each computed as described above, and `sums` is the value computed in the last iteration (when `i = k`). The final output of the loop is the maximum value from `ans` for each of the `t` test cases.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `k`, `x`, and an array `a` of `n` integers. For each test case, it calculates and prints the maximum possible sum based on the specified conditions involving the array elements and the values of `k` and `x`.

