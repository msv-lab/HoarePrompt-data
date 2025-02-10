#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4; for each testcase, n, m, and k are integers where 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2 * 10^5; a is a list of n integers where 1 ≤ a_i ≤ 2 * 10^9 and a_i < a_{i+1}; d is a list of m integers where 1 ≤ d_i ≤ 10^9; f is a list of k integers where 1 ≤ f_i ≤ 10^9.
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
        
    #State: After all iterations of the loop, `t` is decremented by the number of iterations executed, and `res` holds the minimum value found during the loop execution for the maximum of `end - s`, `s - start`, and `nd` for all valid `s` values, where `s` is calculated as `f[j] + b[i]` or `f[j - 1] + b[i]` depending on the conditions specified in the loop. If `res` was initially `inf`, it remains unchanged. All other variables (`n`, `m`, `k`, `a`, `b`, `f`, `gap`, `start`, `end`, `mid`, `nd`) remain unchanged.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `m`, and `k`, and lists `a`, `b`, and `f`. For each test case, it calculates the minimum possible maximum gap between elements in a modified list derived from `a` by inserting an element `s` such that `s` is the sum of an element from `b` and an element from `f`. The function prints the result for each test case, which is either the minimum maximum gap found or the largest gap in the original list `a` if no valid `s` is found. The function does not return any value; it only prints the results.

