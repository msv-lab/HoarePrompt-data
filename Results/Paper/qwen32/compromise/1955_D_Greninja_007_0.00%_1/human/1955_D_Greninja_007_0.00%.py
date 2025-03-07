from collections import Counter
 
def count_good_subarrays(a, b, k,n,m):
 
    good_subarrays = 0
    b_freq = Counter(b)
    window_freq = Counter(a[:m])
    matches = sum(min(window_freq[x], b_freq[x]) for x in window_freq if x in b_freq)
 
    for i in range(n - m):
        if matches >= k:
            good_subarrays += 1
        # Element exiting the window
        if a[i] in b_freq:
            matches -= min(window_freq[a[i]], b_freq[a[i]])
        window_freq[a[i]] -= 1
        if window_freq[a[i]] == 0:
            del window_freq[a[i]]
        # Element entering the window
        if a[i + m] in b_freq:
            matches += min(window_freq[a[i + m]] + 1, b_freq[a[i + m]])
        window_freq[a[i + m]] += 1
 
    # Check the last window
    if matches >= k:
        good_subarrays += 1
 
    return good_subarrays
 
for _ in range(int(input())):
    n,m,k = map(int,input().split(" "))
    a = list(map(int,input().split(" ")))
    b = list(map(int,input().split(" ")))
    print(count_good_subarrays(a, b, k,n,m))