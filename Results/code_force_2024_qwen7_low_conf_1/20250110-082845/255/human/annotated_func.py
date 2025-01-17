#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 3⋅10^5, and a is a list of n positive integers such that 1 ≤ a_i ≤ 10^9. The sum of all n across all test cases does not exceed 3⋅10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    pref = [arr[i] for i in range(n)]
    for i in range(1, n):
        pref[i] += pref[i - 1]
        
    #State of the program after the  for loop has been executed: `pref[i]` for all `i` from 0 to `n-1` is the prefix sum of the list `arr` up to index `i`, `i` is `n`, and `pref` contains the prefix sums of `arr`.
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
        
    #State of the program after the  for loop has been executed: `pref[i]` for all `i` from 0 to `n-1` is the prefix sum of the list `arr` up to index `i`, `ind` is the minimum value between its original value and `i` if `arr[i] < arr[i - 1]` (or remains unchanged if `i - 1 < 0` or `arr[i] == arr[i - 1]`), `ans[i]` is `i - ind` if `i - 1 >= 0 and arr[i] < arr[i - 1]` and `ans[i]` remains unchanged otherwise, `curr` is `pref[i] - 2 * arr[i]` for each `i` from 0 to `n-1`, `ind1` is the index found by `bisect.bisect_left(pref, curr)` for each `i` from 0 to `n-1`, `ind` is the minimum value between its previous value and `i` for each `i` from 0 to `n-1`, `curr` is greater than 0 for each `i` from 0 to `n-1`, and `ans[i]` is updated to 1 if `arr[i] < arr[i - 1]` is true, otherwise `ans[i]` remains unchanged.
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
        
    #State of the program after the  for loop has been executed: `i` is `0`, `arr[i]` is `arr[0]`, `curr` is no longer defined, `ind1` is no longer defined, `ind` is the maximum value among all `ind1` values calculated, and `ans[i]` is updated to 1 if `arr[i] < arr[i + 1]` for `i + 1 < n`, otherwise `ans[i]` retains its previous value.
    for i in range(n):
        if ans[i] == 10 ** 9:
            ans[i] = -1
        
    #State of the program after the  for loop has been executed: `i` is `n`, `n` is a positive integer, and for each `j` in the range `[0, n-1]`, `ans[j]` is either `-1` or retains its original value if it was initially set to `10^9`.
    print(*ans)
#Overall this is what the function does:The function processes a series of test cases, each consisting of a positive integer \( n \) and a list \( a \) of \( n \) positive integers. It calculates and prints a list of results based on specific conditions involving prefix sums and comparisons within the list. Specifically, it computes a list `ans` where each element `ans[i]` represents the minimum number of elements that need to be removed from the list `a` starting from index `i` such that the remaining subarray is non-increasing. If no such subarray can be formed, `ans[i]` is set to -1.

