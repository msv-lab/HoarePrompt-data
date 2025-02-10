#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4; for each test case, n, m, and k are integers where 2 ≤ n ≤ 10^5, 1 ≤ m, k ≤ 2 × 10^5; a is a list of n integers where 1 ≤ a_i ≤ 2 × 10^9 and a_i < a_{i+1}; d is a list of m integers where 1 ≤ d_i ≤ 10^9; f is a list of k integers where 1 ≤ f_i ≤ 10^9.
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
        
    #State: After the loop completes all iterations, `_` will be equal to `t - 1`, indicating that the loop has run `t` times. The variables `n`, `m`, and `k` will hold the values from the last iteration's input. The lists `a`, `b`, and `f` will contain the values from the last iteration's input, with `b` and `f` being sorted. The list `gap` will contain tuples representing the differences between consecutive elements in `a`, sorted in descending order by the first element of each tuple. The variables `start` and `end` will be the second and third elements of the first tuple in `gap`, respectively. The variable `mid` will be `(start + end) // 2`. The variable `nd` will be 0 if the length of `gap` is 1, otherwise it will be the first element of the second tuple in `gap`. The variable `i` will be `m - 1`, indicating the last index of the list `b`. The variable `j` will be the last computed index of the first element in `f` that is not less than `mid - b[m-1]`. The variable `s` will be the last computed value of `f[j - 1] + b[m-1]` or `f[j] + b[m-1]` depending on the conditions. The variable `res` will be the minimum value found during the loop execution of the maximum of `end - s`, `s - start`, and `nd` for all valid `s` values within the range `start < s < end`. If `res` was initially `inf`, it will remain `inf` if no valid `s` was found; otherwise, it will be updated to the minimum valid value.
#Overall this is what the function does:The function reads multiple sets of inputs, each set representing a test case. For each test case, it takes integers `n`, `m`, and `k`, and lists `a`, `b`, and `f` as inputs. It then calculates the optimal position to place a new element in the list `a` such that the maximum gap between any two adjacent elements is minimized. This is done by considering the gaps between consecutive elements in `a`, sorting these gaps, and then using binary search to find the best position for the new element. The function prints the minimum possible maximum gap for each test case. After processing all test cases, the function completes without returning any value.

