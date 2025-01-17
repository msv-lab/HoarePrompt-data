def find_p(s, n, k):
    count = [0] * n
    for i in range(n):
        count[i] = count[i - 1] + (1 if s[i] == '1' else 0)

    for p in range(1, n + 1):
        reversed_count = count[p - 1] + (n - p) - (count[n - 1] - count[p - 1])
        shifted_count = count[p - 1] + (n - p)

        if reversed_count >= k and shifted_count % k == 0:
            return p

    return -1