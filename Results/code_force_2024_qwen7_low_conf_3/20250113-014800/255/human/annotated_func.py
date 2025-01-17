#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 3 ⋅ 10^5, and a is a list of n positive integers such that 1 ≤ a_i ≤ 10^9. The sum of all n across all test cases does not exceed 3 ⋅ 10^5.
def func_1():
    n = int(input())
    arr = list(map(int, input().split()))
    pref = [arr[i] for i in range(n)]
    for i in range(1, n):
        pref[i] += pref[i - 1]
        
    #State of the program after the  for loop has been executed: `t` is a positive integer such that \(1 \leq t \leq 10^4\), `n` is a positive integer such that \(1 \leq n \leq 3 \times 10^5\), `arr` is a list of integers, `pref` is a list of integers where `pref[0]` is the first element of `arr`, `pref[i]` for \(1 \leq i < n\) is the cumulative sum of the first `i+1` elements of `arr`, `pref[i]` for \(i \geq n\) is equal to `pref[n-1]`, `i` is `n` if the loop executes `n-1` times.
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
        
    #State of the program after the  for loop has been executed: `t` is a positive integer such that \(1 \leq t \leq 10^4\); `n` is a positive integer such that \(1 \leq n \leq 3 \times 10^5\); `arr` is a list of integers; `pref` is a list of integers; `ind` is the minimum of `-1` and the index where `curr` would be inserted in `pref`; `i` is `n`; `ans` is a list of length `n` where each element is either `i - ind` if `ind` is non-negative and `curr` is greater than `0`, or `1` if `arr[i] < arr[i-1]` and `i-1` is valid, otherwise `10`.
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
        
    #State of the program after the  for loop has been executed: `i` is 0, `curr` is `pref[0] + arr[0] + 1`, `t` is a positive integer between \(1 \leq t \leq 10^4\), `n` is a positive integer between \(1 \leq n \leq 3 \times 10^5\), `arr` and `pref` remain as lists of integers, `ind` is the maximum index such that `pref[ind]` is the largest prefix sum up to or including `arr[0] + 1`, `ans` is a list of length `n` where each element is determined based on the loop iterations, `ind1` is the same as `ind`.
    for i in range(n):
        if ans[i] == 10 ** 9:
            ans[i] = -1
        
    #State of the program after the  for loop has been executed: `i` is `n`, `curr` is `pref[0] + arr[0] + 1`, `t` is a positive integer between \(1 \leq t \leq 10^4\), `n` is a positive integer between \(1 \leq n \leq 3 \times 10^5\), `arr` and `pref` remain as lists of integers, `ind` is the maximum index such that `pref[ind]` is the largest prefix sum up to or including `arr[0] + 1`, `ans` is a list of length `n` where each element is either \(-1\) (if the corresponding `ans[i]` was initially \(10^9\)) or the original value, `ind1` is the same as `ind`.
    print(*ans)
#Overall this is what the function does:The function processes an input list `arr` of length `n` to generate a list `ans` of the same length. The function computes the prefix sums of `arr` and then iterates through the list to determine the minimum distance to a prefix sum that meets certain conditions. Specifically:

1. It calculates the prefix sums of `arr` and stores them in the list `pref`.
2. It initializes `ans` as a list of `n` elements, each set to a very large number (`10

