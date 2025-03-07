#State of the program right berfore the function call: a is a list of n integers where 1 <= n <= 2 * 10^5, b is a list of m integers where 1 <= m <= n and 1 <= k <= m, and each element in a and b is an integer in the range 1 to 10^6.
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
        
    #State: `a` remains a list of n integers, `b` remains a list of m integers, `good_subarrays` is the number of subarrays of length m in `a` that have at least `k` elements matching the frequency in `b`, `b_freq` remains a Counter object with the frequency of each integer in `b`, `window_freq` is a Counter object with the frequency of the last m integers in `a`, `matches` is the sum of the minimum frequency of each integer in `window_freq` and `b_freq` for integers that are present in both `window_freq` and `b_freq`.
    if (matches >= k) :
        good_subarrays += 1
    #State: *`a` remains a list of n integers, `b` remains a list of m integers, `good_subarrays` is the number of subarrays of length m in `a` that have at least `k` elements matching the frequency in `b`. If `matches` is at least `k`, `good_subarrays` is incremented by 1. `b_freq` remains a Counter object with the frequency of each integer in `b`, and `window_freq` is a Counter object with the frequency of the last m integers in `a`. `matches` is the sum of the minimum frequency of each integer in `window_freq` and `b_freq` for integers that are present in both `window_freq` and `b_freq`.
    return good_subarrays
    #The program returns the number of subarrays of length m in `a` that have at least `k` elements matching the frequency in `b`.
#Overall this is what the function does:The function `func_1` accepts a list `a` of `n` integers, a list `b` of `m` integers, and integers `k`, `n`, and `m`. It returns the number of subarrays of length `m` in `a` that contain at least `k` elements whose frequencies match the frequencies in `b`. The lists `a` and `b` remain unchanged after the function execution.

