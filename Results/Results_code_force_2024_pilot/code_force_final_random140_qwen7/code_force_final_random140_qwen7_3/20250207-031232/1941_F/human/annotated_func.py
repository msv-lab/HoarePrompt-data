#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2 \cdot 10^5. The list a contains n integers such that 1 ≤ a_i ≤ 2 \cdot 10^9 and a_i < a_{i+1}. The list d contains m integers such that 1 ≤ d_i ≤ 10^9. The list f contains k integers such that 1 ≤ f_i ≤ 10^9.
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
        
    #State: After all iterations of the loop, `i` is equal to -1, `res` contains the minimum value found during the loop iterations under the condition `start < s < end`, and `mid` has been adjusted in each iteration based on the value of `b[i]`. If no valid minimum value was found, `res` remains infinity.
#Overall this is what the function does:The function processes multiple test cases, each involving four lists (a, d, f) and three integers (n, m, k). It calculates and returns the minimum value that satisfies a specific condition. Specifically, it finds the smallest possible value of `max(end - s, s - start, nd)` where `s` is the sum of an element from list `f` and an element from list `d`, and `start` and `end` are determined from list `a`. If no valid value is found, it returns the first gap value from list `a`.

