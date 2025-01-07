def odd_Equivalent(s, n):
    s = s * (n // len(s) + 1)
    count = 0
    for i in range(n):
        temp = s[i:i+len(s)]
        count += temp.count('1') % 2
    return count
