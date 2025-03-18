#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2 · 10^5, k and x are integers such that 1 ≤ k, x ≤ n, and a_i are integers such that 1 ≤ a_i ≤ 1000. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    """
    Created on Fri Sep  6 21:42:15 2024
     
    @author: dehon
    """
    t = int(input())
    for _ in range(t):
        n, k, x = map(int, input().split())
        
        a = sorted(list(map(int, input().split())), reverse=True)
        
        ans1 = sum(a)
        
        for i in range(x):
            ans1 -= a[i] * 2
        
        ans2 = ans1
        
        for i in range(k):
            ans1 += a[i]
            if i + x < n:
                ans1 -= a[i + x] * 2
            ans = max(ans1, ans2)
        
        print(ans)
        
    #State: `t` is 0, `n`, `k`, and `x` are input integers, `a` is a list of input integers sorted in descending order, `i` is `k-1`, `ans1` is the sum of all elements in `a` minus `2 * (a[0] + a[1] + ... + a[x-1])` plus the sum of `a[j]` for `j` from 0 to `k-1` minus twice the sum of `a[j + x]` for `j` from 0 to `k-1` where `j + x < n`, `ans2` remains equal to the sum of all elements in `a` minus `2 * (a[0] + a[1] + ... + a[x-1])`, and `ans` is the maximum value between the final `ans1` and `ans2` for each test case.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of integers `n`, `k`, and `x`, followed by a list of `n` integers. It processes each test case to compute and print a result. The result is the maximum value between two computed sums: the sum of all elements in the list minus twice the sum of the first `x` elements, and a modified sum where the first `k` elements are added and the elements from position `k` to `k + x` (if within bounds) are subtracted twice. After processing all test cases, the function concludes with `t` being 0, and the results for each test case printed to standard output.

