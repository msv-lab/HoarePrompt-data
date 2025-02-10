#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2 \cdot 10^5. The list a contains n integers such that 1 ≤ a_i ≤ 2 \cdot 10^9 and a_i < a_{i+1}. The list d contains m integers such that 1 ≤ d_i ≤ 10^9. The list f contains k integers such that 1 ≤ f_i ≤ 10^9. The sum of n over all test cases does not exceed 10^5. The sum of m over all test cases does not exceed 2 \cdot 10^5. The sum of k over all test cases does not exceed 2 \cdot 10^5.
def func():
    for _ in range(int(input())):
        n, m, k = [*map(int, input().split())]
        
        a = [*map(int, input().split())]
        
        b = [*map(int, input().split())]
        
        f = [*map(int, input().split())]
        
        gap = [(y - x, x, y) for y, x in zip(a[1:], a)]
        
        gap.sort(reverse=True)
        
        start = gap[0][1]
        
        end = gap[0][2]
        
        mid = (start + end) // 2
        
        nd = 0 if len(gap) == 1 else gap[1][0]
        
        b.sort()
        
        f.sort()
        
        res = inf
        
        for i in range(m):
            remain = mid - b[i]
            j = bisect.bisect_left(f, remain)
            if j == k:
                s = f[j - 1] + b[i]
                if start < s < end:
                    res = min(res, max(end - s, s - start, nd))
            else:
                s = f[j] + b[i]
                if start < s < end:
                    res = min(res, max(end - s, s - start, nd))
                if j >= 1:
                    s = f[j - 1] + b[i]
                    if start < s < end:
                        res = min(res, max(end - s, s - start, nd))
        
        if res == inf:
            print(gap[0][0])
        else:
            print(res)
        
    #State: After the loop executes all the iterations, the variable `i` will be equal to `m`, indicating that the loop has completed all its iterations. The variable `res` will hold the minimum value among all the updates made during the loop iterations, where each update is the maximum of `end - s`, `s - start`, and `nd`, with `s` being either `f[j - 1] + b[i]` if `j` equals `k` or `f[j] + b[i]` if `j` is not equal to `k` and `j >= 1`. If no valid `s` is found that satisfies `start < s < end`, `res` will remain infinity (`inf`). The values of `end`, `start`, `nd`, `mid`, `b`, `f`, `k`, and `j` will remain unchanged from their initial or previous states within the loop body.
#Overall this is what the function does:The function processes multiple test cases, each containing integers t, n, m, k, a (a sorted list of n integers), d (a list of m integers), and f (a list of k integers). For each test case, it calculates and returns the minimum value among all possible updates. Each update is determined by finding a value s such that start < s < end, where start and end are derived from the list a, and s is either f[j - 1] + b[i] or f[j] + b[i]. If no valid s is found, it returns the maximum gap value from the list a.

