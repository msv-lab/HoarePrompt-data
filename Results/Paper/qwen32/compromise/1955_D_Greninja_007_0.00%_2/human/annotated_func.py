#State of the program right berfore the function call: a is a list of n integers (1 ≤ n ≤ 2 · 10^5), b is a list of m integers (1 ≤ m ≤ n ≤ 2 · 10^5), k is an integer (1 ≤ k ≤ m), n is the length of list a, and m is the length of list b. Each element in a and b is an integer between 1 and 10^6, inclusive. The sum of n over all test cases does not exceed 2 · 10^5, and the sum of m over all test cases does not exceed 2 · 10^5.
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
        
    #State: `good_subarrays` is the count of subarrays of length `m` in `a` where the sum of the minimum of the frequencies of each element in the subarray and in `b` is at least `k`. `b_freq` and `window_freq` are the frequency counters for `b` and the last window of `a` respectively. `matches` is the sum of the minimum of the frequencies of each element in the last window and in `b`.
    if (matches >= k) :
        good_subarrays += 1
    #State: `good_subarrays` is the count of subarrays of length `m` in `a` where the sum of the minimum of the frequencies of each element in the subarray and in `b` is at least `k`. If the current value of `matches` is at least `k`, then `good_subarrays` is increased by 1. `b_freq` and `window_freq` are the frequency counters for `b` and the last window of `a` respectively. `matches` is the sum of the minimum of the frequencies of each element in the last window and in `b`.
    return good_subarrays
    #The program returns `good_subarrays` which is the count of subarrays of length `m` in `a` where the sum of the minimum of the frequencies of each element in the subarray and in `b` is at least `k`.
#Overall this is what the function does:The function calculates and returns the count of subarrays of length `m` in list `a` where the sum of the minimum frequencies of each element in the subarray and in list `b` is at least `k`.

