def max_sum(arr):
    n = len(arr)
    inc = [0]*n
    dec = [0]*n
    for i in range(1, n):
        inc[i] = max(inc[i-1] + arr[i], arr[i])
    for i in range(n-2, -1, -1):
        dec[i] = max(dec[i+1] + arr[i], arr[i])
    max_sum = 0
    for i in range(n):
        max_sum = max(max_sum, inc[i] + dec[i] - arr[i])
    return max_sum