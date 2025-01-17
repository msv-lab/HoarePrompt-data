#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 ⋅ 10^5, and a is a list of n integers such that 1 ≤ a_i ≤ 10^9. The sum of all n across all test cases does not exceed 3 ⋅ 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    pref = [arr[i] for i in range(n)]
    for i in range(1, n):
        pref[i] += pref[i - 1]
        
    #State of the program after the  for loop has been executed: `i` is `n-1`; `n` must be greater than 1; `pref[0]` is unchanged; for all `j` in the range `[1, n-1]`, `pref[j]` is `(j+1) * pref[0]`
    ind = -1
    ans = [(10 ** 9) for i in range(n)]
    for i in range(n):
        curr = pref[i] - 2 * arr[i]
        
        ind1 = bisect.bisect_left(pref, curr)
        
        ind = min(ind, ind1)
        
        if ind >= 0 and curr > 0:
            ans[i] = i - ind
        
        if i - 1 >= 0 and arr[i] != arr[i - 1]:
            if arr[i] < arr[i - 1]:
                ans[i] = 1
                ind = i
        
    #State of the program after the  for loop has been executed: `i` is \( n-1 \), `n` is greater than 1, `curr` is \( pref[i] - 2 * arr[i] \), `ind1` is the leftmost insertion point of `curr` in the sorted list `pref`, `ind` is the minimum of its previous value and `ind1`, `ind` is greater than or equal to 0 and `curr` is greater than 0, `ans[i]` is \( i - ind \) if the condition `ind >= 0` and `curr > 0` is true, otherwise `ans[i]` remains \( 10 \); if `arr[i] < arr[i-1]`, then `ans[i]` is 1.
    ind = n
    for i in range(n - 1, -1, -1):
        curr = pref[i] + arr[i] + 1
        
        ind1 = bisect.bisect_left(pref, curr)
        
        ind = max(ind, ind1)
        
        if ind < n and curr <= pref[-1]:
            ans[i] = min(ans[i], ind - i)
        
        if i + 1 < n and arr[i] != arr[i + 1]:
            if arr[i] < arr[i + 1]:
                ans[i] = 1
                ind = i
        
    #State of the program after the  for loop has been executed: `i` is \(-1\), `curr` is `pref[0] + arr[0] + 1`, `ind1` is the smallest index in `pref` such that `pref[ind1] >= curr`, `ind` is the maximum of its original value and `ind1`, and for each `i` from \(n-1\) to 0, `ans[i]` is the minimum of its current value and `ind - i` if `ind < n` and `curr <= pref[-1]`, and if `arr[i] < arr[i + 1]` for any `i`, `ans[i]` is set to 1 and `ind` is set to `i`.
    for i in range(n):
        if ans[i] == 10 ** 9:
            ans[i] = -1
        
    #State of the program after the  for loop has been executed: `i` is -1, `curr` is `pref[0] + arr[0] + 1`, `ind1` is the smallest index in `pref` such that `pref[ind1] >= curr`, `ind` is the maximum of its original value and `ind1`, for each `i` from `n-1` to 0, `ans[i]` is -1 if the original value was `10
    print(*ans)
#Overall this is what the function does:The function processes a list of integers `a` for multiple test cases defined by `t`. It calculates an array `ans` where each element `ans[i]` represents the minimum distance to either a smaller element on the left or a larger element on the right for each element in the list `a`. If no such element exists, `ans[i]` is set to -1. The function first computes prefix sums and then iterates through the list twice to determine the minimum distances. After processing, it prints the resulting `ans` array. Potential edge cases include when the list `a` is empty or contains duplicate elements.

