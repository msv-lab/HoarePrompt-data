#State of the program right berfore the function call: a is a list of n integers where 1 ≤ n ≤ 2 · 10^5, b is a list of m integers where 1 ≤ m ≤ n and m ≤ 2 · 10^5, k is an integer such that 1 ≤ k ≤ m, and the elements of a and b are integers in the range 1 to 10^6. Additionally, t is an integer representing the number of test cases where 1 ≤ t ≤ 10^4, and the sum of n over all test cases does not exceed 2 · 10^5, and the sum of m over all test cases does not exceed 2 · 10^5.
def func_1(a, b, k, n, m):
    good_subarrays = 0
    b_freq = Counter(b)
    window_freq = Counter(a[:m])
    matches = sum(min(window_freq[x], b_freq[x]) for x in window_freq if x in
    b_freq)
    for i in range(n - m):
        if matches >= k:
            good_subarrays += 1
        
        if a[i] in b_freq:
            matches -= min(window_freq[a[i]], b_freq[a[i]])
        
        window_freq[a[i]] -= 1
        
        if window_freq[a[i]] == 0:
            del window_freq[a[i]]
        
        if a[i + m] in b_freq:
            matches += min(window_freq[a[i + m]] + 1, b_freq[a[i + m]])
        
        window_freq[a[i + m]] += 1
        
    #State: `a` is a list of n integers, `b` is a list of m integers, `k` is an integer, `t` is an integer, `good_subarrays` is the count of subarrays of length m in a that have at least k matches with b, `b_freq` is a Counter object representing the frequency of elements in b, `window_freq` is a Counter object representing the frequency of elements in the last window a[n-m:n], `matches` is the sum of the minimum frequencies of elements in the last window a[n-m:n] that also exist in b_freq.
    if (matches >= k) :
        good_subarrays += 1
    #State: `a` is a list of n integers, `b` is a list of m integers, `k` is an integer, `t` is an integer, `good_subarrays` is the count of subarrays of length m in `a` that have at least `k` matches with `b`, `b_freq` is a Counter object representing the frequency of elements in `b`, `window_freq` is a Counter object representing the frequency of elements in the last window `a[n-m:n]`, `matches` is the sum of the minimum frequencies of elements in the last window `a[n-m:n]` that also exist in `b_freq`. If `matches` is greater than or equal to `k`, `good_subarrays` is incremented by 1.
    return good_subarrays
    #The program returns the count of subarrays of length m in list `a` that have at least `k` matches with list `b`.
#Overall this is what the function does:The function takes a list `a` of `n` integers, a list `b` of `m` integers, and an integer `k`. It returns the count of subarrays of length `m` in list `a` that have at least `k` elements in common with list `b`.

